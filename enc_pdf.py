import sys
from PyPDF2 import PdfReader, PdfWriter
import pymsgbox as pm

if __name__ == "__main__":
    #argc = len(sys.argv)
    #for i, arg in enumerate(sys.argv):
        #print(f"Argument {i:>6}: {arg}")
    inp_file = pm.prompt("Enter filename of the PDF :","PDF to encrypt","example.pdf")
    if len(inp_file) > 0:
        output_file = "enc_" + inp_file
        password = pm.password("Enter password","password lock the pdf","888","*")
        print(f"loading input filename = {inp_file}")
        pm.confirm(f"loading input filename = {inp_file}", "reading source PDF", ['Ok'], timeout=1000)
        try:
            reader = PdfReader(inp_file)
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            writer.encrypt(password)
            with open(output_file, "wb") as f:
                writer.write(f)
            print(f"File {output_file} created !")
            pm.alert(f"File {output_file} created !", 'PDF file encrypted')
        except:
            print("unable to proceed")
            pm.alert("Unable to proceed","Encrypt PDF")
    else:
        pm.alert("Nothing to proceed","Encrypt PDF")