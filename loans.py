def emprunter_livre(livre):
    if livre["disponible"]:
        livre["disponible"] = False
        return True
    return False

def rendre_livre(livre):
    livre["disponible"] = True
