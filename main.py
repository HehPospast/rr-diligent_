"""-----RUSSIAN ROULETTE-----"""
import random
import time
from colorama import Fore

info = Fore.BLUE+"[ИНФО]"+Fore.RESET
game = Fore.CYAN+"[ИГРА]"+Fore.RESET
text = Fore.RED+""


def begin():
    print(Fore.GREEN+"----/*RUSSIAN ROULETTE*\----    -*-*-by HehPospast-*-*-" )
    print("-This is some shitty game-"+Fore.RESET)


def get_players():
    Valid = False
    while not Valid:
        players = input(info+text+"Введите число игроков ---- (Число игроков не может быть больше 6, и равно 1) -")
        try:
            players = int(players)
        except:
            print(info+text+"Введите другое число")
            continue
        if players >= 2 and players <= 6:
            Valid = True
            return players
        else:
            print(info+text+"Вы указали неправильное число----(Возможно указано больше 6 или 1)")


def slugs(players):
    Valid = False
    while not Valid:
        shots = input(info+text+"Введите число пуль----(Число пуль не может быть больше 6 и равно числу игроков) -")
        try:
            shots = int(shots)
        except:
            print(info+text+"Введите другое число")
            continue
        if players==shots:
            print(info+text+"Пули равны количеству игроков, так все умрут :)")
        elif shots >= 1 and shots <= 6:
            Valid = True
            return shots
        else:
            print(info+text+"Вы указали неправильное число----(Возможно указано больше 6)")
    return players


def main():
    begin()
    players=get_players()
    win = False
    startpos = 1
    shot=random.randrange(1, players+1, 1)
    slug= slugs(players)
    while not win:
        time.sleep(1)
        print(game+text+f"Ход игрока №{startpos}")
        checkplayer= input(str(info+text+'Для совершения выстрела нажмите ENTER -*ничего не вводя-'))
        if (checkplayer == ""):
            print(game+text+f"Выстрел игрока №{startpos}")
            time.sleep(2)
            if shot==startpos:
                print(game+text+f'Умер игрок №{startpos}')
                players-=1
                slug-=1
                time.sleep(1)
                print(info+text+f"Количество живых игроков: {players}")
                time.sleep(1)
                print(info+text+f"Количество патронов в барабане: {slug}")
                shot=random.randrange(1, players+1, 1)
                startpos=players
            else:
                print(game+text+f'Пустой патрон')
                time.sleep(1)
                print(info+text+f"Количество патронов в барабане: {slug}")
            if startpos==players:
                startpos=1
            else:
                startpos+=1
            if slug==0:
                print(info+text+"Патроны кончились")
                time.sleep(3)
                win = True


def start():
    main()


start()
