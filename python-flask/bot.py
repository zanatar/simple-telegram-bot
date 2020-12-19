from flask import Flask
import requests
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, World!"

from flask import request

@app.route('/', methods=['POST'])
def login():
    message = request.form.get('message')
    send = requests.get('https://api.telegram.org/bot1060484360:AAEjYmNL-qcz1ngqOksgRFAV_rq6AHZCuvo/sendMessage?chat_id=-1001134991563&text='+message)

    return message
app.run(host='0.0.0.0', port=6400)
