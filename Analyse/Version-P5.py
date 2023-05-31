def Temperature_quanti_a_qualitatif(n):
    label = ''
	if n < 15 :
        label = 'Faibles températures'
	elif 15 <= n <= 25 :
    	label = 'Températures modérées'
	else :
    	label = 'Températures élevées'
    print(label)



def selectionner_selon_température(connexion_bd, id_champ):
	cursor = connexion_bd.cursor()
    
	cursor.execute(
    	"SELECT c.idChamp, mc.idClimat, temperature "
      + "FROM Champ ch, MeteoChamp mc, Meteo me"
      + "WHERE mc.idClimat = me.idClimat"
      + "AND mc.idChamp = ch.idChamp"
      + "GROUP BY c.idChamp"
    	)
    
	for (c.idChamp, mc.idClimat, temperature) in cursor:
    	if c.idChamp == id_champ :
            modèle_qualitatif = Temperature_quanti_a_qualitatif(valeur)
            print(modèle_qualitatif)

            
            
            
def Precipitations_quanti_a_qualitatif(n):
    label = ''
	if n < 50 :
        label = 'Faibles précipitations'
	elif 50 <= n <= 150 :
    	label = 'Précipitations modérées'
	else :
    	label = 'Précipitations élevées'
    print(label)



def selectionner_selon_précipitations(connexion_bd, id_champ):
	cursor = connexion_bd.cursor()
    
	cursor.execute(
    	"SELECT c.idChamp, mc.idClimat, précipitationMensuelle"
      + "FROM Champ ch, MeteoChamp mc, Meteo me"
      + "WHERE mc.idClimat = me.idClimat"
      + "AND mc.idChamp = ch.idChamp"
      + "GROUP BY c.idChamp"
    	)
    
	for (c.idChamp, mc.idClimat, precipitationMensuelle) in cursor:
    	if c.idChamp == id_champ :
            modèle_qualitatif = Precipitations_quanti_a_qualitatif(valeur)
            print(modèle_qualitatif)

            
            
            
            
            
            
def Ensoleillement_quanti_a_qualitatif(n):
    label = ''
	if n < 4 :
        label = 'Ensoleillement limité'
	elif 4 <= n <= 7 :
    	label = 'Ensoleillement modéré'
	else :
    	label = 'Ensoleillement élevé'
    print(label)



def selectionner_selon_ensoleillement(connexion_bd, id_champ):
	cursor = connexion_bd.cursor()
    
	cursor.execute(
    	"SELECT c.idChamp, mc.idClimat, ensoleillementMensuel"
      + "FROM Champ ch, MeteoChamp mc, Meteo me"
      + "WHERE mc.idClimat = me.idClimat"
      + "AND mc.idChamp = ch.idChamp"
      + "GROUP BY c.idChamp"
    	)
    
	for (c.idChamp, mc.idClimat, ensoleillementMensuel) in cursor:
    	if c.idChamp == id_champ :
            modèle_qualitatif = Ensoleillement_quanti_a_qualitatif(valeur)
            print(modèle_qualitatif)

            
            
            
            
            
            
            
def Hum_quanti_a_qualitatif(n):
    label = ''
	if n <= 550.0 :
        label = 'Très sec'
	elif 550.0 < n <= 1100.0 :
    	label = 'Sec à peu humide'
	elif 1100.0 < n <= 1660.0 :
    	label = 'Peu humide à humide'
	else :
    	label = 'Humide à très humide'
    print(label)
    


def selectionner_selon_humidité(connexion_bd, id_champ):
	cursor = connexion_bd.cursor()
    
	cursor.execute(
    	"SELECT c.idChamp, idMesure, dateMesure, valeur, m.idCapteur
      + "FROM Mesure m, Capteur c, TypeCapteur t, Baton b, ZoneChamp z, Localisation l, Champ ch
      + "WHERE m.idCapteur = c.idCapteur"
      + "AND b.idBaton = l.idBaton"
      + "AND z.idChamp = c.idChamp"
      + "AND c.idTypeCapteur = t.idTypeCapteur"
      + "AND grandeur = “Humidité”"
      + "GROUP BY c.idChamp"
    	)
    
	for (c.idChamp, idMesure, dateMesure, valeur, m.idCapteur) in cursor:
    	if c.idChamp == id_champ :
            modèle_qualitatif = Hum_quanti_a_qualitatif(valeur)
            print(modèle_qualitatif)

            
           
          
          
          
          
          
          
          
          
          
def pH_quanti_a_qualitatif(n):
    label = ''
	if n <= 5.0 :
        label = 'Très acide'
	elif 5.0 < n <= 6.0 :
    	label = 'Acide à légèrement acide'
	elif 6.0 < n <= 7.0 :
    	label = 'Neutre'
    elif 7.0 < n <= 8.0 :
    	label = 'Légèrement alcalin'
	else :
    	label = 'Alcalin'
    return label



def selectionner_selon_pH(connexion_bd, id_champ):
	cursor = connexion_bd.cursor()
    
	cursor.execute(
    	"SELECT c.idChamp, idMesure, dateMesure, valeur, m.idCapteur
      + "FROM Mesure m, Capteur c, TypeCapteur t, Baton b, ZoneChamp z, Localisation l, Champ ch
      + "WHERE m.idCapteur = c.idCapteur"
      + "AND b.idBaton = l.idBaton"
      + "AND z.idChamp = c.idChamp"
      + "AND c.idTypeCapteur = t.idTypeCapteur"
      + "AND grandeur = “pH”"
      + "GROUP BY c.idChamp"
    	)
    
	for (c.idChamp, idMesure, dateMesure, valeur, m.idCapteur) in cursor:
    	if c.idChamp == id_champ :
            modèle_qualitatif = pH_quanti_a_qualitatif(valeur)
            print(modèle_qualitatif)
