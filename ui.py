from logger import input_data, print_data
from Change import change_data, delete_row

def interface():
    print("Добрый день! Вы попали на специальный бот справочник \n 1- запиь данных \n 2- вывод данных \n 3- изменить данные \n 4 - удалить данные")
    command=int(input("Введите число"))
    
    while command !=1 and command !=2 and command !=3 and command !=4:
        print("Не правильный ввод")
        command=int(input("Введите число "))
    
    if command==1:
        input_data()
    elif command ==2:
        print_data()
    elif command ==3:
        change_data()
    elif command ==4:
        delete_row()
