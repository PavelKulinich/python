# coding: utf-8
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
int_x = int(equation[4:7])
b = float(equation[-13:])
y = int_x*x+b
print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

date = '01.13.198'
date_lst = date.split('.')
err_lst = []

# обрабатываем день
day = date_lst[0]
if len(day)!=2:
        err_lst.append('Количество символов в дне не равно 2')
if not int(day) in range(1,31):
    err_lst.append('День больше максимального или ввели отрицательное значение или день равен нулю')

# обрабатываем месяц
month = date_lst[1]
if len(month)!=2:
        err_lst.append('Количество символов в месяце не равно 2')
if not int(month) in range(1,12):
    err_lst.append('Месяц больше максимального или ввели отрицательное значение или месяц равен нулю')

# обрабатываем год
year = date_lst[2]
if len(year)!=4:
        err_lst.append('Количество символов в году не равно 4')
if not int(year) in range(1,9999):
    err_lst.append('Год больше максимального или ввели отрицательное значение или месяц равен нулю')

if len(err_lst)==0:
    print('Ошибок в дате нет!')
else:
    print('В дате допущены следующие ошибки: ')
    for i in range(len(err_lst)):
        print(i,err_lst[i])

# coding: utf-8
# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

x = int(input('Введите номер комнаты: '))
sch = 1
lst = []
b = 1
floor=0
num=0
for i in range(x):
	for m in range(i):
		if sch>x:
			break
		else:
			lst.append([i]*i)
			sch+=1

for i in lst:
	if i[0]==1:
		continue
	else:
		for v in range(len(i)):
			if i[v]==2 and v==0:
				continue
			else:
				i[v]=i[v]+b
				b+=1
t=1
for q in lst:
	if x in q:
		floor=t
		num=q.index(x)
		num+=1 #т.к q.index получает индекс, то чтобы получить именно номер, прибавим единицу, т.к индекс начинается с 0
		break
	else:
		t+=1
print('Номер этажа: ',floor)
print('Порядковый номер на этаже: ',num)
                                                                            
