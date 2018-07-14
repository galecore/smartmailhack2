from flask import Flask, render_template, send_from_directory, url_for, request
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'mailparser'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello():
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = json.load(letters_file)
    return render_template("index.html", letters=letters)

@app.route("/search")
def search():
    query = request.args.get('query', '', type=str)
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = json.load(letters_file)
    letters = list(filter(lambda x: query.lower() in x["company"].lower(), letters))
    return render_template("index.html", letters=letters)

@app.route("/data/<filename>")
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)