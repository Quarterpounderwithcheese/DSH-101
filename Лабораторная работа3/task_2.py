# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    intersection_group = list(set(first_group).intersection(second_group))
    return intersection_group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

intersection_group = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(intersection_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
