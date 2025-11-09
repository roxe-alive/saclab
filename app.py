from flask import Flask, send_file


app =  Flask(__name__)

PDF_LINK = "PDFS/pypdf.pdf"
@app.route("/")
def render():
    return send_file(PDF_LINK)

if __name__ == "__main__":
    app.run()