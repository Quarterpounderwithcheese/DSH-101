users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

dict_ = {"Общее количество": 0, "Уникальные посещения": 0}
dict_["Общее количество"] = len(users)
unique_users = set(users)
dict_["Уникальные посещения"] = len(unique_users)
print(dict_)
