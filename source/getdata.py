from mongoConnec.mongoConnection import db, coll_character,coll_dialogue

def all_characters():
    """
    Obtenemos todos los personajes de la colección Characters.
    """

    return coll_character.find({},{"Character":1, "_id":0})

"""
def one_character(name):

    return coll_character.find({"Character": name})
"""


def all_phrases():

    """
    Obtenemos todas las frases de la colección Dialogue.

    """

    return coll_dialogue.find({}, {"Character":1, "Episode":1, "Line":1, "_id":0})


def get_phrases(name, episode):

    """
    Obtenemos las frases de un personajes y capitulo a elegir.

    """

    return coll_dialogue.find({"Character":name, "Episode": episode}, {"_id":0, "Season":0})
















    
    




