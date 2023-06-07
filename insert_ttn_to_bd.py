# Python built-in Packages
import csv
import json
import random
from datetime import datetime
from inspect import currentframe
# Package MySQL Connector >> pip install mysql-connector-python
import mysql.connector as mysql


def ouvrir_connexion_bd():
    print("")
    print("***********************")
    print("** Connexion à la BD **")
    print("***********************")

    connexion_bd = None
    try:
        connexion_bd = mysql.connect(
                host="fimi-bd-srv1.insa-lyon.fr",
                port=3306,
                user="G223_B",      # à compléter
                password="G223_B",  # à compléter
                database="G223_B_BD3"   # à compléter
            )
    except Exception as e:
        if type(e) == NameError and str(e).startswith("name 'mysql'"):
            print("[ERROR] MySQL: Driver 'mysql' not installed ? (Python Exception: " + str(e) + ")")
            print("[ERROR] MySQL:" +
                  " Package MySQL Connector should be installed [Terminal >> pip install mysql-connector-python ]" +
                  " and imported in the script [import mysql.connector as mysql]")
        else:
            print("[ERROR] MySQL: " + str(e))

    if connexion_bd is not None:
        print("=> Connexion établie...")
    else:
        print("=> Connexion échouée...")

    return connexion_bd

def fermer_connexion_bd(connexion_bd):
    print("")
    print("Fermeture de la Connexion à la BD")

    if connexion_bd is not None:
        try:
            connexion_bd.close()
            print("=> Connexion fermée...")
        except Exception as e:
            print("[ERROR] MySQL: "+str(e))
    else:
        print("=> pas de Connexion ouverte")

### Il y a trois fonctions ajouter car les types de valeur peuvent ne pas être les mêmes !


def ajouter_pH(connexion_bd, idMesure, dateMesure, valeur, idCapteur):
    try:
        cursor = connexion_bd.cursor()
        cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
                       + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
        connexion_bd.commit()
    except Exception as e:
        print("MySQL [INSERTION ERROR]")
        print(e)
        
        
def ajouter_humidite(connexion_bd, idMesure, dateMesure, valeur, idCapteur):
    try:
        cursor = connexion_bd.cursor()
        cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
                       + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
        connexion_bd.commit()
    except Exception as e:
        print("MySQL [INSERTION ERROR]")
        print(e)


# def ajouter_gps(connexion_bd, idMesure, dateMesure, valeur, idCapteur):
#     try:
#         cursor = connexion_bd.cursor()
#         cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
#                        + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
#         connexion_bd.commit()
#     except Exception as e:
#         print("MySQL [INSERTION ERROR]")
#         print(e)
# Inutile pour le moment !
        
        
# connexion_bd = ouvrir_connexion_bd()

# fermer_connexion_bd(connexion_bd)
