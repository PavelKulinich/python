import random
class PlayIteration:
    def __init__(self, lst_of_barrels):
        self.lst_of_barrels = lst_of_barrels
    def __str__(self):
        return 'я - итератор вытаскивания бочонков'
    def __iter__(self):
        return self
    def __next__(self):
        number = random.choice(self.lst_of_barrels)
        if len(self.lst_of_barrels) > 1:
            self.lst_of_barrels.remove(number)
            return number
        else:
            raise StopIteration
    @staticmethod
    def cart_gen():
        print("=" * 120)
        stringline = []
        print("Карточка {}".format(cartholder))
        while len(stringline) < 30:
            x = random.randint(1, 90)
            if x not in stringline:
                stringline.append(x)
        return stringline
lst_of_barrels = []
for i in range(1, 91):
    lst_of_barrels.append(i)
cartholder = 'моя'
my_cart = []
my_cart.append(PlayIteration.cart_gen())
my_cart = my_cart[0]
print(my_cart)
his_cart =[]
cartholder = 'соперника'
his_cart.append(PlayIteration.cart_gen())
his_cart = his_cart[0]
print(his_cart)
next_barrel = PlayIteration(lst_of_barrels)
barrels_iterator = (i for i in next_barrel)
for i in barrels_iterator:
    print("="*120)
    print("=====Новый ход! Номер бочонка: {}. Осталось ходов: {}=======================".format(i, len(lst_of_barrels)))
    x1 = int(i)
    do = input("Зачеркнуть цифру? y/n")
    if do == 'y':
        if x1 in his_cart:
            his_cart.remove(x1)
            print("Карточка моя\n", my_cart)
            print("Карточка соперника\n", his_cart)
        if x1 in my_cart:
            my_cart.remove(x1)
            print("Карточка моя\n", my_cart)
            print("Карточка соперника\n", his_cart)
        else:
            print("Игра завершена, Вы проиграли(...")
            break
    else:
        if x1 in his_cart:
            his_cart.remove(x1)
            print("Карточка моя\n", my_cart)
            print("Карточка соперника\n", his_cart)
        if x1 in my_cart:
            #my_cart.remove(x1)
            print(x1)
            print("Карточка моя\n", my_cart)
            print("Карточка соперника\n", his_cart)
            print("Игра завершена, Вы проиграли(...")
            break
if any(my_cart) is int and any(his_cart) is int:
    print("Продолжаем играть!")
    next(barrels_iterator)
elif my_cart == []:
    print("Поздравляем, Вы - ВЫИГРАЛИ!")
elif his_cart == []:
    print("Вы проиграли...")
