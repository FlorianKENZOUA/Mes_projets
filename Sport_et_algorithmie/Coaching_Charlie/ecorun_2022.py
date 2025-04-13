# Imports nécessaires au programme :
import pandas as pd # si besoin, entrer pip install pandas dans le terminal
import gpxpy # si besoin, entrer pip install gpxpy dans le terminal
import math
import matplotlib.pyplot as plt
import numpy as np
import cotation

# Création des listes qui vont stocker les data de la montre :
liste_lon = []
liste_lat = []
liste_ele = []
liste_dis = []
liste_time = []
liste_temps_montre = []
liste_vitesse_moy = []
liste_allure_moy = []
liste_hr = []
liste_hr_moy = []
liste_cad = []
liste_cad_moy = []
liste_x = []
liste_y = []

# Charger le fichier GPX de 2022 :
with open("ecorun_2022_copie.gpx", "r") as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Parcourir les points pour extraire les données des extensions :
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            # Informations de base :
            liste_lon.append(point.longitude)
            liste_lat.append(point.latitude)
            liste_ele.append(point.elevation)
            liste_time.append(point.time)

            # Extensions :
            if point.extensions:
                for extension in point.extensions:
                    # Rechercher les données spécifiques dans les extensions :
                    hr = extension.find("{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}hr")
                    cad = extension.find("{http://www.garmin.com/xmlschemas/TrackPointExtension/v1}cad")

                    liste_hr.append(int(hr.text))
                    liste_cad.append(int(cad.text))

# Calcul et mise en forme du chrono de Charlie :
heure_depart_charlie = liste_time[0].time()
heure_arrivee_charlie = liste_time[-1].time()
temps_secondes_charlie = (liste_time[-1].hour*3600 + liste_time[-1].minute*60 + liste_time[-1].second) - ((liste_time[0].hour*3600 + liste_time[0].minute*60 + liste_time[0].second))
heures_d = temps_secondes_charlie/3600
heures = int(heures_d)
minutes_100 = (heures_d - heures)*100
minutes_d = (60*minutes_100)/100
minutes = int(minutes_d)
secondes_100 = (minutes_d - minutes)*100
secondes = int((60*secondes_100)/100)
temps_charlie = str(heures) + ':' + str(minutes) + ':' + str(secondes) + ':0'

# Définitions de variables :
nb_pts = len(liste_lat)
compteur = 0
fc_moy = 0
cad_moy = 0
distance_course = 0
distance_t = 0
delta_t = 0
denivele_pos = 0
denivele_neg = 0
r_Terre = 6371   

# Traitement des data liées à la cadence et mise en ppm :
for i in range(nb_pts) :
    lat = math.radians(liste_lat[i])
    lon = math.radians(liste_lon[i])
    x = r_Terre*math.cos(lat)*math.cos(lon)
    liste_x.append(x)
    y = r_Terre*math.cos(lat)*math.sin(lon)
    liste_y.append(y)
    cad = 2*int(liste_cad[i])
    liste_cad[i] = cad

# Traitement des données temporelles :
for i in range(1,nb_pts) :
    temps_pts_seconde = (liste_time[i].hour*3600 + liste_time[i].minute*60 + liste_time[i].second) - ((liste_time[i-1].hour*3600 + liste_time[i-1].minute*60 + liste_time[i-1].second))
    liste_temps_montre.append(temps_pts_seconde)

