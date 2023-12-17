import sys
from PyPDF2 import PdfReader, PdfWriter
import pymsgbox as pm

def getpdftext(inp_file,password):
    txt = ""
    try:
        reader = PdfReader(inp_file)
        writer = PdfWriter()
        if reader.is_encrypted:
            reader.decrypt(password)            
        for page in reader.pages:
            writer.add_page(page)
            txt = txt + page.extract_text()
        print(txt)
    except:
        print("unable to proceed")
    return txt

if __name__ == "__main__":
    inp_file = pm.prompt("Enter filename of the PDF :","PDF to decrypt","example.pdf")
    if len(inp_file) > 0:
        password = pm.password("Enter password","password lock the pdf","888","*")
        print(f"loading input filename = {inp_file}")
        pm.confirm(f"loading input filename = {inp_file}", "reading source PDF", ['Ok'], timeout=1000)
        txt = ""
        try:
            txt = getpdftext(inp_file,password)
            pm.alert(txt,"Decrypt PDF")
        except:
            print("unable to proceed")
            pm.alert("Unable to proceed","Decrypt PDF")
    else:
        pm.alert("Nothing to proceed","Decrypt PDF")
        