from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm

app = Flask(__name__)


# methods=["GET","PATCH"]
@app.route("/")
def main():


    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    for i in client.fillingGame.game.find():
        print(i)
    return 'nb'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
