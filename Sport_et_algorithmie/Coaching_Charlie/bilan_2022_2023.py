# Imports nécessaires au programme :
import math
import ecorun_2022 as e2022
import ecorun_2023 as e2023

# Récuperer les données qui servent à l'élaboration du bilan :
liste_hr_2022 = e2022.liste_hr_moy
liste_hr_2023 = e2023.liste_hr_moy
liste_cad_2022 = e2022.liste_cad_moy
liste_cad_2023 = e2023.liste_cad_moy
liste_vitesse_2022 = e2022.liste_vitesse_moy
liste_vitesse_2023 = e2023.liste_vitesse_moy
liste_allure_2022 = e2022.liste_allure_moy
liste_allure_2023 = e2023.liste_allure_moy
distance_2022 = round(e2022.distance_course, 3)
distance_2023 = round(e2023.distance_course, 3)
dpos_2022 = round(e2022.denivele_pos, 0)
dpos_2023 = round(e2023.denivele_pos, 0)
dneg_2022 = e2022.denivele_neg
dneg_2023 = e2023.denivele_neg
nb_coureurs_2022 = e2022.taille
nb_coureurs_2023 = e2023.taille
liste_temps_2022 = e2022.liste_temps
liste_temps_2023 = e2023.liste_temps
temps_charlie_2022 = e2022.temps_charlie
temps_charlie_2023 = e2023.temps_charlie
temps_moy_2022 = e2022.temps_moy
temps_moy_2023 = e2023.temps_moy
liste_rang_2022 = e2022.liste_rang
liste_rang_2023 = e2023.liste_rang
rang_charlie_2022 = e2022.rang_charlie
rang_charlie_2023 = e2023.rang_charlie
liste_cat_2022 = e2022.liste_rang_cat
liste_cat_2023 = e2023.liste_rang_cat
cat_charlie_2022 = '9'
cat_charlie_2023 = '5'
liste_cotes_2022 = e2022.liste_cotes
liste_cotes_2023 = e2023.liste_cotes
cote_charlie_2022 = e2022.cote_charlie
cote_charlie_2023 = e2023.cote_charlie

# Création de nos variables globales :
ecartt_vitesse_2022 = 0
ecartt_vitesse_2023 = 0
ecartt_hr_2022 = 0
ecartt_hr_2023 = 0
ecartt_cad_2022 = 0
ecartt_cad_2023 = 0
moy_vitesse_2022 = 0
moy_vitesse_2023 = 0
moy_hr_2022 = 0
moy_hr_2023 = 0
moy_cad_2022 = 0
moy_cad_2023 = 0
n = len(liste_vitesse_2022)
n_2022 = len(liste_cotes_2022)
n_2023 = len(liste_cotes_2023)
cote_moy_2022 = 0
cote_moy_2023 = 0

# Calculs des moyennes pour la formule de l'écart-type :
for i in range(n) :
    moy_vitesse_2022 += liste_vitesse_2022[i]
    moy_vitesse_2023 += liste_vitesse_2023[i]
    moy_hr_2022 += liste_hr_2022[i]
    moy_hr_2023 += liste_hr_2023[i]
    moy_cad_2022 += liste_cad_2022[i]
    moy_cad_2023 += liste_cad_2023[i]
    liste_allure_2022[i] = round(liste_allure_2022[i], 2)
    liste_allure_2023[i] = round(liste_allure_2023[i], 2)
moy_vitesse_2022 = moy_vitesse_2022/n
moy_vitesse_2023 = moy_vitesse_2023/n
moy_hr_2022 = moy_hr_2022/n
moy_hr_2023 = moy_hr_2023/n
moy_cad_2022 = moy_cad_2022/n
moy_cad_2023 = moy_cad_2023/n

# Calculs et normalisation de l'écart-type :
for i in range(n) :
    ecartt_vitesse_2022 += (liste_vitesse_2022[i]-moy_vitesse_2022)**2
    ecartt_vitesse_2023 += (liste_vitesse_2023[i]-moy_vitesse_2023)**2
    ecartt_hr_2022 += (liste_hr_2022[i]-moy_hr_2022)**2
    ecartt_hr_2023 += (liste_hr_2023[i]-moy_hr_2023)**2
    ecartt_cad_2022 += (liste_cad_2022[i]-moy_cad_2022)**2
    ecartt_cad_2023 += (liste_cad_2023[i]-moy_cad_2023)**2
ecartt_vitesse_2022 = math.sqrt((1/n)*ecartt_vitesse_2022)*100/moy_vitesse_2022
ecartt_vitesse_2023 = math.sqrt((1/n)*ecartt_vitesse_2023)*100/moy_vitesse_2023
ecartt_hr_2022 = math.sqrt((1/n)*ecartt_hr_2022)*100/moy_hr_2022
ecartt_hr_2023 = math.sqrt((1/n)*ecartt_hr_2023)*100/moy_hr_2023
ecartt_cad_2022 = math.sqrt((1/n)*ecartt_cad_2022)*100/moy_cad_2022
ecartt_cad_2023 = math.sqrt((1/n)*ecartt_cad_2023)*100/moy_cad_2023

# Calculs des cotes moyennes :
for i in range(n_2022) :
    cote_moy_2022 += liste_cotes_2022[i]
for i in range(n_2023) :
    cote_moy_2023 += liste_cotes_2023[i]
cote_moy_2022 = int(cote_moy_2022/n_2022)
cote_moy_2023 = int(cote_moy_2023/n_2023)

# Classements en pourcentages :
top_2022 = round(int(rang_charlie_2022)*100/n_2022, 1)
top_2023 = round(int(rang_charlie_2023)*100/n_2022, 1)

