import pickle


class Goods:
    name = None
    shop = None
    count = None
    unit = None


fname = input('введите имя базы данных: ')
f = open(fname, 'rb')
g = pickle.load(f)
for x in g:
    print(x.name, x.shop, x.count, x.unit)
print()

while True:
    print('Введите номер операции')
    print('1 - изменить базу данных')
    print('2 - сортировать список данных')
    print('3 - вывод информации о товаре')
    print('4 - сохранить изменения')
    print('5 - вывести данные')
    print('6 - выйти')

    n = input()
    if n == '1':
        a = input('корректировать данные / дополнить список данных (ввести нужное): ')
        if a == 'корректировать':
            g_title = input('введите название продукта, информацию о котором хотите корректировать: ')
            new_data = input('введите новые данные о продукте: ').split()
            for x in g:
                if x.name == g_title:
                    x.shop = new_data[1]
                    x.count = new_data[2]
                    x.unit = new_data[3]
        elif a == 'дополнить':
            new_item = Goods()
            new_data = input('Введите данные о продукте: ').split()
            new_item.name = new_data[0]
            new_item.shop = new_data[1]
            new_item.count = new_data[2]
            new_item.unit = new_data[3]
            g.append(new_item)

    elif n == '2':
        a = input('сортировать по названию товара / назвнию магазина (ввести нужное): ')
        if a == 'по названию товара':
            g.sort(key=lambda x: x.name)
            for x in g:
                print(x.name, x.shop, x.count, x.unit)
        elif a == 'по названию магазина':
            g.sort(key=lambda x: x.name)
            for x in g:
                print(x.name, x.shop, x.count, x.unit)

    elif n == '3':
        name = input('Введите название товара: ')
        for x in g:
            if x.name == name:
                print(x.name, x.shop, x.count, x.unit)

    elif n == '4':
        a = input('сохранить базу под старым / новым именем (ввести нужное): ')
        if a == 'под старым':
            d = open(fname, 'wb')
            pickle.dump(g, d)
            d.close()
        elif a == 'под новым':
            fname = input('введите новое название базы: ')
            d = open(fname, 'wb')
            pickle.dump(g, d)
            d.close()

    elif n == '5':
        for x in g:
            print(x.name, x.shop, x.count, x.unit)

    elif n == '6':
        a = input('Выйти? да/нет ')
        if a == 'да':
            break
    else:
        print('Нет такой операции')

d = open(fname, 'wb')
pickle.dump(g, d)
d.close()
f.close()
