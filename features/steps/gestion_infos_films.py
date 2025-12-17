from behave import given, when, then
from film import Film
from categorie import Categorie

@given('un nouveau film est créé')
def step_impl_creation(context):
    # On instancie un film vierge (valeurs par défaut)
    context.mon_film = Film()

@when('je définis la catégorie sur "{nom_categorie}"')
def step_impl_categorie(context, nom_categorie):
    # Création de l'objet Categorie
    ma_categorie = Categorie()
    ma_categorie.set_nom(nom_categorie)
    
    # Association avec le film
    context.mon_film.set_categorie(ma_categorie)

@when('je modifie la durée à {duree:d} minutes et la date de sortie à "{date_sortie}"')
def step_impl_modification(context, duree, date_sortie):
    # Mise à jour des attributs via les setters
    # Note : {duree:d} assure que behave convertit automatiquement le chiffre en int
    context.mon_film.set_duree(duree)
    context.mon_film.set_date_sortie(date_sortie)

@then('la description finale doit être "{description_attendue}"')
def step_impl_verification(context, description_attendue):
    # Appel de la méthode description() et comparaison
    resultat_reel = context.mon_film.description()
    
    assert resultat_reel == description_attendue, \
        f"Erreur description: \nAttendu: {description_attendue}\nObtenu : {resultat_reel}"