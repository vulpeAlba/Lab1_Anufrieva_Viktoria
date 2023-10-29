# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, splitter=','):
    same_participants_set = set(str1.split(splitter)).intersection(str2.split(splitter))
    return sorted(same_participants_set)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
