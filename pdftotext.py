# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:47:39 2016

@author: Ketakee Nimavat
"""

import pyPdf

def getPDFContent(path):
    content = ""
    num_pages = 1
    p = file(path, "rb")
    pdf = pyPdf.PdfFileReader(p)
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
        print(content)
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content
    
 
f= open('D:\\Projects\\PDFFormParser\\pdftext.txt','w')   
pdfl=getPDFContent("D:\\Projects\\PDFFormParser\\test.pdf").encode("ascii", "ignore")
print(pdfl)
f.write(pdfl)
f.close()