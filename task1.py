numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
lenght = len(numbers)
missing_index = 4
average = round(sum(numbers[:4] + numbers[5:]) / lenght, 2)
numbers[missing_index] = average
print("Измененный список:", numbers)

