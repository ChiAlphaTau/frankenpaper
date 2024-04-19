import argparse
if __package__ == '':#So python3 frankenpaper works.
    from lib_frankenpaper import *
else:#So python3 -m frankenpaper works.
    from .lib_frankenpaper import *

#The following stuff makes it so the program works nicely as a command line program, including having a "help" output.
parser = argparse.ArgumentParser(description="Python program to assemble pages from multiple pdfs into one pdf.\n"+code_help)
parser.add_argument("--verbose","-v",dest="verbose",help="Whether to output progress or not.",action="store_true")
parser.add_argument("--dirin","-i",dest="input_dir",help="The directory containing the input files.")
parser.add_argument("--dirout","-o",dest="output_dir",help="The directory to save the generated pdf to.")
parser.add_argument("--saveas","-s",dest="output_name",help="The filename (excluding extension) within OUTPUT_DIR to output the pdf to.")
parser.add_argument("--code","-c",dest="input_code",help="The code for which file to input, in file:num format, semicolon separated.")
args=parser.parse_args()
construct_pdf_interactive(input_dir=args.input_dir,
                          output_dir=args.output_dir,
                          input_code=args.input_code,
                          output_name=args.output_name,
                          verbose=args.verbose) 
