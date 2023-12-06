import random

print('Wählen sie ein Variante aus:')
print('[1].Stein')
print('[2].Schere')
print('[3].Papier')

game_list = ['Stein', 'Schere', 'Papier']
eingabe = input()

enemy_list = random.choices(game_list)
enemy = ''.join(str(x) for x in enemy_list)


def player_choice():
    if eingabe == "1":
        selection = "Stein"
        return selection
    elif eingabe == "2":
        selection = "Schere"
        return selection
    elif eingabe == "3":
        selection = "Papier"
        return selection


def res_check():
        player_choice()
        while True:
            if eingabe == "1" and enemy == "Schere":
                res = "Du hast gewonnen"
                return res
            elif eingabe == "2" and enemy == "Papier":
                res = "Du hast gewonnen"
                return res
            elif eingabe == "3" and enemy == "Stein":
                res = "Du hast gewonnen"
                return res
            elif eingabe == "1" and enemy == "Stein":
                res = "Unterscheiden"
                return res
            elif eingabe == "2" and enemy == "Schere":
                res = "Unterscheiden"
                return res
            elif eingabe == "3" and enemy == "Papier":
                res = "Unterscheiden"
                return res
            elif eingabe == "1" and enemy == "Papier":
                res = "Du hast Verloren"
                return res
            elif eingabe == "2" and enemy == "Stein":
                res = "Du hast Verloren"
                return res
            elif eingabe == "3" and enemy == "SChere":
                res = "Du hast Verloren"
                return res


print(res_check())
print(player_choice(), 'schlägt', enemy)
