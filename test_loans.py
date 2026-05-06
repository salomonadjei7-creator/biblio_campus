from books import ajouter_livre
from loans import emprunter_livre, rendre_livre

livre = ajouter_livre("Python avancé", "Collaborateur C")

print("Avant emprunt :", livre)

if emprunter_livre(livre):
    print("Livre emprunté :", livre)
else:
    print("Impossible d'emprunter :", livre)

rendre_livre(livre)
print("Après retour :", livre)
