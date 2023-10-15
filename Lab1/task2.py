list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

players_count = len(list_players)
list_players_1 = list_players[0:int(players_count/2)]
list_players_2 = list_players[int(players_count/2):players_count]
print(list_players_1)
print(list_players_2)
