from flask import Flask
import pymongo as pm

app = Flask(__name__)

'''
 editor() affiche la page la liste de tout les éditeurs enregistré dans la base de données

:parameter
none

:return 
body: string
'''


# methods=["GET","PATCH"]
@app.route("/")
def editor():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    body = f'Éditeur enregistré :<br><br>'
    for i in client.fillingGame.editor.find():
        print(i["nameEditor"])
        body = body + f'id : {i["idEditor"]}, name : {i["nameEditor"]} <br>'
    return body


'''
 addEditor() ajoute un éditeur dans la base de donnés

:parameter
    id : int
    name : string
    commentaire : string

:return
    string

'''


@app.route("/editeur/add")
def addEditor():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    id = input("idantifiant de l'éditeur :")
    name = input("Nom de l'éditeur :")
    commentaire = input("Un commantaire :")
    client.fillingGame.editor.insert_one({"idEditor": id, "nameEditor": name, "commentaire": commentaire})
    return f'Editeur {name} ajouter sous l identifiant {id}'


'''
suppEditor() supprime un éditeur de la base de données en fonction de l'id entrer par l'utilisateur
 
:parameter
    id : int
    
:return
    string
'''


@app.route("/editeur/supp")
def suppEditor():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    id = input('Id  à supprimé :')
    client.filling.editor.delete_one({"idEditor": id})
    return f"L'éditeur d'id {id} a bien été supprimé"


'''
    modifyEditor() modifie un Editeur en passant par sont id
    
    :parameter
        idEditor: int
        newName: string
        newCommentaire: string
    
    :return
        string
'''


@app.route("/editeur/modifier")
def modifyEditor():
    db_url = f'mongodb+srv://groupe7:root@projetpython.uo5ak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = pm.MongoClient(db_url)
    idEditor = input('Id à modifier :')
    newName = input('Nouveau de l editeur :')
    newCom= input('Nouveau Commentaire ')
    if newName != "":
        client.fillingGame.editor.update_one({"idEditor": idEditor}, {"$set": {"nameEditor": newName}})

    client.fillingGame.editor.update_one({"idEditor": idEditor}, {"$set": {"commentaire": newCom}})

    return f'Éditeur {idEditor} à été modifier'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
