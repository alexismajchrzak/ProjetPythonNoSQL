from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm

app = Flask(__name__)

#methods=["GET","PATCH"]
@app.route("/")

def main():
    print("hello_wolrd")
    
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )