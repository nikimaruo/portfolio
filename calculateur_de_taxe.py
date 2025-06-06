       def get_prix_ht():
    while True:
        try:
            prix_ht = float(input("Entre le prix hors taxes : "))
            return prix_ht
            break
        except ValueError:
            print('Il faut entrer un nombre!')
def get_taux_tva():
    taux_tva = 0.18
    return taux_tva
def calculer_montant_taxe(prix_ht, taux_tva):
    montant_taxe = prix_ht * taux_tva
    return montant_taxe
def calculer_prix_ttc(prix_ht, montant_taxe):
    prix_ttc = prix_ht + montant_taxe
    return prix_ttc
def afficher_resultats(prix_ht, montant_taxe, prix_ttc):
    print('Les Resultats sont :\n')
    print(f'Prix Hors Taxe : {prix_ht}\n')
    print(f'Montant Taxe : {montant_taxe}\n')
    print(f'Prix Taxe Tva Compris : {prix_ttc}\n')
    
if __name__ == "__main__":
    prix_ht = get_prix_ht()
    taux_tva = get_taux_tva()
    montant_taxe = calculer_montant_taxe(prix_ht, taux_tva)
    prix_ttc = calculer_prix_ttc(prix_ht, montant_taxe)
    afficher_resultats(prix_ht, montant_taxe, prix_ttc)
