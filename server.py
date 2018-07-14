from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello():
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = json.load(letters_file)
    return render_template("index.html", letters=letters)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)