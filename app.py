from flask import Flask, send_file


app =  Flask(__name__)

PDF_LINK = "PDFS/pypdf.pdf"
PDF_LINK_1 = "PDFS/mongodb.pdf"
PDF_LINK_2 = "PDFS/pdf2.pdf"

@app.route("/")
def render():
    return send_file(PDF_LINK)

@app.route("/1")
def mongo():
    return send_file(PDF_LINK_1)

@app.route("/2")
def getpdf():
    return send_file(PDF_LINK_2)

@app.route("/health")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run()