from logger  import input_data, print_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник \n 1- запиь данных \n 2- вывод данных")
    command=int(input("Введите число"))
    
    while command !=1 and command !=2:
        print("Не правильный ввод")
        command=int(input("Введите число "))
    
    if command==1:
        input_data()
    elif command ==2:
        print_data()
