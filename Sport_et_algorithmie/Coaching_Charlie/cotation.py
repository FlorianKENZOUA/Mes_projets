## Imports et définition des variables globales : 

import tqdm # si besoin, entrer pip install tqdm dans le terminal

wr_100m_h = "00:00:09:58" # record du monde 100m Usain Bolt 2009
wr_200m_h = "00:00:19:19" # record du monde 200m Usain Bolt 2009
wr_400m_h = "00:00:43:03" # record du monde 400m  Wayde van Niekerk 2016
wr_800m_h = "00:01:40:91" # record du monde 800m David Rudisha 2012 
wr_1000m_h = "00:02:11:96" # record du monde 1000m Noah Ngeny 1999
wr_1500m_h = "00:03:26:00" # record du monde 1500m Hicham El Guerrouj 1998
wr_1600m_h = "00:03:43:13" # record du monde 1600m Hicham El Guerrouj 1999
wr_2000m_h = "00:04:43:13" # record du monde 2000m Jakob Ingebrigtsen 2023
wr_3000m_h = "00:07:17:55" # record du monde 3000m Jakob Ingebrigtsen 2024
wr_5000m_h = "00:12:35:36" # record du monde 5000m Joshua Cheptegei 2020
wr_10000m_h = "00:26:11:00" # record du monde 10000m Joshua Cheptegei 2024
wr_15km_h = "00:40:42:00" # record du monde 15km Jacob Kiplimo 2024
wr_semi_marathon_h = "00:57:30:00" # record du monde semi-marathon Kibiwott Kandie 2024
wr_30km_h = "01:27:13:00" # record du monde 30km Eliud Kipchoge 2016
wr_38km_h = "01:52:00:00" # record de la Skyrhune en km d'efforts Jan Margarit Solé 2021
wr_marathon_h = "02:00:35:00" # record du monde marathon Kelvin Kiptum 2023
wr_53km_h = "02:25:34:00" # record de la Sierre-Zinal en km d'efforts Kilian Jornet 2024
wr_67km_h = "03:21:04:00" # record du marathon du Mont-Blanc en km d'efforts Eric Lacroix 2003
wr_72km_h = "03:36:40:00" # record de Zegama-Aizkorri en km d'efforts Kilian Jornet 2022
wr_100km_h = "06:05:35:00" # record du monde 100km Aleksandr Sorokin 2023

wr_100m_f = "00:00:10:49" # record du monde 100m Florence Griffith-Joyner 1988
wr_200m_f = "00:00:21:34" # record du monde 200m Florence Griffith-Joyner 1988
wr_400m_f = "00:00:47:60" # record du monde 400m Marita Koch 1985
wr_800m_f = "00:01:53:28" # record du monde 800m Jarmila Kratochvílová 1983
wr_1000m_f = "00:02:28:98" # record du monde 1000m Svetlana Masterkova 1996
wr_1500m_f = "00:03:49:04" # record du monde 1500m Faith Kipyegon 2024
wr_1600m_f = "00:04:07:64" # record du monde 1600m Faith Kipyegon 2023
wr_2000m_f = "00:05:19:70" # record du monde 2000m Jessica Hull 2024
wr_3000m_f = "00:08:16:60" # record du monde 3000m Wang Junxia 1993
wr_5000m_f = "00:14:00:21" # record du monde 5000m Gudaf Tsegay 2023
wr_10000m_f = "00:28:54:14" # record du monde 10000m Beatrice Chebet 2024
wr_15km_f = "00:44:20:00" # record du monde 15km Letesenbet Gidey 2019
wr_semi_marathon_f = "01:02:52:00" # record du monde semi-marathon Letesenbet Gidey 2021
wr_30km_f = "01:36:05:00" # record du monde 30km Mary Keitany 2017
wr_38km_f = "02:04:39:00" # record de la Skyrhune en km d'efforts Nienke Brinkman 2021
wr_marathon_f = "02:09:56:00" # record du marathon Ruth Chepngetich 2024
wr_50km_f = "02:59:54:00" # record du monde 50km Desiree Linden 2021
wr_67km_f = "03:53:33:00" # record du marathon du Mont-Blanc en km d'efforts Elisa Desco 2015
wr_72km_f = "04:16:43:00" # record de Zegama-Aizkorri en km d'efforts Nienke Brinkman 2022
wr_100km_f = "06:33:11:00" # record du monde 100km Tomoe Abe 2000

