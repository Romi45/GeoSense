def Temperature_quanti_a_qualitatif(n):
    """
    
Intervalle de température (°C) | Espèces de plantes comestibles
---------------------------- | ----------------------------
0°C - 5°C                    | Chou frisé, Épinard, Cresson, Carotte, Navet, Persil, Mâche, Roquette, Bettes à carde, Poireau, Radis, Chou-rave
5°C - 10°C                   | Chou de Bruxelles, Chou-fleur, Céleri-rave, Oignon, Chou pommé, Pois, Laitue, Ciboulette, Coriandre, Salsifis, Moutarde, Endive
10°C - 15°C                  | Pomme de terre, Haricot vert, Fenouil, Chou-rave, Chou frisé, Courgette, Poivron, Aubergine, Tomate, Basilic, Betterave, Persil
15°C - 20°C                  | Courge, Maïs doux, Concombre, Melon, Pastèque, Pois, Haricot mange-tout, Laitue, Épinard, Radis, Cresson, Céleri
20°C - 25°C                  | Tomate, Piment, Aubergine, Poivron, Courgette, Haricot vert, Concombre, Basilic, Persil, Melon, Pastèque, Haricot mange-tout
25°C - 30°C                  | Poivron, Piment, Aubergine, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs doux
30°C - 35°C                  | Piment, Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs doux
35°C - 40°C                  | Piment, Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs doux  
    
    """
    label = ''
    if n < 15 :
        label = 'Faibles températures'
    elif 15 <= n <= 25 :
        	label = 'Températures modérées'
    else :
        	label = 'Températures élevées'
    return label

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
    """
    
Intervalle de précipitations (mm/an) | Espèces de plantes comestibles
----------------------------------- | ----------------------------
0 - 500                             | Cactus de fruits, Romarin, Thym, Sarriette, Origan, Lavande, Sauge, Estragon, Marjolaine, Ciboulette, Persil, Coriandre
500 - 1000                          | Carotte, Radis, Chou-rave, Betterave, Fève, Épinard, Haricot vert, Oignon, Laitue, Fenouil, Roquette, Mâche
1000 - 1500                         | Pomme de terre, Tomate, Poivron, Aubergine, Courgette, Céleri, Concombre, Pois, Chou-fleur, Brocoli, Laitue, Épinard
1500 - 2000                         | Melon, Pastèque, Courge, Maïs, Riz, Canne à sucre, Patate douce, Haricot rouge, Poireau, Banane, Arachide, Taro
2000 - 2500                         | Piment, Aubergine, Courgette, Poivron, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Haricot mange-tout
2500 - 3000                         | Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs, Haricot mange-tout
3000 - 3500                         | Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs, Haricot mange-tout
3500 - 4000                         | Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs, Haricot mange-tout

    """
    label = ''
    if n < 50 :
        label = 'Faibles précipitations'
    elif 50 <= n <= 150 :
        	label = 'Précipitations modérées'
    else :
        	label = 'Précipitations élevées'
    return label

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
    """
    
Intervalle d'ensoleillement (heures/jour) | Espèces de plantes comestibles
---------------------------------------- | ----------------------------
0 - 2                                   | Épinard, Laitue, Mâche, Roquette, Chou frisé, Persil, Cresson, Bettes à carde, Coriandre, Ciboulette, Radis, Céleri
2 - 4                                   | Carotte, Betterave, Oignon, Poireau, Chou-rave, Navet, Fenouil, Moutarde, Salsifis, Chou-fleur, Endive, Chou de Bruxelles
4 - 6                                   | Tomate, Poivron, Aubergine, Courgette, Haricot vert, Concombre, Maïs doux, Potiron, Courge, Basilic, Persil, Piment
6 - 8                                   | Pomme de terre, Haricot mange-tout, Céleri-rave, Chou pommé, Brocoli, Chou-fleur, Pois, Haricot rouge, Patate douce, Melon, Pastèque, Haricot nain
8 - 10                                  | Haricot vert, Concombre, Courgette, Tomate, Aubergine, Poivron, Courge, Melon, Pastèque, Maïs doux, Pois, Basilic
10 - 12                                 | Courgette, Aubergine, Poivron, Haricot vert, Concombre, Tomate, Basilic, Melon, Pastèque, Maïs doux, Piment, Haricot mange-tout
12 - 14                                 | Aubergine, Poivron, Courgette, Haricot vert, Concombre, Tomate, Basilic, Persil, Melon, Pastèque, Maïs doux, Haricot mange-tout

    """
    
    label = ''
    if n < 4 :
        label = 'Ensoleillement limité'
    elif 4 <= n <= 7 :
        	label = 'Ensoleillement modéré'
    else :
        	label = 'Ensoleillement élevé'
    return label

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
    """
    0V à 2.2V en range et 0.76V à 2.12V écart sec-humide (/!\ évolution logarithmique)

| Niveau d'eau | Espèces de plantes |
| ------------ | ----------------- |
| Très faible  | Cactus de fruits (Opuntia spp.), Romarin (Rosmarinus officinalis), Thym (Thymus spp.), Sarriette (Satureja spp.), Origan (Origanum spp.), Lavande (Lavandula spp.), Sauge (Salvia officinalis), Estragon (Artemisia dracunculus), Marjolaine (Origanum majorana), Ciboulette (Allium schoenoprasum), Persil (Petroselinum crispum), Coriandre (Coriandrum sativum) |
| Faible       | Carotte (Daucus carota), Radis (Raphanus sativus), Chou-rave (Brassica oleracea var. gongylodes), Betterave (Beta vulgaris), Fève (Vicia faba), Épinard (Spinacia oleracea), Haricot vert (Phaseolus vulgaris), Oignon (Allium cepa), Laitue (Lactuca sativa), Fenouil (Foeniculum vulgare), Mâche (Valerianella locusta), Roquette (Eruca vesicaria) |
| Moyen        | Tomate (Solanum lycopersicum), Poivron (Capsicum annuum), Courgette (Cucurbita pepo), Aubergine (Solanum melongena), Pomme de terre (Solanum tuberosum), Céleri (Apium graveolens), Concombre (Cucumis sativus), Pois (Pisum sativum), Brocoli (Brassica oleracea var. italica), Chou-fleur (Brassica oleracea var. botrytis), Piment (Capsicum spp.), Épinard (Spinacia oleracea) |
| Élevé        | Melon (Cucumis melo), Pastèque (Citrullus lanatus), Courge (Cucurbita spp.), Maïs (Zea mays), Riz (Oryza sativa), Canne à sucre (Saccharum officinarum), Taro (Colocasia esculenta), Banane (Musa spp.), Patate douce (Ipomoea batatas), Haricot rouge (Phaseolus vulgaris), Poireau (Allium ampeloprasum), Arachide (Arachis hypogaea) |

    """
    label = ''
    if n <= 550.0 :
        label = 'Très sec'
    elif 550.0 < n <= 1100.0 :
        	label = 'Sec à peu humide'
    elif 1100.0 < n <= 1660.0 :
        	label = 'Peu humide à humide'
    else :
        	label = 'Humide à très humide'
    return label
    
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
    """
    https://www.astucesaupotager.com/le-taux-dacidite-ph-au-potager/
    https://www.consoglobe.com/ph-du-sol-cg
    https://www.lunion.fr/art/23524/article/2017-03-31/le-bon-ph-pour-chaque-plante
    (ci-dessus trois sites associant pH avec plantations)

pH du sol	Plantations adaptées
4.5 - 5.0	Myrtille, Ail des ours, Fraisier, Renoncule, Glaïeul, Lys, Muguet, Groseille, Cassis, Framboise, Sureau, Cerise
5.0 - 5.5	Bleuet, Érable japonais, Chèvrefeuille, Jacinthe, Lis, Orchidée, Pervenche, Mûre, Framboise, Sureau, Cassis, Groseille
5.5 - 6.0	Chou-fleur, Laitue, Épinard, Fraisier, Ail, Brocoli, Ciboulette, Oignon, Persil, Radis, Thym, Persil frisé
6.0 - 6.5	Carotte, Concombre, Basilic, Persil, Céleri, Courgette, Pois, Romarin, Sauge, Tomate, Haricot vert, Poivron
6.5 - 7.0	Courgette, Betterave, Poivron, Asperge, Cerfeuil, Laitue romaine, Melon, Poireau, Rose, Sauge, Tomate, Haricot vert
7.0 - 7.5	Tomate, Aubergine, Pomme de terre, Rose, Artichaut, Chrysanthème, Dahlia, Pivoine, Souci, Tournesol, Courge, Pois
7.5 - 8.0	Asperge, Céleri, Citrouille, Menthe, Oseille, Patate douce, Poire, Persil frisé, Chou-rave, Chou de Bruxelles, Cresson, Haricot mange-tout
8.0 - 8.5	Maïs doux, Tournesol, Capucine, Lavande, Menthe poivrée, Oignon vert, Piment, Sariette, Verveine, Maïs à popcorn, Aubergine japonaise, Navet
8.5 - 9.0	Melon, Persil, Aneth, Carvi, Coriandre, Fenouil, Moutarde, Poivron de Cayenne, Radis, Ciboule, Épinard, Chou-rave
    (ci-dessus données de chatgpt avec des espèces comestibles uniquement)      
    
    """
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





