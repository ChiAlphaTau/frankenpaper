# A Python program for combining questions from multiple exam papers into one
## Overview
This program is made with the intention of being used to combine questions from multiple years into one exam paper, so e.g. if you have a number of previous exam papers, each of which you have answered some of the questions, then you can construct an exam paper that is entirely unseen for taking as a mock.
The input papers must be all in one folder, and be PDFs. The output is a PDF.

## Installation
- You will need Python and PIP setup on your computer.
- You will need to install [PyPDF2](https://pypi.org/project/PyPDF2/).
- You will need to download the files in this repository (or at least the ones ending in `.py`, grouped together in a folder).

## Running
Assuming you have downloaded the files into a folder called `frankenpaper`, then running that folder as a python program should work.
On my system, on the command line (when in the folder containing the `frankenpaper` folder), that would be:
```
python3 frankenpaper ANY_ARGUMENTS
```
or
```
python3 -m frankenpaper ANY_ARGUMENTS
```
Presumably running the program in your editor of choice would also work.

## Usage
You need all your input files saved as PDFs in one folder, and you need a (possibly different to avoid overriding input files by accident) output folder. If you run the program without any arguments passed to it, it shall ask for all information required on the terminal.
Otherwise, how to use is explained if you pass `-h` as an argument to the program, where it then outputs the following help:
```
usage: [-h] [--verbose] [--dirin INPUT_DIR] [--dirout OUTPUT_DIR] [--saveas OUTPUT_NAME] [--code INPUT_CODE]

Python program to assemble pages from multiple PDFs into one pdf.
    The input code encodes the desired pages as a ';'-separated list of statements of the form 'file:pages', where:
        - 'file' is the name of the pdf within the input directory to get the page(s) from, without the .pdf extension
        - 'pages' consists of a ','-separated list of statements of the form:
            - 'num', to represent page#num only (1-indexed).
            - 'low-high' to represent pages low-high inclusive (1-indexed).
          ('pages' may optionally be wrapped in [],{} and/or () brackets to make it look nice.)
    E.g.:
        alpha:12;beta:1-2,5; alpha:{7,18,12-15}
    would generate page 12 of alpha.pdf, then pages 1, 2, 5 of beta.pdf, then pages 7, 18, 12, 13, 14, 15 of alpha.pdf (in that order).

Any arguments not supplied shall be asked for from the user during the program run.

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         Whether to output progress or not.
  --dirin INPUT_DIR, -i INPUT_DIR
                        The directory containing the input files.
  --dirout OUTPUT_DIR, -o OUTPUT_DIR
                        The directory to save the generated pdf to.
  --saveas OUTPUT_NAME, -s OUTPUT_NAME
                        The filename (excluding extension) within OUTPUT_DIR to output the pdf to.
  --code INPUT_CODE, -c INPUT_CODE
                        The code for which file to input, in file:num format, semicolon separated. If you're supplying this on the command line, then you may
                        need to wrap the code in "" quotes.
```

## License
The program, along with previous versions in the git history with no `LICENSE` file, are licensed under the license in `LICENSE`.

## Etymology
Frankenstein - a scientist in Mary Shelley's book of the same name that creates a monster by stitching together parts from various dead humans and other animals.

Frankenpaper - a program that creates an exam paper by stitching together questions from various past exam papers.
