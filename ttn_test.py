# Requirement: package paho-mqtt // Terminal >> pip install paho-mqtt
from ttn_client import TTNClient


# Classe TTNDataHandler qui doit avoir une méthode on_ttn_message
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

print()
print("** Récupération des messages stockés (depuis 5 minutes)")
ttn.storage_retrieve_messages(hours=0, minutes=5) # en temps continu

print()
print("** Connexion à MQTT @ TTN")
ttn.mqtt_connect()  # Connect to TTN

# ttn.mqtt_register_device("node16")
# ttn.mqtt_register_device("node8")
ttn.mqtt_register_devices(['eui-a8610a3032338711', 'node7']) # en temps réel

try:
    print("[Attente au clavier]")
    input("Appuyer 2 fois sur Entrée pour arrêter le script\n\n")
except KeyboardInterrupt as ex:
    print("[Attente interrompue]")

print("Déconnexion de MQTT @ TTN")
ttn.mqtt_disconnect()

print("** Fin du script **")
