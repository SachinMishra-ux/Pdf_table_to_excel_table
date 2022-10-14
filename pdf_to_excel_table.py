import tabula
import pandas as pd
import numpy as np
from PyPDF2 import PdfFileMerger
import os
#file_name = 'abc.xlsx'
file_name1= 'abc1.xlsx'
def pdfmerger(path):
    """This function merges all the pdf from a specified source and give the merged(resultant) pdf to the specified destination"""
    allfiles = os.listdir(path)
    merger = PdfFileMerger()
    for pdf in allfiles:
        if pdf[-1:-4:-1]=='fdp':
            merger.append(pdf,'rb')
    merger.write("result.pdf")
    merger.close()
path='./'    
  

def create_excel():
    l=tabula.read_pdf("result.pdf",pages='all')
    # concatenating df1 and df2 along rows
    #vertical_concat = pd.concat(l, axis=0)
    l1=[]
    for j in l:
        j.drop(columns=j.columns[0], axis=1, inplace=True)
        l1.append(j)
    #vt=vertical_concat.transpose()
    # concatenating df3 and df4 along columns
    horizontal_concat = pd.concat(l1, axis=1)

    ht=horizontal_concat.transpose()

    #vt.to_excel(file_name,header=False)
    ht.to_excel(file_name1,header=False)

pdfmerger(path)  
create_excel()