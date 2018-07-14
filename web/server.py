from flask import Flask
import json as js
print('f')
app = Flask(__name__)

@app.route('/get')
def get_json():
    FUCKING_JSON=js.dumps([{'id':'1', 'content':'Пятёрочка | Скидка 50% на хлеб', 'start':'29.07.2018', 'end':'30.07.2018'},{'id':'2', 'content':'Пятёрочка2 | Скидка 50% на хлеб', 'start':'18.07.2018', 'end':'24.07.2018'}, {'id':'3', 'content':'Пятёрочка3 | Скидка 50% на хлеб', 'start':'23.07.2018', 'end':'28.07.2018'}])
    return FUCKING_JSON
