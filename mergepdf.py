import PyPDF2

def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(pdf)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

def main():
    # pdf files to merge
    pdfs = ['example1.pdf', 'example2.pdf']

    # output pdf file name
    output = 'example12.pdf'

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)

    
if __name__ == "__main__":
    # calling the main function
    main()
    print("merge pdf task completed")

