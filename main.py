import httpx
import os
import requests
import time



from colorama import Fore
from itertools import cycle

os.system("cls") if os.name == "nt" else os.system("clear")
__tokens__, __proxy__, __threads__ = open("tokens.txt", "r").read().splitlines(), cycle(open("proxies.txt", "r").read().splitlines()), 1


logo = """


    ___            _  __ _  
    / _ \_   _ _ __(_)/ _(_) ___ _ __
    / /_)/ | | | '__| | |_| |/ _ \ '__|
    / ___/| |_| | |  | |  _| |  __/ |
    \/     \__,_|_|  |_|_| |_|\___|_|


"""

print (logo)

def cleaner(token):
    try:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }

        while True:
            time.sleep(0.1)
            channels = httpx.get("https://discordapp.com/api/v9/users/@me/channels", headers=headers).json()
            requests = httpx.delete(f"https://discordapp.com/api/v9/channels/{channels[0]['id']}?silent=false", headers=headers).json()
            #print(requests)
            print(Fore.GREEN + "Token: " + token + " | Channel: " + channels[0]['id']) 

    except Exception as e:
        print (Fore.RED + "Token: " + token + " | Error: " + str(e))

for token in __tokens__:
    cleaner(token)
    __threads__ += 1
    print (Fore.YELLOW + "Token Nr: " + str(__threads__))
    time.sleep(0.1)

print (Fore.GREEN + "Done")



