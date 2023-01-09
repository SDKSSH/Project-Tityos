from pick import pick
import modules.ComponentsLoader as cl
import modules.NewGame as ng

if __name__ == "__main__":
    cl.launch()

    #STARTING SCREEN
    options, selected = pick(['Nouvelle partie', 'Charger une partie'], "Bienvenu(e) sur Tityos !\n", indicator="=> ")
    if selected == 0:
        ng.launch()
    else:
        print("Les sauvegardes sont réservé lors de l'achat du jeu !\nMerci de votre compréhension !")