from mongoConnec.mongoConnection import db, coll_character,coll_dialogue

def new_episode(episode):

    """
    Añadimos un capitulo a la base de datos Dialogue.

    """

    dic_epi = {
        "Episode": episode
    }
    
    return coll_dialogue.insert_one(dic_epi)




def new_char(name, episode):

    """
    Añadimos un personaje y un episode a la coleccion Character.

    """

    dic_new = {
        "Character":name,
        "Episode": episode
        }


    check_user = list(coll_character.find({"Character": name , "Episode":episode}))


    if len(check_user)>0:
        return """<!DOCTYPE html>
<html lang="es">
<center>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SouthPark API </title>
    </head>

    <body style="background-color:#e3d7d1;">
        <h1> Character already exists </h1>
        
        <img src="https://static.onecms.io/wp-content/uploads/sites/6/2013/01/south-park-gun.jpg" />
    </body>

</html>
"""
    
    else: 
        coll_character.insert_one(dic_new)
        return """<!DOCTYPE html>
<html lang="es">
<center>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SouthPark API </title>
    </head>

    <body style="background-color:#e3d7d1;">
        <h1>Character added! </h1>
        
        <img src="https://www.cinemascomics.com/wp-content/uploads/2020/10/south-park-origen-coronavirus-covid-19-960x720.jpg" />
    </body>

</html>
"""
 





def new_dialogue(name, phrase, episode, season = "10"):

    """
    Añadimos personaje, episodio y frase.

    """

    dic_newdialogue= {
        "Season": season,
        "Episode": episode,
        "Character": name,
        "Line": phrase

    }

    check_mess = list(coll_dialogue.find({"Character": name, "Episode":episode, "Line":phrase}))

    if len(check_mess)>0:
        return  """<!DOCTYPE html>
<html lang="es">
<center>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SouthPark API </title>
    </head>

    <body style="background-color:#e3d7d1;">
        <h1> Dialogue already exists </h1>
        
        <img src="https://i.redd.it/xosux9ox86601.jpg" />
    </body>

</html>
"""




    
    else: 
        coll_dialogue.insert_one(dic_newdialogue)
        return """<!DOCTYPE html>
<html lang="es">
<center>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SouthPark API </title>
    </head>

    <body style="background-color:#e3d7d1;">
        <h1> Dialogue added!</h1>
        
        <img src="https://m.media-amazon.com/images/M/MV5BZjI2MGRlZDMtNDNlMi00YTVjLTg5MjItZDM5Y2RjYjI3NGMyXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_CR0,45,480,270_AL_UX477_CR0,0,477,268_AL_.jpg" />
    </body>

</html>
"""

    


