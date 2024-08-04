import os
import shutil
import time
import sys
import requests
from colorama import init, Fore

# Initialise colorama pour la coloration de la sortie dans la console
init(autoreset=True)


GITHUB_VERSION_URL = 'https://github.com/votre-utilisateur/votre-repo/raw/main/version.txt'  # URL vers le fichier version.txt
GITHUB_SCRIPT_URL = 'https://github.com/votre-utilisateur/votre-repo/raw/main/votre_script.py'  # URL vers le script mis à jour

# Fonction pour télécharger le contenu d'une URL
def download_file(url, destination):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(Fore.GREEN + "Téléchargement réussi.")
    except Exception as e:
        print(Fore.RED + f"Erreur lors du téléchargement de {url}: {e}")

# Fonction pour obtenir la version depuis GitHub
def get_latest_version():
    try:
        response = requests.get(GITHUB_VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(Fore.RED + f"Erreur lors de la récupération de la version : {e}")
        return None

# Fonction pour obtenir la version actuelle du script
def get_local_version(version_file='version.txt'):
    if os.path.exists(version_file):
        with open(version_file, 'r') as file:
            return file.read().strip()
    return None

# Fonction pour mettre à jour le script
def update_script():
    print(Fore.YELLOW + "Une mise à jour est disponible. Téléchargement en cours...")
    download_file(GITHUB_SCRIPT_URL, sys.argv[0])  # Remplace le script en cours d'exécution
    print(Fore.GREEN + "Le script a été mis à jour. Veuillez relancer le script.")
    sys.exit(0)



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
$$ |      $$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |$$$$$$$  |$$$$$$/   
$$ |   __ $$ |  $$ | /    $$ |$$ |  $$/ $$ |  $$ |$$    $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |  $$ | __ 
$$ \__/  |$$ |  $$ |/$$$$$$$ |$$ |      $$ \__$$ |$$$$$$$$/ $$ | $$ | $$ |$$$$$$$$/ $$ |  $$ |  $$ |/  |
$$    $$/ $$ |  $$ |$$    $$ |$$ |      $$    $$ |$$       |$$ | $$ | $$ |$$       |$$ |  $$ |  $$  $$/ 
 $$$$$$/  $$/   $$/  $$$$$$$/ $$/        $$$$$$$ | $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ $$/   $$/    $$$$/  
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
