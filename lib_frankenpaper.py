from PyPDF2 import PdfMerger
import os

code_help="""\
    The input code encodes the desired pages as a ';'-separated list of statements of the form 'file:pages', where:
        - 'file' is the name of the pdf within the input directory to get the page(s) from, without the .pdf extension
        - 'pages' consists of a ','-separated list of statements of the form:
            - 'num', to represent page#num only (1-indexed).
            - 'low-high' to represent pages low-high inclusive (1-indexed).
          ('pages' may optionally be wrapped in [],{} and/or () brackets to make it look nice.)
    E.g.:
        alpha:12;beta:1-2,5; alpha:{7,18,12-15}
    would generate page 12 of alpha.pdf, then pages 1, 2, 5 of beta.pdf, then pages 7, 18, 12, 13, 14, 15 of alpha.pdf (in that order).
\
"""

def construct_pdf(input_dir,output_dir,input_code,output_name,verbose):
    input_files=dict()#To store the opened PDFs
    merger=PdfMerger()#Thing to merge the PDFs.

    for code in input_code.split(";"):#For each document statement in the code.
        [paper_key,pages_code]=code.split(":")
        
        paper_key=paper_key.strip()
        if paper_key not in input_files:#If the paper that page is from has not been opened yet, open it.
            filename = os.path.join(input_dir,f"{paper_key}.pdf")
            input_files[paper_key]=open(filename,"rb")
            if(verbose):    print(f"----Opened {paper_key} as '{filename}'")

        for page_code in pages_code.strip("[]{}() \t").split(","):#Remove any aesthetic brackets from the list of pages, then split along the commas.
            page_range=page_code.split("-")
            if len(page_range)==1:#Then if that entry is of the form 'num', set pages to be only page#num.
                page_num=int(page_range[0])
                pages=(page_num-1,page_num)
                if(verbose):    addition_message = f"Added {paper_key}'s page#{page_num}"
            elif len(page_range)==2:#Otherwise if that entry is of the form 'low-high', set pages to pages#low-high (inclusive)
                pages=( int(page_range[0])-1 , int(page_range[1]) )
                if(verbose):    addition_message = f"Added {paper_key}'s pages#{pages[0]+1}-{pages[1]}"
            else:#Otherwise page code is invalid; tell the user and skip.
                print(f"{page_code} is not a valid page code; skipping this entry")
                continue
        
            merger.append(fileobj=input_files[paper_key], pages=pages)#Add the desired pages to the desired output pdf.
            if(verbose):    print(addition_message)#And output that have done so.

    filename=os.path.join(output_dir,f"{output_name}.pdf")
    with open(filename,"wb") as output_file:#Output the desired pdf.
        merger.write(output_file)
        if(verbose):    print(f"Saved pdf to '{filename}'")

    merger.close()#Clean up stuff.
    for f in input_files.values():
        f.close()
    if(verbose):    print("Done")

def construct_pdf_interactive(input_dir=None,output_dir=None,input_code=None,output_name=None,verbose=True):
    #For each argument that is None, it asks the user for the actual value from the command line. It then generates the pdf.
    if input_dir==None:
        input_dir=input("Input directory: ")
    if output_dir==None:
        output_dir=input("Output directory: ")
    if input_code==None:
        print("Please input 'code' for the output.")
        print(code_help)
        input_code=input()
    if output_name==None:
        output_name=input("Name of generated file (no file extension): ")

    construct_pdf(input_dir,output_dir,input_code,output_name,verbose)
