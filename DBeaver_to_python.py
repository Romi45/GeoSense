# Python built-in Packages
import csv
import json
import random
from datetime import datetime
from inspect import currentframe
# Package MySQL Connector >> pip install mysql-connector-python
import mysql.connector as mysql


class BD_to_Python():

    def __init__(self):
        self.connexion_bd = self.ouvrir_connexion_bd()

    

    def ouvrir_connexion_bd(self):
        print("")
        print("***********************")
        print("** Connexion à la BD **")
        print("***********************")

    
        try:
            self.connexion_bd = mysql.connect(
                    host="fimi-bd-srv1.insa-lyon.fr",
                    port=3306,
                    user="G223_B",      # à compléter
                    password="G223_B",  # à compléter
                    database="G223_B_BD3"   # à compléter
                )
        except Exception as e:
            if type(e) == NameError and str(e).startswith("name 'mysql'"):
                print("[ERROR] MySQL: Driver 'mysql' not installed ? (Python Exception: " + str(e) + ")")
                print("[ERROR] MySQL:" + " Package MySQL Connector should be installed [Terminal >> pip install mysql-connector-python ]" + " and imported in the script [import mysql.connector as mysql]")
            else:
                print("[ERROR] MySQL: " + str(e))

        if self.connexion_bd is not None:
            print("=> Connexion établie...")
        else:
            print("=> Connexion échouée...")

        return self.connexion_bd

    def fermer_connexion_bd(self):
        print("")
        print("Fermeture de la Connexion à la BD")

        if self.connexion_bd is not None:
            try:
                self.connexion_bd.close()
                print("=> Connexion fermée...")
            except Exception as e:
                print("[ERROR] MySQL: "+str(e))
        else:
            print("=> pas de Connexion ouverte")





    def extraire_mesure(self):
        cursor = self.connexion_bd.cursor()
    
        cursor.execute(
            "SELECT m.idMesure, m.dateMesure, m.valeur, m.idCapteur "
            + " FROM Mesure m, Capteur c "
            + " WHERE m.idCapteur = c.idCapteur; "
        )
        res_dict = {}
        for (idMesure, dateMesure, valeur, idCapteur) in cursor: 
            res_dict[idCapteur] = valeur
        return res_dict
            




    





