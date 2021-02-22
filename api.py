import flask
from flask import Flask, request
from pymongo import MongoClient

import source.getdata as get
import source.postdata as post

from bson.json_util import dumps



app = Flask("shout_park")

@app.route("/")
def hola():
    return """<!DOCTYPE html>
<html lang="es">
<center>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SouthPark API </title>
    </head>

    <body style="background-color:#bda195;">
        <h1>Bienvenido a mi nueva API sobre SouthPark!</h1>
        <h2>Puedes encontrar informacion sobre los tres primeros capitulos utilizando los siguientes endpoints:</h2>
        <h3>GET Endpoints:  </h3>
        <h4>/users</h4>
        <h4>/messages</h4>
        <h4>/episode/name</h4>
        <h3>POST Endpoints:  </h3>
        <h4> /addepisode/episode</h4>
        <h4> /add/episodecharacter </h4>
        <h4> /add/episode/message/character</h4>


        <img src="https://www.revistacambio.com.mx/wp-content/uploads/2019/11/B9721169814Z.1_20191007183636_000GALEKV3R6.1-0-768x432.jpg" />
    </body>

</html>
"""



### GET 

@app.route("/users")
def user():
    users = get.all_characters()

    return dumps(users)


@app.route("/messages")
def messages():
    mess = get.all_phrases()

    return dumps(mess)

@app.route("/<episode>/<name>")
def chat_user(episode, name):
    #episode = str(episode)
    #name= str(name)

    chat = get.get_phrases(name, episode)

    return dumps(chat)




### POST

@app.route("/addepisode/<episode>")
def add_episode(episode):
    post.new_episode(episode)

    return  f"Episode {episode} added"



@app.route("/add/<episode>/<character>")
def add_character(episode,character):
    x = post.new_char(character,episode)

    return x


@app.route("/add/<episode>/<message>/<character>")
def add_mess(episode, message, character):

    y = post.new_dialogue(character, message, episode)

    return y




app.run(debug= True)