from flask import Flask, render_template, send_from_directory, url_for, request, jsonify
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'mailparser'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello():
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = sorted(json.load(letters_file), key=lambda x: -int(x["data"]["discount"][:-1]))
    return render_template("index.html", letters=letters)

@app.route("/search")
def search():
    query = request.args.get('query', '', type=str)
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = sorted(json.load(letters_file), key=lambda x: -int(x["data"]["discount"][:-1]))
    letters = list(filter(lambda x: query.lower() in x["company"].lower(), letters))
    return render_template("index.html", letters=letters)

@app.route("/filter")
def filter_letters():
    query = request.args.get('query', '', type=str)
    letters = list()
    with open("mailparser/letters.json", 'r') as letters_file:
        letters = sorted(json.load(letters_file), key=lambda x: -int(x["data"]["discount"][:-1]))
    letters = list(filter(lambda x: query.lower() in x["company"].lower(), letters))
    return jsonify(letters)

def cooldatafilter(value):
    n_t_m = {"01":"января", "02":"февраля", "03":"марта",
                       "04":"апреля", "05":"мая", "06":"июня", "07":"июля", "08":"августа", 
                       "09":"сентября", "10":"октября", "11":"ноября", "12":"декабря"}

    day, month, year = value.split('.')
    date = "{} {}".format(int(day), n_t_m[month])
    return date

@app.route("/data/<filename>")
def upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# environment.filters['datetimeformat'] = datetimeformat

app.jinja_env.filters["cooldatafilter"] = cooldatafilter
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)