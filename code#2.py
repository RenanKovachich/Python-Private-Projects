#Conversor de PDF para DOCX
from pdf2docx import converter

pdf_file = 'cloding.pdf'
docx_file = 'sample.docx'

cv = Converter(pdf_file)
cv.converter(docx_file)
cv.close()