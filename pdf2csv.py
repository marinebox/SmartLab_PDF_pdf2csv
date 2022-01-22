import os
import re
import argparse
import subprocess
import pandas as pd


def judgeValue(value: str):
    ret = None
    fl = re.compile('[0-9]+\.[0-9]+')
    hkl = re.compile('[0-9]+\s[0-9]+\s[0-9]')
    if fl.match(value):
        ret = 'float'
    elif hkl.match(value):
        ret = 'hkl'
    else:
        ret = 'integer'
    return ret


def makeCsv(data, outputName):
    # data[0]: degree
    # data[1]: dValue
    # data[2]: intensity
    # data[3]: hkl
    rows = []
    for i in range(20001):
        x = i / 100
        y = 0
        rows.append([x, y])
    for d in data:
        dx = d[0]
        dy = d[2]
        num = int(dx * 100 + 0.001)
        rows[num] = [dx, dy]
    rows.sort()
    df = pd.DataFrame(rows, columns=['two_theta', 'intensity'])
    df.to_csv(outputName, index=False)
    return


def pdf2csv(pdfpath: str, outpath: str):
    print('converting:', pdfpath)
    sub = subprocess.run(
        ['pdf2txt.py', pdfpath],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    basename = os.path.basename(pdfpath)
    basenameWoExt = os.path.splitext(basename)[0]
    if outpath == None:
        outpath = os.path.dirname(pdfpath)
        if outpath == '':
            outpath = '.'
    outputName = os.path.join(outpath, basenameWoExt + '.csv')

    passExpressions = re.compile(
        '^[0-9]+\.[0-9]+$|^[0-9]+$|^[0-9]+\s[0-9]+\s[0-9]+$')
    values = sub.stdout.decode('utf-8').split('\n')
    values = filter(lambda x: passExpressions.match(x), values)
    values = list(map(lambda x: [x, judgeValue(x)], values))
    previousValueType = None
    integerLength = None
    for e in values:
        presentValueType = e[1]
        if presentValueType != previousValueType:
            previousValueType = presentValueType
            if presentValueType == 'integer':
                integerLength = 1
        else:
            if previousValueType == 'integer':
                integerLength += 1
        e.append(integerLength)
    values = list(filter(lambda x: x[1] != 'integer', values))

    degrees = []
    dValues = []
    intensities = []
    hkls = []
    previousValueType = 'hkl'
    for i in range(len(values)):
        presentValueType = values[i][1]
        if previousValueType == 'hkl' and presentValueType == 'float':
            step = values[i][2]
            degrees += values[i + 0 * step: i + 1 * step]
            dValues += values[i + 1 * step: i + 2 * step]
            intensities += values[i + 2 * step: i + 3 * step]
            hkls += values[i + 3 * step: i + 4 * step]
            previousValueType = presentValueType
        else:
            previousValueType = presentValueType
            continue
    degrees = list(map(lambda x: float(x[0]), degrees))
    dValues = list(map(lambda x: float(x[0]), dValues))
    intensities = list(map(lambda x: float(x[0]), intensities))
    hkls = list(map(lambda x: x[0], hkls))
    data = []
    for i in range(len(degrees)):
        data.append([degrees[i], dValues[i], intensities[i], hkls[i]])

    makeCsv(data, outputName)
    return


def argParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='*', default='.',
                        help='specify input files or directories.')
    parser.add_argument('-o', '--output', nargs=1,
                        default=None, help='specify output directory.')
    args = parser.parse_args()
    return args


def main():
    args = argParser()
    inputs = args.input
    output = None
    if args.output != None:
        output = args.output[0]
        if not os.path.isdir(output):
            print(output, ': No such directory.')
            return

    for f in inputs:
        if os.path.isfile(f):
            if '.pdf' not in f:
                print(f, 'is not PDF file.')
                continue
            pdf2csv(f, output)
        elif os.path.isdir(f):
            pdfFiles = [fn for fn in os.listdir(f) if '.pdf' in fn]
            for df in pdfFiles:
                pdf2csv(os.path.join(f, df), output)
        else:
            print(f, ': No such file or directory.')
    return


if __name__ == '__main__':
    main()
