import PyPDF3
pdfFileObj= open("textpdf.pdf","rb")
pdfReader= PyPDF3.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()
