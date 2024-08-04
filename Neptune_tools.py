import os
import shutil
import time
import sys
import requests
from colorama import init, Fore
import subprocess

# Initialise colorama pour la coloration de la sortie dans la console
init(autoreset=True)


def run_update():
    result = subprocess.run([sys.executable, 'maj.py'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Erreur lors de la mise à jour : {result.stderr}")
        return False
    print(result.stdout)
    return "Mise à jour nécessaire." in result.stdout

def restart_script():
    """Redémarre le script principal."""
    print("Redémarrage du script principal...")
    os.execv(sys.executable, ['python'] + sys.argv)

# Exécutez le script de mise à jour
needs_update = run_update()

# Redémarrez le script principal si nécessaire
if needs_update:
    restart_script()
else:
    # Continuez avec le reste de votre code
    print("Début du script principal...")
    # Ajoutez le reste de votre code ici


    


# Fonction pour nettoyer le répertoire temporaire de l'utilisateur
def clear_temp_directory(directory_path):
    errors_encountered = False

    try:
        # Parcourt tous les fichiers et dossiers dans le répertoire temporaire
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                # Supprime les fichiers ou les dossiers
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path) 
            except Exception as e:
                # Gère les erreurs rencontrées lors de la suppression
                print(Fore.RED + f"Erreur lors de la suppression de {file_path}: {e}")
                errors_encountered = True

        if not errors_encountered:
            print(Fore.GREEN + "Tous les fichiers temporaires ont été supprimés avec succès.")
        else:
            print(Fore.YELLOW + "Certaines erreurs se sont produites lors de la suppression des fichiers temporaires.")

    except Exception as e:
        print(Fore.RED + f"Erreur lors de l'accès au répertoire ! : {e}")

    # Indique à l'utilisateur que Solara doit être réinstallé
    print(Fore.GREEN + "Veuillez réinstaller Solara.")
    input(Fore.LIGHTRED_EX + "\nAppuyez sur Enter pour fermer.")

# Fonction pour effacer la console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour afficher un message de chargement en grand avec animation de points
def display_large_loading_message():
    loading_message = r"""
  ______   __                                                                                    __     
 /      \ /  |                                                                                  /  |    
/$$$$$$  |$$ |____    ______    ______    ______    ______   _____  ____    ______   _______   _$$ |_   
$$ |  $$/ $$      \  /      \  /      \  /      \  /      \ /     \/    \  /      \ /       \ / $$   |  
$$ |      $$$$$$$  | $$$$$$  |/$$$
                                        /  \__$$ |                                                      
                                        $$    $$/                                                       
                                         $$$$$$/  
  """
    
    # Obtenez la taille de la console
    columns, rows = os.get_terminal_size()

    # Divisez le message en lignes
    lines = loading_message.strip().split('\n')

    # Calculez la position verticale pour centrer le texte
    vertical_position = (rows - len(lines)) // 2
    horizontal_position = (columns - max(len(line) for line in lines)) // 2

    # Créez le message pour la console
    message = '\n' * vertical_position + '\n'.join(
        ' ' * horizontal_position + line for line in lines
    )

    start_time = time.time()
    while time.time() - start_time < 1:  # Durée totale de l'animation
        for dots in ["", ".", "..", "...",]:
            clear_console()
            print(Fore.LIGHTMAGENTA_EX + message)

            sys.stdout.flush()
            time.sleep(0.5)

    # Efface la console après l'animation
    clear_console()

    print(Fore.LIGHTMAGENTA_EX + """
d8b   db d88888b d8888b. d888888b db    db d8b   db d88888b      .d8888.  .o88b. d8888b. d888888b d8888b. d888888b 
888o  88 88'     88  `8D `~~88~~' 88    88 888o  88 88'          88'  YP d8P  Y8 88  `8D   `88'   88  `8D `~~88~~' 
88V8o 88 88ooooo 88oodD'    88    88    88 88V8o 88 88ooooo      `8bo.   8P      88oobY'    88    88oodD'    88    
88 V8o88 88~~~~~ 88~~~      88    88    88 88 V8o88 88~~~~~        `Y8b. 8b      88`8b      88    88~~~      88    
88  V888 88.     88         88    88b  d88 88  V888 88.          db   8D Y8b  d8 88 `88.   .88.   88         88    
VP   V8P Y88888P 88         YP    ~Y8888P' VP   V8P Y88888P      `8888Y'  `Y88P' 88   YD Y888888P 88         YP 



                                        ╔══════════════════════════════╗
                                        ║   discord.gg/neptunescript   ║           
                                        ╚══════════════════════════════╝

    """)
    
    # Affiche le menu sous forme de tableau
    print(Fore.GREEN + "[Menu] \n ")
    print(Fore.BLUE + "[1] -> Solara Réparteur")
    print(Fore.WHITE + "[2] -> Maj Bloquer")
    print(Fore.RED + "[3] -> Soon")

# Fonction principale
def main():
    while True:  # Boucle pour permettre la répétition en cas d'option invalide
        display_large_loading_message()  # Affiche le message de chargement

        n = input(Fore.MAGENTA + "\nVeuillez entrer un numéro : " + Fore.YELLOW)

        if n == '1':
            # Obtient le chemin du répertoire temporaire de l'utilisateur et nettoie les fichiers temporaires
            user_profile = os.environ.get('USERPROFILE', '')  # Utilisez get() pour éviter une KeyError
            if user_profile:
                temp_directory_path = os.path.join(user_profile, 'AppData', 'Local', 'Temp')
                if os.path.exists(temp_directory_path):
                    clear_temp_directory(temp_directory_path)
                else:
                    print(Fore.RED + "Le répertoire temporaire n'existe pas.")
            else:
                print(Fore.RED + "Le chemin du profil utilisateur est introuvable.")
            break  # Quitte la boucle après une option valide
    
        elif n == '2':
            print(Fore.GREEN + "Test pour la fonction 'maj bloquer'.")
            break  # Quitte la boucle après une option valide

        else:
            print(Fore.RED + "Option non valide.")
            print(Fore.YELLOW + "\n Appuyez sur une touche pour recommencer...")
            input()  # Attend que l'utilisateur appuie sur une touche
            clear_console()  # Efface la console avant de redemander l'entrée

if __name__ == "__main__":
    main()
