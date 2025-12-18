from film import Film
from categorie import Categorie
from realisateur import Realisateur

categorie1 = Categorie()
categorie1.set_nom("Action")


kill_bill = Film()
kill_bill.set_duree(111)
kill_bill.set_date_sortie("2003/10/29")
kill_bill.set_categorie(categorie1)

pulp_fiction = Film()
pulp_fiction.set_duree(144)
pulp_fiction.set_date_sortie("1994/01/01")
pulp_fiction.set_categorie(categorie1)

realisateur1 = Realisateur("Quentin Tarantino")
realisateur1.ajouter_film(kill_bill)
realisateur1.ajouter_film(pulp_fiction)

print(realisateur1.afficher_stats())
print(kill_bill.description())
print(pulp_fiction.description())
