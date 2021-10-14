from flask import Flask, request
import pymongo as pm

app = Flask(__name__)

@app.route('/classement')
def rank():
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
    return f'{sorted(tabIdGame)}'


@app.route('/classement/note')
def rankNote():
    tab3 = []
    tab4 = []
    tabIdGamee = []
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame
    coll = db.game
    for i in client.fillingGame.game.find():
        tab3.append(i)
    for t in db.list_collection_names():
        body = t
        tab4.append(body)
    for w in coll.find():
        print(w["nameGame"])
    for y in range(len(tab4)):
        tabIdGamee.append(f' note: {tab3[y]["meanNote"]}/5 {tab3[y]["nameGame"]} <br>')
    return f'{(tabIdGamee)}'





if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
