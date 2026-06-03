from flask import Flask
import requests
import jwt
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World - This app uses vulnerable dependencies!"

@app.route('/test')
def test():
    return {
        "message": "Testing endpoint",
        "status": "ok"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
