from flask import Flask, send_file, render_template

app =  Flask(__name__)


@app.route("/health")
def health_check():
    return "OK", 200

@app.route("/")
def rpdf():
    return "etha Mone , Fear ayo :/" , 403

if __name__ == "__main__":
    app.run()
