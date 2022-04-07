import pickle

class Shop:

    name_of_product = None
    name_of_shop = None
    count = None
    quanity = None

f = open('students.txt', 'r', encoding='utf-8')
s = []
while True:
    x = f.readline()
    if not x:
        break
    x = x.split(' ', 3)
    shop = Shop()
    shop.name_of_product = x[0]
    shop.name_of_shop = x[1]
    shop.count = x[2]
    shop.quanity = x[3]
    s.append(shop)
    print(shop.name_of_product, shop.name_of_shop, shop.count, shop.quanity)

d = open('shop.dat', 'wb')
pickle.dump(s, d)
d.close()
f.close()

