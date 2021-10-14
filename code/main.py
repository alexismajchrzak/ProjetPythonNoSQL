from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm
import game as g
import note as n
import editor as e
import rank as r
app = Flask(__name__)


# methods=["GET","PATCH"]
@app.route("/")
#
#cette fonction permet de renvoyer l'utilisateur vers différentes pages
#
def main():
    user = input('Quelle categorie souhaites-tu accéder?')
    match user:
        case ("jeux"):
            return g.game()
        case ("note"):
            return n.note()
        case ("editeur"):
            return e.editor()
        case ("classement"):
            return r.rank()
            
        

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
