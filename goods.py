import pickle

class Goods:
    title = None
    shop = None
    count = None
    unit = None

f = open('goods.dat', 'rb')
gs = pickle.load(f)
for x in gs:
    print(g.title, g.shop, g.count, g.unit)

while True:
    print('Введите номер операции')
    print('1 - изменить базу данных')
    print('2 - сортировать')
    print('3 - вывод информации о товаре')
    print('4 - сохранить изменения/изменить название базы')
    print('5 - выйти')

    n = input()
    if n == '1':
        a = input('коректировать/дополнить ')
        if a == 'коректировать':
            g_title = input('введите название продукта, информацию о котором хотите корректировать: ')
            new_data = input('')
            
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

d = open('student.dat', 'wb')
pickle.dump(st, d)
d.close()
f.close()

