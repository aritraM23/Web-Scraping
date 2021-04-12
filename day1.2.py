# merge pdfs together
# open your first doc
# open your second doc
#for each page copy it to third doc
# open your third doc

from PyPDF2 import PdfFileWriter,PdfFileReader

"""write_obj=PdfFileWriter()
pdf_list=["C:\\Users\\Aritra Marik\\Documents\\Letter.pdf","C:\\Users\\Aritra Marik\\Documents\\Letter2.pdf"]
for i in pdf_list:
	red_obj=PdfFileReader(i)
	pages= red_obj.getNumPages()
	b=list(range(pages)) #gives the sequence till the integer denoting the number of pages in the pdf
	for j in b:
		p=red_obj.getPage(j)
		write_obj.addPage(p)

write_obj.encrypt('ApesTogetherStrong','Aritra@2002',True)


pdf_file=open("C:\\Users\\Aritra Marik\\Desktop\\python_learn\\pdf1+pdf2.pdf",'wb')
write_obj.write(pdf_file)
"""
#read the pdf
#read the watermark
#create a new pdf
#merge each page and pdf

pdf=PdfFileReader("C:\\Users\\Aritra Marik\\Documents\\Letter.pdf")
watermark=PdfFileReader("C:\\Users\\Aritra Marik\\Downloads\\ketter3_watermark.pdf")
page_w=watermark.getPage(0)
new_pdf=PdfFileWriter()
page_num=pdf.getNumPages()
for i in range(page_num):
	page=pdf.getPage(i)
	page.mergePage(page_w)
	new_pdf.addPage(page)

pdf_file=open("C:\\Users\\Aritra Marik\\Desktop\\python_learn\\pdf1+pdf2_watermarked.pdf",'wb')
new_pdf.write(pdf_file)

pdf_file.close()