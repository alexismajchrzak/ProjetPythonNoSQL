from logging import root
from flask import Flask, redirect, url_for, request
import pymongo as pm
import urllib.parse as urlparse
from urllib.parse import parse_qs


app = Flask(__name__)

@app.route("/jeux")
def game():
    '''
    il y a 5 tableau pour l'affichage sur la page web
    '''
    tabCollnameGame = []
    tabNameGame = []
    tabIdGame = []
    tabDecoration = []
    tabDecorationSup = []
    '''
    les variables sont définie à ce moment pour avoir accès à ces-dernieres
    depuis n'importe ou dans la fonction 
    '''
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    '''
    ci-dessous, nous retrouvons les boucles qui servent à afficher les tableaus ci-dessus
    dans la page web
    '''
    for i in coll.find():
        tabCollnameGame.append(i)
    for t in tabCollnameGame:
        tabNameGame.append(t["nameGame"])
        tabIdGame.append(t["idGame"])
    for j in tabNameGame:
        tabDecorationSup.append(f'{j}')
    for y in range(len(tabNameGame)):
        tabDecoration.append(f'nom du jeux : {tabDecorationSup[y]} ; id du jeux : {tabIdGame[y]}<br>')

    return f'{tabDecoration}'
@app.route('/jeux/ajouter/<string:nameGame>/<int:idEditor>/<int:idGame>')
#
#fonction qui ajoute un article à partir des paramêtres d'URL 
#elle prend en entrée idGame, nameGame et idEditor
#retourne un tableau avec l'élément ajouter 
#
def add(idGame,nameGame,idEditor):
    '''
    il y a 5 tableau pour l'affichage sur la page web
    '''
    tabCollnameGame = []
    tabNameGame = []
    tabIdGame = []
    tabDecoration = []
    tabDecorationSup = []
    '''
    les variables sont définie à ce moment pour avoir accès à ces-dernieres
    depuis n'importe ou dans la fonction 
    '''
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    '''
    la ligne ci-dessous permet d'ajouter un document dans base de donnée,
    en rentrant dans l'URL le nom du jeux, puis l'index de l'editeur et l'index du jeux
    ex:
        localhost:8001/jeux/ajouter/nomDuJeux/indexDEditeur/indexDeJeux
    '''
    coll.insert_one({"idGame":idGame,"nameGame":f'{nameGame}',"idEditor":idEditor,"meanNote":0})
    '''
    ci-dessous, nous retrouvons les boucles qui servent à afficher les tableaus ci-dessus
    dans la page web
    '''
    for i in coll.find():
        tabCollnameGame.append(i)
    for t in tabCollnameGame:
        tabNameGame.append(t["nameGame"])
        tabIdGame.append(t["idGame"])
    for j in tabNameGame:
        tabDecorationSup.append(f'{j}')
    for y in range(len(tabNameGame)):
        tabDecoration.append(f'nom du jeux : {tabDecorationSup[y]} ; id du jeux : {tabIdGame[y]}<br>')

    return f'{tabDecoration}'

@app.route('/jeux/supprimer/<string:nameGame>')
#
#fonction qui supprime un article à partir des paramêtres d'URL 
#retourne un tableau sans l'élément supprimer
#
def delete(nameGame):
    '''
    il y a 5 tableau pour l'affichage sur la page web
    '''
    tabCollnameGame = []
    tabNameGame = []
    tabIdGame = []
    tabDecoration = []
    tabDecorationSup = []
    '''
    les variables sont définie à ce moment pour avoir accès à ces-dernieres
    depuis n'importe ou dans la fonction 
    '''
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    '''
    la ligne ci-dessous permet de supprimer tous les document de la base de donnée qui ont
    le même nom, en rentrant dans l'URL le nom du jeux 
    ex:
        localhost:8001/jeux/supprimer/nomDuJeuxÀSupprimer
    '''
    coll.delete_many({"nameGame":f'{nameGame}'})
    '''
    ci-dessous, nous retrouvons les boucles qui servent à afficher les tableaus ci-dessus
    dans la page web
    '''
    for i in coll.find():
        tabCollnameGame.append(i)
    for t in tabCollnameGame:
        tabNameGame.append(t["nameGame"])
        tabIdGame.append(t["idGame"])
    for j in tabNameGame:
        tabDecorationSup.append(f'{j}')
    for y in range(len(tabNameGame)):
        tabDecoration.append(f'nom du jeux : {tabDecorationSup[y]} ; id du jeux : {tabIdGame[y]}<br>')
    return f'{tabDecoration}'
#
#fonction qui modifie un article à partir des paramêtres de URL 
#retourne un tableau avec l'élément modifier
#
@app.route('/jeux/modifier/<string:nameGame>/<string:nameGame2>')
def edit(nameGame,nameGame2):
    '''
    il y a 5 tableau pour l'affichage sur la page web
    '''
    tabCollnameGame = []
    tabNameGame = []
    tabIdGame = []
    tabDecoration = []
    tabDecorationSup = []
    '''
    les variables sont définie à ce moment pour avoir accès à ces-dernieres
    depuis n'importe ou dans la fonction 
    '''
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    '''
    la ligne ci-dessous permet de modifier un document de la base de donnée 
    en rentrant dans URL le nom du jeux à modifier puis en quoi le modifier
    ex:
        localhost/jeux/modifier/nomDuJeuxDeBase/nomDuJeuxApresFonction
    '''
    coll.find_and_modify(
        query={'nameGame':f'{nameGame}'}, 
        update={"$set": {'nameGame':f'{nameGame2}'}}, 
        upsert=False, 
        full_response= True
        )
    '''
    ci-dessous, nous retrouvons les boucles qui servent à afficher les tableaus ci-dessus
    dans la page web
    '''
    for i in coll.find():
        tabCollnameGame.append(i)
    for t in tabCollnameGame:
        tabNameGame.append(t["nameGame"])
        tabIdGame.append(t["idGame"])
    for j in tabNameGame:
        tabDecorationSup.append(f'{j}')
    for y in range(len(tabNameGame)):
        tabDecoration.append(f'nom du jeux : {tabDecorationSup[y]} ; id du jeux : {tabIdGame[y]}<br>')
    return f'{tabDecoration}'
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )