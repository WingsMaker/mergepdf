import sys
from PyPDF2 import PdfReader, PdfWriter
import pymsgbox as pm

if __name__ == "__main__":
    inp_file = pm.prompt("Enter filename of the PDF :","PDF to decrypt","example.pdf")
    if len(inp_file) > 0:
        output_file = "dec_" + inp_file
        password = pm.password("Enter password","password lock the pdf","888","*")
        print(f"loading input filename = {inp_file}")
        pm.confirm(f"loading input filename = {inp_file}", "reading source PDF", ['Ok'], timeout=1000)
        try:
            reader = PdfReader(inp_file)
            writer = PdfWriter()
            txt = ""
            if reader.is_encrypted:
                reader.decrypt(password)            
            for page in reader.pages:
                writer.add_page(page)
                txt = txt + page.extract_text()
            with open(output_file, "wb") as f:
                writer.write(f)
            print(f"File {output_file} created !")
            pm.alert(f"File {output_file} created !", 'PDF file decrypted')
            print(txt)
        except:
            print("unable to proceed")
            pm.alert("Unable to proceed","Decrypt PDF")
    else:
        pm.alert("Nothing to proceed","Decrypt PDF")