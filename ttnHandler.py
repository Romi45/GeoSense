# Requirement: package paho-mqtt // Terminal >> pip install paho-mqtt
from ttn_client import TTNClient
from insert_ttn_to_bd import TTNtoBD
import datetime
import math
from datetime import datetime


# Classe TTNDataHandler qui doit avoir une méthode on_ttn_message


# Example usage
#input_date = '2023-06-09T08:17:11.904501326Z'
#output_date = extract_date(input_date)
#print(output_date)

class TTNDataHandler:

    # Constructeur : attributs et paramètres à adapter aux besoins de votre projet (connexion BD, etc.)
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2


    # Méthode appelée lorsque le client TTN reçoit un message
    def on_ttn_message(self, message):
        print(f"[TTNDataHandler] Données reçues par le Handler avec les paramètres '{self.parameter1}', '{self.parameter2}'")
        self.my_method()
        device_id = message['device_id']
        message_date = message['date']
        message_json = message['json']
        # print(message_date)
        aff_message_date = message_date.strftime("%d/%m/%Y %H:%M:%S (%Z%z)")
        print(f"[TTNDataHandler] {aff_message_date}: Message de {device_id} => " + str(message_json))

    # Méthode(s) à adapter aux besoins de votre projet (requêtes SQL, etc.)
    def my_method(self):
        TTNClient.storage_retrieve_messages()


        print(f"[TTNDataHandler] Méthode du TTNDataHandler... ['{self.parameter1}', '{self.parameter2}']")







print("** Début du script **")

# ** Information de connexion à adapter à votre projet **
ttn_application_id = "projet-223b"
ttn_api_key_secret = "NNSXS.KK2BHBT7MRPRISSDYDEDUH3OP224ELDQW6A2VSI.F7T6FMQ7MIIHQZNTQMED6U4LMI5VTU4ELSKLHK3Q7L27OUPUKDIA"

ttn_data_handler = TTNDataHandler('P2i-2 Test Value', 1742)

ttn = TTNClient(
    "eu1.cloud.thethings.network",
    ttn_application_id,
    ttn_api_key_secret,
    ttn_data_handler
)

# print()
# print("** Envoi d'un message ???")
# ttn.webhook_send_downlink('cmu-p32', 'node7')
#
# exit()


#en continue jusqu'a KeyInterrupt
print()
TTNtoBD = TTNtoBD()
minutes = 5
print(f"** Récupération des messages stockés (depuis {minutes} minutes)")
message = ttn.storage_retrieve_messages(hours=0, minutes=minutes)   # en temps continu
message_content = message['uplink_message']['decoded_payload']  #those are to be uncommented

#message_content = {'CoordX': 45.750000 , 'CoordY': 4.850000, 'V_HumOut': 981, 'V_pHOut': 1335, 'len': 12}

print(message_content)
reception_time = message['received_at']    #Just need to uncomment this
#reception_time = '2023-06-09T14:22:33.411956962Z'


print(reception_time)
reception_time_formatted = TTNtoBD.extract_date(date_string = reception_time)
#truncated_date_string = reception_time[:26]  # Truncate to remove extra digits
#rounded_date_string = f"{reception_time[:26]}Z"  # Round and append 'Z' for UTC time
#datetime_obj = datetime.datetime.strptime(rounded_date_string, '%Y-%m-%dT%H:%M:%S.%fZ')
#reception_time_formatted = datetime_obj.date()
print(reception_time_formatted)

#-------On assigne les identifiants des mesures----#
now = datetime.now()
now = str(now).replace(":", "").replace(" ", "").replace("-", "")
print(now)
now =int(float(now))


idMesure1 = f'PH{now}'
idMesure2 = f'HU{now}'
idMesure3 = f'CX{now}'
idMesure4 = f'CY{now}'


#--------On vide la table de mesure pour y insérer les nouvelles mesures




#-----------Ajout des 3 mesures l'une apres l'autre----------

#------pH-------------------------------------
try:
    pH = round(message_content['V_pHOut'],2)
    pH = 14*pH/3000
    print(pH)
    TTNtoBD.ajouter_pH(idMesure= idMesure1, dateMesure = reception_time_formatted, valeur = pH, idCapteur='C1')
    print('Data successfully inserted')
    #time.sleep(100)
except Exception as e:
    print(f"Erreur lors de l'ajout des données : {e}")
#--------------------Humidite---------------------------  
try:
     
    humidite = round(message_content['V_HumOut'],2)
    humidite = humidite/1000
    humidite = ((math.exp(humidite) + 0.97)/10)*100
    TTNtoBD.ajouter_humidite(idMesure = idMesure2, dateMesure = reception_time_formatted, valeur = humidite, idCapteur='C2')
    print('Data successfully inserted')
    #time.sleep(100)
except Exception as e:
    print(f"Erreur lors de l'ajout des données : {e}")


#-------------------------GPS COORD X ----------------------------

try:
     
    COORDX = round(message_content['CoordX'],6)
    print(COORDX)
    TTNtoBD.ajouter_humidite(idMesure = idMesure3, dateMesure = reception_time_formatted, valeur =COORDX, idCapteur='C3')
    print('Data successfully inserted')
    #time.sleep(100)
except Exception as e:
    print(f"Erreur lors de l'ajout des données : {e}")
    pass
#-----------------------GPS COORD Y--------------------------------------

try:
     
    COORDY = round(message_content['CoordY'],6)
    print(COORDY)
    TTNtoBD.ajouter_humidite(idMesure = idMesure4, dateMesure = reception_time_formatted, valeur = COORDY, idCapteur='C4')
    print('Data successfully inserted')
    #time.sleep(100)
except Exception as e:
    print(f"Erreur lors de l'ajout des données : {e}")
    pass



print()
print("** Connexion à MQTT @ TTN")
ttn.mqtt_connect()  # Connect to TTN

# ttn.mqtt_register_device("node16")
# ttn.mqtt_register_device("node8")
ttn.mqtt_register_devices(['eui-a8610a3032338711', 'node7']) # en temps réel
#ttn.on_ttn_message()

try:
    print("[Attente au clavier]")
    input("Appuyer 2 fois sur Entrée pour arrêter le script\n\n")
except KeyboardInterrupt as ex:
    print("[Attente interrompue]")

print("Déconnexion de MQTT @ TTN")
ttn.mqtt_disconnect()

print("** Fin du script **")