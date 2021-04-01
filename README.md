# Challenge_bik

PRESENTATION DU JEU DE DONNEES

L'objectif de notre étude est de réaliser une prédiction sur les données récoltées par des compteurs vélos déployé par Totem Montpellier à Albert 1er afin de compter le passage de vélo dans cette zone.

Le jeu de données est constitué de 1110 lignes (dynamiques) et de 6 variables: Date et heure de comptage, Vélos depuis le 1er janvier 2020,Vélos ce jour, Remarque, Unammed.

Les variables qui serviront principalement à mener à bien notre analyse sont le nombre de Vélos ce jour (notre variable cible), la date et heure du comptage.

Le prétraitement des données à été réalisé en plusieurs étapes à savoir:
Nous avons tout d'abord supprimé les valeurs manquantes grâce à la fonction dropna(). Nous avons opté pour la suppression des valeurs manquantes et non leur remplacement car elles ne correspondent qu’à 3% des données présentes dans notre jeu de données et ne possèdent donc pas de réel impact sur les résultats. Nous avons avons par la suite visualiser les nouvelles données sans les valeurs maquantes pour voir s'il n'y a pas des valaurs abérantes. Nous avons donc constaté que pendant les deux confinement il y avait une baisse considérable du nombre de vélo qui passe. Outre l'année 2020 est néttement différente de l'année 2021. Nous avons donc décidé d'ignorer toutes les données relever en 2020. Par ailleure, l'activité des jours de la semaine est également différente de celle des week-end, et nous cherchons à prédire le nombre de comtage sur une période de minuit vers 09 heures 00 munites, le Vendredi. A cet effet, nous avons décidé d'ignorer également les comtages des week-end ainsi ceux qui sont hors des heures entre 08 heueres et 10 heuers.

Nous avons donc par la suite travaillé sur un jeu de données de 48 lignes et une colonne.

