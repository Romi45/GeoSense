# Python built-in Packages
import csv
import json
import random
from datetime import datetime
from inspect import currentframe
# Package MySQL Connector >> pip install mysql-connector-python
import mysql.connector as mysql


class TTNtoBD():

    def __init__(self):
    
        self.connexion_bd = self.ouvrir_connexion_bd()
        self.date_string = None

    
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

### Il y a trois fonctions ajouter car les types de valeur peuvent ne pas être les mêmes !


    def ajouter_pH(self, idMesure, dateMesure, valeur, idCapteur):
        try:
            cursor = self.connexion_bd.cursor()
            cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
                        + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
            self.connexion_bd.commit()
        except Exception as e:
            print("MySQL [INSERTION ERROR]")
            print(e)
        
        
    def ajouter_humidite(self, idMesure, dateMesure, valeur, idCapteur):
        try:
            cursor = self.connexion_bd.cursor()
            cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
                        + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
            self.connexion_bd.commit()
        except Exception as e:
            print("MySQL [INSERTION ERROR]")
            print(e)
    
    def extract_date(self, date_string):
    # Truncate or round the fractional seconds to 6 digits
        self.date_string = date_string
        truncated_date_string = date_string[:26]  # Truncate to remove extra digits
        rounded_date_string = f"{date_string[:26]}Z"  # Round and append 'Z' for UTC time
        datetime_obj = datetime.strptime(rounded_date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_only = datetime_obj.date()
        return str(date_only)






    
    def ajouter_gps(connexion_bd, idMesure, dateMesure, valeur, idCapteur):
        try:
            cursor = connexion_bd.cursor()
            cursor.execute("INSERT INTO Mesure (idMesure, dateMesure, valeur, idCapteur)"
                        + "VALUES (%s,%s,%s,%s)", [idMesure, dateMesure, valeur, idCapteur])
            connexion_bd.commit()
        except Exception as e:
            print("MySQL [INSERTION ERROR]")
            print(e)
# Inutile pour le moment !
        


# fermer_connexion_bd(connexion_bd)




