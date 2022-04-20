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
    print('2 - сортировать')
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
            new_data = input('введите данные о продукте: ').split()
            new_item.title = new_data[0]
            new_item.shop = new_data[1]
            new_item.count = new_data[2]
            new_item.unit = new_data[3]
            g.append(new_item)

    elif n == '2':
        for x in st:
            if 2 in x.marks:
                print(x.fam, x.name, x.surname, *x.marks)

    elif n == '3':
        fam1 = input('Введите фамилию студента: ')
        student = input('Введите все данные о студенте: ').split()
        for x in st:
            if x.fam == fam1:
                x.fam = fam1
                x.name = student[1]
                x.surname = student[2]
                x.marks = list(map(int, student[3:]))

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

