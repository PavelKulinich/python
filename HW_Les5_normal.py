# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os


def go_to():
    name_to_go = input("Введите название папки, в которую желаете перейти: ")
    path = os.path.join(os.getcwd(), name_to_go)
    os.chdir(path)
    print('Переход в папку {} успешно осуществлён'.format(name_to_go))
    current_dir_dirs()


def current_dir_dirs():
    print("Содержимое текущей директории:", os.listdir())


def create_directory():
    name_create = input("Введите название для создаваемой директории: ")
    try:
        os.mkdir(os.path.join(os.getcwd(), name_create))
        print('Директория {} создана'.format(name_create))
    except FileExistsError:
        print('Директория {} уже существует, выберите другое название'.format(name_create))


def delete_directory():
    name_delete = input("Введите имя удаляемой директории: ")
    try:
        os.rmdir(os.path.join(os.getcwd(), name_delete))
        print('Директория {} успешно удалена'.format(name_delete))
    except FileExistsError:
        print('Директории не найдено!'.format(name_delete))


do = input("Выберите действие из списка:\n"
           "[1] - Перейти в папку \n"
           "[2] - Просмотреть содержимое текущей папки\n"
           "[3] - Удалить папку\n"
           "[4] - Создать папку")
print('=' * 50)

if do == '1':
    name_to_go = input("Введите название папки, в которую желаете перейти: ")
    path = os.path.join(os.getcwd(), name_to_go)
    os.chdir(path)
    print('Переход в папку {} успешно осуществлён'.format(name_to_go))
    current_dir_dirs()
elif do == '2':
    current_dir_dirs()
elif do == '3':
    delete_directory()
elif do == '4':
    create_directory()
print('=' * 50)
