import pickle

class Goods:
    title = None
    shop = None
    count = None
    unit = None

f = open('goods.dat', 'rb')
g = pickle.load(f)
for x in g:
    print(x.title, x.shop, x.count, x.unit)

while True:
    print('Введите номер операции')
    print('1 - изменить базу данных')
    print('2 - сортировать по названию товара или магазина')
    print('3 - вывод информации о товаре')
    print('4 - сохранить изменения/изменить название базы')
    print('5 - выйти')

    n = input()
    if n == '1':
        a = input('корректировать данные / дополнить список данных (ввести нужное): ')
        if a == 'корректировать':
            g_title = input('введите название продукта, информацию о котором хотите корректировать: ')
            new_data = input('введите новые данные о продукте: ').split()
            for x in g:
                if x.title == g_title:
                    x.shop = new_data[1]
                    x.count = new_data[2]
                    x.unit = new_data[3]
        elif a == 'дополнить':
            new_item = Goods()
            new_data = input('Введите данные о продукте: ').split()
            new_item.title = new_data[0]
            new_item.shop = new_data[1]
            new_item.count = new_data[2]
            new_item.unit = new_data[3]
            g.append(new_item)

    elif n == '2':  # сортировать по названию товара или магазина
        total_1 = []
        total_2 = []
        print('Если хотите сортировать по товару, то нажмите 1, если хотите сортировать по магазинам, то нажмите 2')
        m = int(input()):
        if m == '1':
            for x in g:
                total_1.append(x.title)
            for el in total_1:
                for ele in x:
                    if ele.title == el:
                        print(ele.title, ele.shop, ele.count, ele.unit)
                    
        elif m == '2':
            for x in g:
                total_2.append(x.shop)
            for el in total_2:
                for ele in x:
                    if ele.shop == el:
                        print(ele.title, ele.shop, ele.count, ele.unit)

    elif n == '3':
        name = input('Введите название товара: ')
        for x in g:
            if x.title == name:
                print(x.title, x.shop, x.count, x.unit)

    elif n == '4':
        for x in st:
            print(x.fam, x.name, x.surname, x.marks)

    elif n == '5':
        a = input('Выйти? да/нет ')
        if a == 'да':
            break
    else:
        print('Нет такой операции')

d = open('goods.dat', 'wb')
pickle.dump(g, d)
d.close()
f.close()

