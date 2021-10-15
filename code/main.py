from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm
import game as g
import note as n
import editorFile as e
import rank as r
app = Flask(__name__)


#
#cette fonction permet d'afficher la page principal
#
@app.route("/")
def main():
    return "j'chuis lo page d'acceuil, pour vrai j'chert pos vroiment à grand chose mais j'chui lo"
#
#cette fonction permet de renvoyer l'utilisateur vers différentes pages
#
   
@app.route('/jeux')
def gameMain():
    return g.game()
@app.route('/jeux/ajouter/<string:nameGame>/<int:idEditor>/<int:idGame>')
def addGameMain(idGame,nameGame,idEditor):
    return g.add(idGame,nameGame,idEditor)
@app.route('/jeux/supprimer/<string:nameGame>')
def deleteGameMain(nameGame):
    return g.delete(nameGame)
@app.route('/jeux/modifier/<string:nameGame>/<string:nameGame2>')
def modifyGameMain(nameGame,nameGame2):
    return g.edit(nameGame,nameGame2)
@app.route('/notes')
def noteMain():
    return n.note()
@app.route('/editeurs')
def editorMain():
    return e.editor()
@app.route('/editeurs/ajouter')
def addEditorMain():
    return e.addEditor()
@app.route('/editeurs/supprimer')
def suppEditorMain():
    return e.suppEditor()
@app.route('/editeurs/modifier')
def modifyEditorMain():
    return e.modifyEditor()
@app.route('/classements/<string:typeSort>')
def rankMain(typeSort):
    return r.rank(typeSort)
@app.route('/trier-par-notes')
def sortNote():
    return r.sortNote()
            
        

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
    