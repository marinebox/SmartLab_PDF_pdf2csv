# SL_PDF_pdf2csv

This python program reads the diffraction angles and intensities from a PDF format Powder Diffraction File (PDF) output by Rigaku's SmartLab Studio ii and output these data as a CSV file.

## Description

In the field of material science, X-ray diffraction(XRD) is an important method to determine if the desired crystalline phase is fabricated.

In the laboratory, it is sufficient to able to compare the obtained diffraction pattern with known powder diffraction file(PDF) using the analysis software. On the other hand, when making a XRD chart, it is useful to be able to output powder diffraction data as a numerical file such as CSV.

Rigaku's SmartLab Studio ii is a integrated software to control XRD instrument and analyze diffraction pattern. This software can output powder diffraction file. However, the output format is PDF(portable document file) only, and can not be output in other format such as CSV.

This program supports material researchers by reads the diffraction angles and intensities from a PDF format Powder Diffraction File (PDF) output by Rigaku's SmartLab Studio ii and output these data as a CSV file.

## Requirements

- python
- pandas
- pdfminer.six

## How to use

```bash
python3 pdf2csv.py
```
pdf2csv.py converts all powder diffraction files in the same directory. The CSV files will be created on the same directory.

```bash
python3 pdf2csv.py -h
```
Show help message.

## Others

Bug reports, feature requests, and any pull requests are always welcome.

## LICENSE

[MIT](LICENSE)


