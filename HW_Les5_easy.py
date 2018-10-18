# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def create_directories():
    for i in range(1, 10):
        name = 'dir_' + str(i)
        os.mkdir(os.path.join(os.getcwd(), name))


def delete_directories():
    for j in range(1, 10):
        name = 'dir_' + str(j)
        os.rmdir(os.path.join(os.getcwd(), name))
do = input("Выберите действие - c - create all directories, d - delete all directories")

if do == 'c':
    create_directories()
if do == 'd':
    delete_directories()
    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os


def current_dir_dirs():
    L = []
    for i in os.listdir():
        if os.path.isdir(i):
            L.append(i)
    print(L)

current_dir_dirs()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def current_file_copy():
    import shutil
    shutil.copy(__file__, "NEW")
    

current_file_copy()
