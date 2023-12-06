import random

print('Wählen sie ein Variante aus:')
print('[1].Stein')
print('[2].Schere')
print('[3].Papier')

game_list = ['Stein', 'Schere', 'Papier']
eingabe = input()

gegner_list = random.choices(game_list)
gegner = ''.join(str(x) for x in gegner_list)


def spieler_choice():
    if eingabe == "1":
        spieler = "Stein"
        return spieler
    elif eingabe == "2":
        spieler = "Schere"
        return spieler
    elif eingabe == "3":
        spieler = "Papier"
        return spieler


def spiel_check():
    while True:
        spieler_choice()

        if eingabe == "1" and gegner == "Schere":
            res = "Du hast gewonnen"
            return res
        elif eingabe == "2" and gegner == "Papier":
            res = "Du hast gewonnen"
            return res
        elif eingabe == "3" and gegner == "Stein":
            res = "Du hast gewonnen"
            return res
        elif eingabe == "1" and gegner == "Stein":
            res = "Unterscheiden"
            return res
        elif eingabe == "2" and gegner == "Schere":
            res = "Unterscheiden"
            return res
        elif eingabe == "3" and gegner == "Papier":
            res = "Unterscheiden"
            return res
        elif eingabe == "1" and gegner == "Papier":
            res = "Du hast Verloren"
            return res
        elif eingabe == "2" and gegner == "Stein":
            res = "Du hast Verloren"
            return res
        elif eingabe == "3" and gegner == "SChere":
            res = "Du hast Verloren"
            return res


print(spiel_check())
print(spieler_choice(), 'schlägt', gegner)
