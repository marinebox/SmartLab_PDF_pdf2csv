# SL_PDF_pdf2csv

This python program reads the diffraction angles and intensities from a PDF format Powder Diffraction File (PDF) output by Rigaku's SmartLab Studio ii and output these data as a CSV file.

## Description

In the field of material science, X-ray diffraction(XRD) is an important method to determine if the desired crystalline phase is fabricated.

In the laboratory, it is sufficient to compare the obtained diffraction pattern with known powder diffraction file(PDF) using the analysis software. On the other hand, to making a graph, it is useful to be able to output these PDF data as a numerical file such as CSV.

Rigaku's SmartLab Studio ii is a integrated software to control XRD instrument and analyze diffraction pattern. This software can output PDF file. However, the output format is PDF(portable document file) only, and can not be output in other format such as CSV.

This program supports material researchers by reads the diffraction angles and intensities from a PDF format Powder Diffraction File (PDF) output by Rigaku's SmartLab Studio ii and output these data as a CSV file.

## Requirements

- python
- pdfminer.six

## How to use

```bash
python3 pdf2csv.py
```
pdf2csv.py converts all PDF file in the same directory. The CSV files are saved on the same directory.


```bash
python3 pdf2csv.py a b...
```
pdf2csv.py converts a, and b. if directory is specified, all PDF files in that directory will be converted.

```bash
python3 pdf2csv.py a b... -o c
```
Convert the same files as in the previous pattern. CSV files are saved on the directory C.

```bash
python3 pdf2csv.py -h
```
Show help message.
