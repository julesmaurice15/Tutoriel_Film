from film import Categorie, Film

# 1. Création de la catégorie
ma_categorie = Categorie()
ma_categorie.set_nom("Science-Fiction")

# 2. Création du film
mon_film = Film()
mon_film.set_duree(120)
mon_film.set_date_sortie("2023/10/25")
mon_film.set_categorie(ma_categorie)

# 3. Affichage de la description
print(mon_film.description())
# Résultat: Je suis un film de catégorie Science-Fiction et de durée 120 sorti en 2023/10/25