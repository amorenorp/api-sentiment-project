# Api Sentiment Project
## ***Shout Park Analysis.***
------------




### **_Objetivo:_**

El objetivo de este proyecto es crear una Api la cual nos proporcionará información sobre los 3 primeros episodios de la temporada 10 de `Shout Park`.   
También realizar un _sentiment analysis_ sobre los dialogos de los protagonistas.

>Los datos sobre estos episodios, obtenidos de `Kaggle`, [aquí](https://www.kaggle.com/tovarischsukhov/southparklines), han pasado por un proceso de `data cleanning` y más tarde añadidos a una base de datos en `MongoDB`. 

Comprobamos el funcionamiento de la API en un Jupyter Notebook en el que realizammos llamadas utilizando `requests`.



### **_Proceso:_**
Empezamos descargando el `.csv` y el data cleanning.
Creamos en `MongoDB Compass` una base de datos y 2 biliotecas: _characters_ y _dialogues_.

A partir de ahora usaremos *`Visual Code`*:

Creamos un `.py` para crear la conexion con MongoDB, y dos más (_getdata y postdata_) con las funciones que usaremos en `api.py`. 

En este último se encuentran los _endpoints_.

**Para finalizar** tenemos dos `.ipynb`, uno de ellos para realizar llamadas a la API y otro con el analisis de los dialogos. 


___
#### _**Referencias y bibliotecas**_:
- https://www.kaggle.com
- https://seaborn.pydata.org
- https://pandas.pydata.org
- https://matplotlib.org
- https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
- https://www.diegocalvo.es/analisis-de-discursos-con-wordcloud-en-python/
