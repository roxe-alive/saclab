from flask import Flask, send_file, render_template

app =  Flask(__name__)


@app.route("/health")
def health_check():
    return "OK", 200

@app.route("/")
def rpdf():
    return send_file("Asset/lab.pdf")

@app.route("/r")
def index():
    return render_template("index.html")

@app.route("/readme.md")
def readme():
    return send_file("Asset/readme.md")

if __name__ == "__main__":
    app.run()
