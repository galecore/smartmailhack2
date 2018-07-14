from flask import Flask, render_template, send_from_directory
import json

app = Flask(__name__)

@app.route("/")
def hello():
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = json.load(letters_file)
    return render_template("index.html", letters=letters)

@app.route("/data/<filename>")
def upload(filename):
    return send_from_directory("/mailparser", filename)
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)