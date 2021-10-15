from flask import Flask, request
import pymongo as pm



'''
- Classement odre alphabétique ou inverssé et classement par note 

:parameter : none 

    return body : string [] 
'''

app = Flask(__name__)
@app.route('/classement/<string:typeSort>')
def rank(typeSort):
    tab = []
    tab2 = []
    tabIdGame = []
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    for i in client.fillingGame.game.find():
        tab.append(i)
    for t in db.list_collection_names():
        body = t
        tab2.append(body)
    for w in coll.find():
        print(w["nameGame"])
    for y in range(len(tab)):
        tabIdGame.append(f' a-z : {tab[y]["nameGame"]} <br>')
    if typeSort == 'alphabetique':
        return f'{sorted(tabIdGame)}'
    if typeSort == 'alphabetique-inverser':
        return f'{sorted(tabIdGame , reverse=True)}'
    
@app.route('/trier-par-note')
def sortNote():
    tab = []
    tab2 = []
    tabIdGame = []
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    for i in client.fillingGame.game.find():
        tab.append(i)
    for t in db.list_collection_names():
        body = t
        tab2.append(body)
    for w in coll.find():
        print(w["nameGame"])
    for y in range(len(tab)):
        tabIdGame.append(f' note: {tab[y]["meanNote"]}/5 {tab[y]["nameGame"]} <br>')
    return f'{sorted(tabIdGame, reverse=True)}'



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )