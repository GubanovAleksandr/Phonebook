def change_data():
    var = 2
    if var == 2:
        with open("data_second_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()
            count_rows = len(data)
            if count_rows == 0:
                print("Файл пустой")
            else:
                number_row = int(input(f"Введите номер строки "
                                       f"от 1 до {count_rows}: "))
                while number_row < 1 or number_row > count_rows:
                    number_row = int(input(f"Ошибка!"
                                           f"Введите номер строки "
                                           f"от 1 до {count_rows}: "))
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    phone = input("Введите телефон: ")
    adress = input("Введите адрес: ")
    data[number_row - 1] = f'{name};{surname};{phone};{adress}\n'
    with open("data_second_variant.csv", 'w', encoding='utf-8') as file:
        file.writelines(data)
        print("Данные успешно изменены!")

def delete_row():

    var = int(input(f"В каком файле удалить данные? Данные можно удалить только из второго файла \n\n "))

    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()
            count_rows = len(data)
            if count_rows == 0:
                print("Файл пустой")
            else:
                number_row = int(input(f"Введите номер строки от 1 до {count_rows}"))
                while number_row < 1 or number_row > count_rows:
                    number_row = int(input(f"ОШИБКА Введите номер строки от 1 до {count_rows}"))
                del data[number_row - 1]
                data = [f'{i + 1};{data[i].split(";")[1]};'
                        f'{data[i].split(";")[2]};'
                        f'{data[i].split(";")[3]};'
                        f'{data[i].split(";")[4]}'
                        for i in range(len(data))]
                with open("data_first_variant.csv", 'w', encoding='utf-8') as file:
                    file.writelines(data)
                print("Строка успешно удалена!")

                print(data)

    elif var == 2:
        with open("data_second_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()
            count_rows = len(data)
            if count_rows == 0:
                print("Файл пустой")
            else:
                number_row = int(input(f"Введите номер строки от 1 до {count_rows}"))
                while number_row < 1 or number_row > count_rows:
                    number_row = int(input(f"ОШИБКА Введите номер строки от 1 до {count_rows}"))
                del data[number_row - 1]
                data = [f'{i + 1};{data[i].split(";")[1]};'
                        f'{data[i].split(";")[2]};'
                        f'{data[i].split(";")[3]};'
                        f'{data[i].split(";")[4]}'
                        for i in range(len(data))]
                with open("data_second_variant.csv", "w", encoding="utf-8") as file:
                             file.write('\n'.join(data))
                print("Строка успешно удалена!")