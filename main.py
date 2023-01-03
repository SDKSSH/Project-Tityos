from pick import pick
import modules.ComponentsLoader as cl
import modules.NewGame as ng

if __name__ == "__main__":
    cl.launch()

    #STARTING SCREEN
    selected = pick(['Nouvelle partie', 'Charger une partie', 'Options'], "Bienvenu(e) sur Tityos !\n", indicator="=> ")
    if selected[0][1] == 0:
        ng.launch()