import pickle

class Goods:
    title = None
    shop = None
    count = None
    unit = None

f = open('goods.txt', 'r', encoding='utf-8')
goods = []
while True:
    x = f.readline()
    if not x:
        break
    x = x.split(' ', 3)
    g = Goods()
    g.title = x[0]
    g.shop = x[1]
    g.count = x[2]
    g.unit = x[3]
    goods.append(g)
    print(g.title, g.shop, g.count, g.unit)

d = open('goods.dat', 'wb')
pickle.dump(goods, d)
d.close()
f.close()
