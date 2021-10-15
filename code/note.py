from flask import Flask
from flask import request
from flask import make_response
import pymongo as pm

app = Flask(__name__)


#
# Affichage dans la route /note (dans l'url)
# Fonction note permet d'afficher la moyenne de toutes les notes d'un meme idGame
#
@app.route("/note")
def note():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    db = client.fillingGame

    affichage=''
    '''
    Pour j qui est dans la collection game 
    On récupere simplement l'id de notre jeu
    On créer un tableau pour y stocké nos note calculé
    '''
    for j in db.game.find():
        gameid = int(str(j["idGame"]))
        #print(gameid)
        TbNote = []
        '''
        Pour mydoc dans la collection mean on récupere:
            idGame de la note
            gameid = idGame des jeux
        '''
        for mydoc in db.mean.find({"idGame": gameid}):
            #print(str(mydoc))
            #print(str(j))
            '''
            Si idGame des notes est egal a l'idGame du jeux
            On envoie la note dans le tableau TbNote
                S = base du calcul de la moyenne
            '''
            if mydoc["idGame"] == j["idGame"]:
                TbNote.append(mydoc["idNote"])
                s = 0
                #print(TbNote)
                '''
                Pour x dans le tableau de note
                Faire le calcul de la moyenne en fonction de la longueur du tableau
                Afficher nos résultats
                '''
                for x in TbNote:
                    s = s + x
                    result = s / len(TbNote)
                affichage = affichage + f'Note moyenne du jeu {j["nameGame"]}: {result}/5 <br>'
                print(affichage)


    return (affichage)


@app.route("/moyenne")
def moyenne():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    body = [""]
    mydb = client["fillingGame"]
    mycol = mydb["mean"]

    test = mycol.find(([
        {"$project": {"idGame": 1}},
        {"$group": {"idNote": "$mean"},
         "count": {"$avg ": "idNote"}}
    ]))

    print(list(test))
    return


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
