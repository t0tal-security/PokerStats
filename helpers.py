import platform
import subprocess
import random


def clear() -> None:
    match platform.system():
        case "Windows":
            subprocess.run(["cls"])
        
        case _:
            try:
                subprocess.run(["clear"])
                
            except subprocess.CalledProcessError:
                print("can't clear screen...")


def random_number() -> int:
    return random.randrange(2, 9)


def player_amt() -> str:
    print("\nNumber of players: [o]wn / [r]andom")
    return str(input("o / r >> "))


def all_hands() -> int:
    print("""[9] Poker Krolewski
[8] Poker
[7] Four Of A Kind
[6] Full House
[5] Kolor
[4] Straight
[3] Three Of A Kind
[2] Dwie Pary
[1] Para
[0] Wysoka Karta

[99] Exit""")

    try:
        # wartosc wyzsza niz 9 -> fix in handsstats.txt
        # hand == -1 -> fix in handsstats.txt
        hand = int(input("\nhand >> "))
    
    except ValueError:
        return -1
    
    else:
        return hand


def greetings() -> None :
    clear()
    print("Count your PokerStats")