import os
import time
import subprocess
from pyfiglet import Figlet


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def intro(figlet):
    clear()
    print(figlet.renderText('deathstar'))
    print("[Github]: https://github.com/floxs2/deathstar")
    time.sleep(0.3)


def links(nick):
    platforms = [
        ("Youtube", f"https://youtube.com/@{nick}"),
        ("TikTok", f"https://tiktok.com/@{nick}"),
        ("Telegram", f"https://t.me/{nick}"),
        ("Vk", f"https://vk.com/{nick}"),
        ("Pinterest", f"https://pinterest.com/{nick}"),
        ("Github", f"https://github.com/{nick}"),
        ("Steam", f"https://steamcommunity.com/id/{nick}")
    ]

    print("Found:")
    for platform, link in platforms:
        print(f"[{platform}]: {link}")
        time.sleep(0.3)


def main():
    time.sleep(0.3)
    figlet = Figlet(font='slant')

    intro(figlet)

    nick = input("Enter nickname: ")
    time.sleep(0.3)

    intro(figlet)
    links(nick)

    restart = input("Restart program (yes/no): ").strip().lower()
    if restart == "yes":
        current_dir = os.path.dirname(os.path.abspath(__file__))
        main_path = os.path.join(current_dir, 'main.py')
        subprocess.run(['python', main_path])
    elif restart == "no":
        print("Exit")
    else:
        print("Invalid input. Exiting...")


if __name__ == "__main__":
    main()