# Calculs de la distance, dénivelés; vitesses, allures, fc et cad moyennes par km :
liste_temps_montre.append(0)
liste_dis.append(0)
for i in range(1, nb_pts) :
    # Distance :
    distance = math.sqrt((liste_x[i] - liste_x[i-1])**2 + (liste_y[i] - liste_y[i-1])**2)
    distance_course += distance
    distance_t += distance
    liste_dis.append(distance_course)

    # Dénivelés :
    epsilon = liste_ele[i]-liste_ele[i-1]
    if epsilon > 0 :
        denivele_pos += epsilon
    else :
        denivele_neg += epsilon
    
    # Vitesses, allures, fc et cad moyennes par km :
    compteur += 1
    fc_moy += int(liste_hr[i])
    cad_moy += int(liste_cad[i])
    delta_t += liste_temps_montre[i]

    # km par km :
    if distance_t >= 1 :
        delta_t = delta_t/3600
        vitesse = distance_t/delta_t
        liste_vitesse_moy.append(vitesse)
        allure_d = 60/vitesse
        dec_part, int_part = math.modf(allure_d)
        allure = int_part + dec_part*0.60
        liste_allure_moy.append(allure)
        distance_t = 0
        delta_t = 0
        fc_moy = fc_moy/compteur
        liste_hr_moy.append(fc_moy)
        fc_moy = 0
        cad_moy = cad_moy/compteur
        liste_cad_moy.append(cad_moy)
        cad_moy = 0
        compteur = 0
    
    # Les derniers mètres :
    if i == nb_pts-1 :
        delta_t = delta_t/3600
        vitesse = distance_t/delta_t
        liste_vitesse_moy.append(vitesse)
        allure_d = 60/vitesse
        dec_part, int_part = math.modf(allure_d)
        allure = int_part + dec_part*0.60
        liste_allure_moy.append(allure)
        distance_t = 0
        delta_t = 0
        fc_moy = fc_moy/compteur
        liste_hr_moy.append(fc_moy)
        fc_moy = 0
        cad_moy = cad_moy/compteur
        liste_cad_moy.append(cad_moy)
        cad_moy = 0
        compteur = 0

# Charger le fichier Excel dans un DataFrame :
df = pd.read_excel('ecorun_2022_scrape.xlsx')

# Création des listes qui vont stocker les data du scrape :
liste_rang = []
liste_coureurs = []
liste_sexe = []
liste_cat = []
liste_rang_cat = []
liste_club = []
liste_temps = []
liste_pace = []
liste_cotes = []
liste_cotes_M = []
liste_rang_M = []
liste_cotes_F = []
liste_rang_F = []
liste_cotes_cat = []
liste_rang_cat = []

# Itérer sur les lignes du DataFrame avec `iterrows()` :
for index, row in df.iterrows():
    dict = row.to_dict()
    valeurs = list(dict.values())
    liste_rang.append(valeurs[2])
    liste_coureurs.append(valeurs[3])
    liste_sexe.append(valeurs[4])
    liste_cat.append(valeurs[5])
    liste_rang_cat.append(valeurs[6])
    liste_club.append(valeurs[7])
    liste_temps.append(valeurs[8])
    liste_pace.append(valeurs[9])

def conversion_en_secondes(temps) :
        '''Retourne le temps d'une course en secondes
        
        Argument(s) :
            temps (str) : temps lors d'une course
        
        Resultat(s) :
            temps_secondes (int) : temps converti en secondes
        '''
        temps_secondes = 0
        liste_dimensions = temps.split(':')
        taille = len(liste_dimensions)
        for i in range(taille) :
            if i == 0 :
                heures = int(liste_dimensions[0]) * 3600
                temps_secondes += heures
            if i == 1 :
                minutes = int(liste_dimensions[1]) * 60
                temps_secondes += minutes
            if i == 2 :
                secondes = int(liste_dimensions[2])
                temps_secondes += secondes
        return temps_secondes

def affichage_temps(temps_secondes) :
        '''Retourne le temps de la course sur format h:min:s:cs
        
        Argument(s) :
            temps_secondes (int) : temps du coureur en secondes
        
        Résultat(s) :
            temps (str) : temps du coureur
        '''
        heures_d = temps_secondes/3600
        heures = int(heures_d)
        minutes_100 = (heures_d - heures)*100
        minutes_d = (60*minutes_100)/100
        minutes = int(minutes_d)
        secondes_100 = (minutes_d - minutes)*100
        secondes = int((60*secondes_100)/100)
        temps = str(heures) + ':' + str(minutes) + ':' + str(secondes) + ':00 '
        return temps

# Création de variables :
taille = len(liste_rang)
temps_moy = 0

