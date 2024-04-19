from PyPDF2 import PdfMerger
import os

code_help="""\
    Encode each page like 'file:num', separating each by a ';'
    E.g. Type:
        alpha:12;beta:1
    to get page 12 of alpha.pdf, followed by page 1 of beta.pdf.\
"""

def construct_pdf(input_dir,output_dir,input_code,output_name,verbose):
    input_files=dict()#To store the opened PDFs
    merger=PdfMerger()#Thing to merge the PDFs.

    for code in input_code.split(";"):#For each page in the requested output.
        [paper_key,page_num]=code.split(":")
        
        paper_key=paper_key.strip()
        if paper_key not in input_files:#If that paper that page is from has not been opened yet, open it.
            filename = os.path.join(input_dir,f"{paper_key}.pdf")
            input_files[paper_key]=open(filename,"rb")
            if(verbose):    print(f"----Opened {paper_key} as '{filename}'")

        page_num=int(page_num)#Get the page number
        
        merger.append(fileobj=input_files[paper_key], pages=(page_num-1,page_num))#Add that page to the desired output pdf.
        if(verbose):    print(f"Added {paper_key}'s page#{page_num}")

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
