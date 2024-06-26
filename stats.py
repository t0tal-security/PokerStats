#!/usr/bin/python3
import datetime
current_date = str(datetime.datetime.now()).split(".")[0]

import helpers
import time
import random
import time

import exslog
try:
    helpers.clear()
    user_verbose = int(input("Set program verbosity\n0 - 3  a.k.a.  less - more\n( 0-3 ) >> "))

except ValueError:
    print("not a number")
    exit()

else:
    success = exslog.Exslog("success", user_verbose)
    error = exslog.Exslog("error", user_verbose)
    info = exslog.Exslog("info", user_verbose)

players = []
try:
    for i in range(10):
        helpers.clear()
        
        info.say(1, f"adding random players #{i}")
        players.append(helpers.random_number())

        time.sleep(random.uniform(0.1,0.4))

except KeyboardInterrupt:
    exit()

stats = []
players_amt = 0
game_elapsed_time = 0.0
hand = 0
helpers.greetings()

try:
    players_amt_choice = helpers.player_amt()
    
    match players_amt_choice:
        case "o":
            try:
                players_amt = int(input("Amount >> "))
            
            except ValueError:
                error.say(0, "Not a number!")
                exit()
            
            else:
                stats.append(players_amt_choice)
                stats.append(players_amt)

        case "r":
            players_amt = players[random.randrange(0, len(players))]

            stats.append(players_amt_choice)
            stats.append(players_amt)

        case _:
            error.say(0, "Bad choice!")
            exit()

except KeyboardInterrupt:
    exit()


def main() -> list:
    error_msg = ""
    start = time.time()

    while True:
        helpers.clear()
        info.say(0, f"Players: {players_amt}\n{error_msg}\n")
        
        hand = helpers.all_hands()

        if hand == 99:
            break
        
        elif hand == -1:
            error_msg = error.say(0, "Wrong hand")
            continue

        elif hand > 9:
            error_msg = error.say(0, "Too big hand [ 0-9 ]")
            continue

        elif 0 > hand:
            error_msg = error.say(0, "Too small [ 0-9 ]")
            continue
        
        else:
            error_msg = ""
            mine = str(input("yours? (y/n) >> "))

            with open("handsstats.txt", "a") as hands_file:
                data_to_write = f"{str(datetime.datetime.now()).split('.')[0],hand,mine}\n"
                hands_file.writelines(data_to_write)
            continue

    end = time.time()
    game_elapsed_time = end - start

    #======================
    #laczny czas rozgrywek
    #ile razy jaki uklad
    #laczna ilosc trafien ukladow
    #laczna ilosc wszystkich ukladow
    #na procenty

    return [stats, round(game_elapsed_time, 2)]


if __name__ == "__main__":
    try:
        with open("pokerstats.txt", "a") as file:
            file.writelines(f'\n<{current_date}>\n')

        data = main()
        
        success.say(0, f"elapsed time: {data[1]} seconds | {round(data[1]/60,2)} minutes | {round((data[1]/60)/60,2)} hours")
    
    except KeyboardInterrupt:
        with open("pokerstats.txt", "a") as file:
            file.writelines("interrupted\n")
        exit()
    
    else:
        data_to_write = f"{data[0]},{data[1]}s\n"

        with open("pokerstats.txt", "a") as file:
            file.writelines(data_to_write)
