# Исходные данные
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальное значение индекса
counter = 0

# Цикл while для перебора элементов списка
while counter < len(my_list):
    current_number = my_list[counter]

    if current_number < 0:  # Оператор break при встрече отрицательного числа
        break
    elif current_number == 0:  # Оператор continue для игнорирования нуля
        counter += 1
        continue
    else:  # Если число положительное
        print(current_number)

    counter += 1  # Увеличиваем индекс для перехода к следующему элементу