liste_distances = [100, 200, 400, 800, 1000, 1500, 1600, 2000, 3000, 5000, 
10000, 15000, 21100, 30000, 38000, 42195, 53000, 67000, 72000, 100000] # à compléter

liste_temps_h = [wr_100m_h, wr_200m_h, wr_400m_h, wr_800m_h, wr_1000m_h, wr_1500m_h, wr_1600m_h,
wr_2000m_h, wr_3000m_h, wr_5000m_h, wr_10000m_h, wr_15km_h, wr_semi_marathon_h, wr_30km_h, wr_38km_h,
wr_marathon_h, wr_53km_h, wr_67km_h, wr_72km_h, wr_100km_h] # à compléter

liste_temps_f = [wr_100m_f, wr_200m_f, wr_400m_f, wr_800m_f, wr_1000m_f, wr_1500m_f, wr_1600m_f,
wr_2000m_f, wr_3000m_f, wr_5000m_f, wr_10000m_f, wr_15km_f, wr_semi_marathon_f, wr_30km_f, wr_38km_f,
wr_marathon_f, wr_50km_f, wr_67km_f, wr_72km_f, wr_100km_f] # à compléter

## Fonctions et traitement des données :

def calculs_cote(sexe, distance_plat, denivele_pos, temps_str) :

    distance_theorique = distance_plat*1000 + denivele_pos*10

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

    temps_theorique = conversion_en_secondes(temps_str)

    def process_list(distances, temps) :
        '''Retourne la version de la liste temps avec des valeurs converties en secondes
        
        Argument(s) :
            distances (list) : liste des distances
            temps (list) : liste des temps
        
        Résultat(s) :
            liste_temps_secondes (list) : liste des temps en secondes
        '''
        liste_t = []
        taille1 = len(distances)
        taille2 = len(temps)
        if taille1 == taille2 :
            taille = taille1
        else :
            return("Les listes de la data base ne sont pas de même taille.")
        for i in range(taille) :
            temps_secondes = conversion_en_secondes(temps[i])
            liste_t.append(temps_secondes)
        return liste_t

    if sexe == 'M.' :
        liste_temps_secondes = process_list(liste_distances, liste_temps_h)
    if sexe == 'F.' :
        liste_temps_secondes = process_list(liste_distances, liste_temps_f)

    def recherche(liste_x, liste_y, x_valeur) :
        '''Retourne les coordonnées (interpolation) de la performance de cotation 1000 correspondant à la distance théorique
        
        Argument(s) :
            liste_x (list) : liste des distances
            liste_y (list) : liste des temps
        
        Résultat(s) :
            (x_inter, y_inter) (tuple) : coorconnées de la performance de cotation 1000
        '''
        taille = len(liste_x)
        if x_valeur < liste_x[0] or x_valeur > liste_x[-1] :
            return('valeur de distance non conforme')
        if x_valeur in liste_x :
            indice = liste_x.index(x_valeur)
            x = x_valeur
            y = liste_y[indice]
            return (x, y)
        else :
            for i in range(1, taille) :
                if liste_x[i-1] < x_valeur < liste_x[i] :
                    x_inter = x_valeur
                    y_inter = int (liste_y[i-1] + (x_inter - liste_x[i-1])*((liste_y[i] - liste_y[i-1])/(liste_x[i] - liste_x[i-1])))
            return (x_inter, y_inter)

    coordonnees_utilisateur = (distance_theorique, temps_theorique)
    coordonnees_cotation_max = recherche(liste_distances, liste_temps_secondes, distance_theorique)

    def cotation(c1, c2) :
        '''Retourne la cotation finale
        
        Argument(s) :
            c1 (tuple) : coordonnées de l'utilisateur
            c2 (tuple) : coordonnées de référence
        
        Résultat(s) :
            cotation_finale (int) : cotation évaluée par l'algorithme
        '''
        quotient_cotation = c1[1]/c2[1]
        cote = 1000/quotient_cotation
        cote_finale = int(cote)
        return cote_finale
    
    cote_coureur = cotation(coordonnees_utilisateur, coordonnees_cotation_max)

    return cote_coureur
