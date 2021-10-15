from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm
#import game as g
#import note as n
#import editor as e
import rank as r
app = Flask(__name__)


# methods=["GET","PATCH"]
@app.route("/")
#
#cette fonction permet de renvoyer l'utilisateur vers différentes pages
#
   
@app.route('/jeux')
def gameMain():
    return g.game()
@app.route('/note')
def noteMain():
    return n.note()
@app.route('/editeur')
def editorMain():
    return e.editor()
@app.route('/classement/<string:typeSort>')
def rankMain(typeSort):
    return r.rank(typeSort)
@app.route('/trier-par-note')
def sortNote():
    return r.sortNote()
            
        

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
