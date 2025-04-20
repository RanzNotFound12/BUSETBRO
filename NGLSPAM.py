import requests, time, threading, os
from datetime import datetime
try:
    from colorama import Fore, init
except:
    os.system("pip install colorama")
    from colorama import Fore, init

init(autoreset=True)

count = 0

ascii_art = Fore.GREEN + """
⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
"""

def get_time_wib():
    return time.strftime('%H:%M:%S', time.localtime(time.time() + 7 * 3600))

def show_status(username, message):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_art)
        print(Fore.LIGHTGREEN_EX + f"""
┏━━━━━━━━━━━ R A N Z  S P A M M E R ━━━━━━━━━━━┓
┃ Spam   : {Fore.CYAN}{count:<39}{Fore.LIGHTGREEN_EX}┃
┃ Target : {Fore.CYAN}@{username:<38}{Fore.LIGHTGREEN_EX}┃
┃ Teks   : {Fore.CYAN}{message:<39}{Fore.LIGHTGREEN_EX}┃
┃ Waktu  : {Fore.CYAN}{get_time_wib()} WIB                 {Fore.LIGHTGREEN_EX}┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
        time.sleep(1)

def spam_ngl(username, message):
    global count
    url = "https://ngl.link/api/submit"
    payload = {
        "username": username,
        "question": message,
        "deviceId": "random-ranz-device"
    }
    try:
        requests.post(url, data=payload)
        count += 1
        time.sleep(0.25)
    except:
        pass

def start():
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_art)
    username = input(Fore.YELLOW + "[?] Masukkan Username NGL (tanpa @): ")
    message = input(Fore.MAGENTA + "[?] Masukkan Teks Spam: ")

    threading.Thread(target=show_status, args=(username, message), daemon=True).start()
    while True:
        threading.Thread(target=spam_ngl, args=(username, message)).start()

if __name__ == "__main__":
    start()