# Calculs des cotes, conversion en secondes du temps de chaque coureur :
for i in range(taille) :
    temps_coureur = liste_temps[i]+':00'
    temps_s = conversion_en_secondes(temps_coureur)
    cote = cotation.calculs_cote(liste_sexe[i], distance_course, denivele_pos, temps_coureur)
    liste_cotes.append(cote)
    temps_moy += temps_s

    if liste_sexe[i] == 'F.' :
        liste_cotes_F.append(cote)
        liste_rang_F.append(liste_rang[i])
    else :
        liste_cotes_M.append(cote)
        liste_rang_M.append(liste_rang[i])
        if liste_cat[i] == 'SE' :
            liste_cotes_cat.append(cote)
            liste_rang_cat.append(liste_rang[i])

# Création de variables :
cote_charlie = cotation.calculs_cote('M.', distance_course, denivele_pos, temps_charlie)
rang_charlie = '28'
temps_moy = temps_moy/taille
temps_moy = affichage_temps(temps_moy)

# Input pour simplifier la prise en main du programme par l'utilisateur :
souhait_1 = input("Voulez-vous afficher le dashboard de l'édition 2022 ? (oui/non) : ")

# Affichage des différents graphiques :
if souhait_1 == 'oui' :
    def affiche() :
        '''Affiche les graphiques.
        
        Résultat(s) :
            None (bool) : rien
        '''
        L = []
        for i in range(285):
            L.append(cote_charlie)

        # Graphique des allures :
        plt.figure('Allures de la course en 2022')
        x = np.arange(len(liste_allure_moy))
        plt.bar(x, liste_allure_moy, width=1, edgecolor='black')
        plt.xticks(x, ['1', '2', '3', '4', '5', '5,200'])
        plt.xlabel('km')
        plt.ylabel('Allure (min/km)')
        plt.title('Allures de Charlie km après km')

        # Graphique de la cadence :
        fig, ax1 = plt.subplots()
        plt.title('Profil de la course 2022 et Cadence')
        ax2 = ax1.twinx()
        ax1.plot(liste_dis, liste_cad, color='green',label='Fréquence cardiaque', markersize=1)
        ax2.plot(liste_dis, liste_ele, color='blue',label='Profil', markersize=4)
        ax1.set_xlabel('Distance (km)')
        ax1.set_ylabel('Cadence (ppm)')
        ax2.set_ylabel('Altitude (m)')

        # Graphique de la fc :
        fig, ax1 = plt.subplots()
        plt.title('Profil de la course 2022 et HR')
        ax2 = ax1.twinx()
        ax1.plot(liste_dis, liste_hr, color='red',label='Fréquence cardiaque', markersize=1)
        ax2.plot(liste_dis, liste_ele, color='blue',label='Profil', markersize=4)
        ax1.set_xlabel('Distance (km)')
        ax1.set_ylabel('Fréquence cardiaque (bpm)')
        ax2.set_ylabel('Altitude (m)')

        # Graphique de la physionomie :
        plt.figure('Physionomie de la course en 2022')
        plt.title('Physionomie de la course en 2022')
        plt.plot(liste_rang_M, liste_cotes_M, 'o', color='blue', label = 'Hommes', markersize=2)
        legende_charlie = f"Performance de Charlie avec \n une cote de {cote_charlie} (rang {rang_charlie})"
        plt.plot(rang_charlie, cote_charlie, 'o', color='red', label = legende_charlie, markersize=4)
        plt.plot(liste_rang_F, liste_cotes_F, 'o', color='pink', label = 'Femmes', markersize=2)
        plt.plot(liste_rang, L, '--', color='red', markersize=2)
        #plt.plot(liste_rang_cat, liste_cotes_cat, 'yellow', label = 'Catégorie')
        plt.legend()
        plt.xlabel('Rang allant de 1 (tout à gauche) à 285 (tout à droite)')
        plt.xlim(-5, 290)
        plt.ylabel('Cotation sur 1000')
        plt.show(block=False)
        
        return None

    affiche()

#input()