# Correction des données pour mise en forme dans le bilan :
moy_vitesse_2022 = round(moy_vitesse_2022, 2)
moy_vitesse_2023 = round(moy_vitesse_2023, 2)
ecartt_vitesse_2022 = round(ecartt_vitesse_2022, 1)
ecartt_vitesse_2023 = round(ecartt_vitesse_2023, 1)
moy_hr_2022 = int(moy_hr_2022)
moy_hr_2023 = int(moy_hr_2023)
ecartt_hr_2022 = round(ecartt_hr_2022, 2)
ecartt_hr_2023 = round(ecartt_hr_2023, 2)
moy_cad_2022 = int(moy_cad_2022)
moy_cad_2023 = int(moy_cad_2023)
ecartt_cad_2022 = round(ecartt_cad_2022, 2)
ecartt_cad_2023 = round(ecartt_cad_2023, 2)

# Input pour simplifier la prise en main du programme par l'utilisateur :
souhait_3 = input("Voulez-vous afficher dans le terminal le bilan chiffré des deux éditions ? (oui/non) : ")

# Création du Bilan chiffré :
if souhait_3 == 'oui' :
    print('\nBilan statistique éditions 2022 et 2023 :')
    print(f"\t - distance : {distance_2022}km (2022), {distance_2023}km (2023) soit {int(round((distance_2022-distance_2023), 3)*1000)}m de moins en 2023")
    print(f"\t - dénivelé positif : {int(dpos_2022)}m (2022), {int(dpos_2023)}m (2023) soit {int(dpos_2023-dpos_2022)}m de plus en 2023")
    print(f"\t - dénivelé négatif : {abs(int(dneg_2022))}m (2022), {abs(int(dneg_2023))}m (2023)")
    print(f"\t - températue : 5°C (2022) infoclimat.fr, 19°C (2023) soit 14°C de plus en 2023")
    print(f"\t - vent : pas de donnée")
    print(f"\t - temps moyen de la course : {temps_moy_2022} (2022), {temps_moy_2023} (2023) soit 27s de plus en 2023")
    print(f"\t - cote moyenne : {cote_moy_2022}/1000 (2022), {cote_moy_2023}/1000 (2023) soit 2 de moins en 2023")
    print(f"\t - nombre de coureurs : {nb_coureurs_2022} (2022), {nb_coureurs_2023} (2023) soit 119 de plus en 2023")

    print('\nBilan des performances personnelles éditions 2022 et 2023 :')
    print(f"\t - temps : {temps_charlie_2022} (2022), {temps_charlie_2023} (2023) soit 1min10 de mieux en 2023")
    print(f"\t - classement : {rang_charlie_2022}/{nb_coureurs_2022} top {top_2022}% (2022), {rang_charlie_2023}/{nb_coureurs_2023} top {top_2023}% (2023)")
    print(f"\t - classement catégorie : {cat_charlie_2022} (2022), {cat_charlie_2023} (2023)")
    print(f"\t - cote et % coureur mondial sur distance d'effort : {cote_charlie_2022}/1000 top {(1000-cote_charlie_2022)/10}% (2022), {cote_charlie_2023}/1000 top {(1000-cote_charlie_2023)/10}% (2023)")
    print(f"\t - vitesse moyenne : {moy_vitesse_2022}km/h (2022), {moy_vitesse_2023}km/h (2023) soit {round(moy_vitesse_2023-moy_vitesse_2022, 2)}km/h plus vite en 2023")
    print(f"\t - variabilité de la vitesse : {ecartt_vitesse_2022}% (2022), {ecartt_vitesse_2023}% (2023) soit une vitesse {ecartt_vitesse_2022-ecartt_vitesse_2023}% plus régulière en 2023")
    print(f"\t - fréquence cardiaque moyenne : {moy_hr_2022}bpm (2022), {moy_hr_2023}bpm (2023) soit {moy_hr_2022-moy_hr_2023}bpm de moins en 2023")
    print(f"\t - dispersion de la fréquence cardiaque : {ecartt_hr_2022}% (2022), {ecartt_hr_2023}% (2023) soit une hausse de {round(ecartt_hr_2023-ecartt_hr_2022, 2)}% en 2023")
    print(f"\t - cadence de pas moyenne : {moy_cad_2022}ppm (2022), {moy_cad_2023}ppm (2023)")
    print(f"\t - variabilité de la cadence : {ecartt_cad_2022}% (2022), {ecartt_cad_2023}% (2023) soit une baisse de {round(ecartt_cad_2022-ecartt_cad_2023, 2)}% en 2023")
    
    print(f"\nBilan km après km (allure en min/km|FC en bpm) :")
    print(f"\t - km 1 : {liste_allure_2022[0]}|{int(liste_hr_2022[0])} (2022), {liste_allure_2023[0]}|{int(liste_hr_2023[0])} (2023)")
    print(f"\t - km 2 : {liste_allure_2022[1]}|{int(liste_hr_2022[1])} (2022), {liste_allure_2023[1]}|{int(liste_hr_2023[1])} (2023)")
    print(f"\t - km 3 : {liste_allure_2022[2]}|{int(liste_hr_2022[2])} (2022), {liste_allure_2023[2]}|{int(liste_hr_2023[2])} (2023)")
    print(f"\t - km 4 : {liste_allure_2022[3]}|{int(liste_hr_2022[3])} (2022), {liste_allure_2023[3]}|{int(liste_hr_2023[3])} (2023)")
    print(f"\t - km 5 : {liste_allure_2022[4]}|{int(liste_hr_2022[4])} (2022), {liste_allure_2023[4]}|{int(liste_hr_2023[4])} (2023)")
    print(f"\t - 200 derniers mètres : {liste_allure_2022[5]}|{int(liste_hr_2022[5])} (2022), {liste_allure_2023[5]}|{int(liste_hr_2023[5])} (2023)")
