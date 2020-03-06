class Car:
    # --- 變數(Property)
    year = 2019
    mpg = 30
    speed = 0
    # ---方法(Method)
    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

def main():
    car1 = Car()
    print('car1', type(car1), id(car1))
    print('speed', car1.speed)
    car1.accelerate()
    car1.accelerate()
    print('speed', car1.speed)
    car1.brake()
    print('speed', car1.speed)


if __name__ == "__main__":
    main()

print()
# ------ 第二題 ------
class Car:
    # --- 變數(Property)

    year = 2019
    mpg = 30
    speed = 0
    # ---方法(Method)

    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

def main():
    car1 = Car()
    car2 = Car()
    car1.accelerate()
    car1.accelerate()
    print("car1 speed =", car1.speed)
    print("car2 speed =", car2.speed)


if __name__ == "__main__":
    main()

print()
# ------ page. 4 ------
class Car:

    year = 2019
    mpg = 30
    speed = 0

    def __init__(self):
        self.speed = 10

    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

def main():
    car1 = Car()
    print('car1 speed', car1.speed)


if __name__ == "__main__":
    main()

print()
# ------ page. 5 -----
class Car:

    year = 2019
    mpg = 30
    speed = 0

    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

def main():
    car1 = Car(15)
    print('car1 speed', car1.speed)


if __name__ == "__main__":
    main()

print()
# --- 練習 ---
class Box():
    H = 0
    W = 0
    L = 0
    Name = ''

    def __init__(self, L, W, H, Name):
        self.L = L
        self.W = W
        self.H = H
        self.Name = Name

    def info(self):
        print(self.Name, self.L, self.W, self.H)

    def volume(self):
        print(self.L * self.H * self.W)

def main():
    b1 = Box(1, 1, 1, 'box1')
    b1.info()
    b1.volume()

    b2 = Box(10, 20, 30, 'box2')
    b2.info()
    b2.volume()


if __name__ == "__main__":
    main()

print()
# --- 類別方法(class method)
class Box():
    H = 1
    W = 2
    L = 3
    Name = ''

    def __init__(self, L, W, H, Name):
        self.L = L
        self.W = W
        self.H = H
        self.Name = Name

    def info(self):
        print(self.Name, self.L, self.W, self.H)

    @classmethod
    def volume(cls):
        print(cls.L * cls.H * cls.W)

    def get_volume(self):
        print(self.L * self.H * self.W)

def main():
    Box.volume()

    b1 = Box(1, 1, 1, 'box1')
    b1.info()
    b1.volume()
    b1.get_volume()


if __name__ == "__main__":
    main()

print()
# ------ page. 6 ------
class A:
    count = 0

    def __init__(self):
        A.count += 1

    @classmethod
    def get_count(cls):
        print(cls.count)

    def add_count(self):
        self.count += 1

def main():
    A.get_count()
    a1 = A()
    A.get_count()
    a1.add_count()
    a1.add_count()
    print(a1.count)
    print("空一行")
    a2 = A()
    a2.get_count()
    a2.add_count()
    a2.add_count()
    print(a2.count)


if __name__ == "__main__":
    main()

print()
# ------ 第二題 ------
# --- 靜態方法(static method)
class A:
    count = 0

    def __init__(self):
        A.count += 1

    @classmethod
    def get_count(cls):
        print(cls.count)

    def add_count(self):
        self.count += 1

    @staticmethod
    def usage():
        print('A is a class used to demo class method')

def main():
    A.usage()
    A.get_count()
    a1 = A()
    A.get_count()
    a2 = A()
    A.get_count()


if __name__ == "__main__":
    main()

print()
# ------ page. 7 ------
class Car:
    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 20

    def brake(self):
        self.speed -= 10

def main():
    Car.color = 'black'
    Car.brand = 'benz'
    car1 = Car(15)
    car1.type = 'SUV'

    print('car1 speed', car1.speed)
    print('car1 color', car1.color)
    print('car1 brand', car1.brand)
    print('car1 type', car1.type)


if __name__ == "__main__":
    main()

print()
# ------ page. 8 ------
# --- 封裝
class Book():
    def __init__(self, name='', author='', price=0):
        self.name = name
        self.author = author
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        self.__price = value

def main():
    book1 = Book('哈利波特神秘的魔法石', 'JK羅琳', 350)
    print('書名 :', book1.name)
    print('作者 :', book1.author)
    book1.price = 350
    print('售價 :', book1.price, '$NTD')


if __name__ == "__main__":
    main()

print()
# ------ page. 9 ------
# --- 類別內建方法
class Book():
    def __init__(self, name='', author='', price=0):
        self.name = name
        self.author = author
        self.__price = price

    def __str__(self):
        return 'name, '+self.name +\
               ', author, '+self.author+',' \
               ' price, '+str(self.__price)

    def __del__(self):
        print(self.name+'已移除')

    def __call__(self, name='', author='', price=0):
        if len(name.strip()) > 0:
            self.name = name
        if len(author.strip()) > 0:
            self.author = author
        if price >= 0:
            self.__price = price

def main():
    book1 = Book('哈利波特神秘的魔法石', 'JK羅琳', 350)
    book1('哈利波特-消失的密室', '', 320)
    print(book1)


if __name__ == "__main__":
    main()

print()
# ------ page. 10 ------
# --- 父類別
class Car:
    year = 1990 ; mpg = 30000 ; speed = 0

    def __init__(self, year , mpg, speed):
        self.year = year
        self.mpg = mpg
        self.speed = speed

    def accelerate(self):
        self.speed += 20
        print('speed up :', self.speed)

    def brake(self):
        self.speed -= 10
        print('speed down :', self.speed)


# --- 子類別
class RaceCar(Car):
    def __init__(self, color='', make='', engine='', year='', mpg=0, speed=0):
        self.color = color
        self.make = make
        self.engine = engine
        super(RaceCar, self).__init__(year, mpg, speed)

    def turbo_start(self):
        self.speed += 100
        print('Turbo Mode Start Speed :', self.speed)

    def brake(self):
        print('ABS Mode Start')
        super().brake()

def main():
    my_car = RaceCar('White', 'NISSAN GTR', 'V6', '2007', 3000, 0)
    print(my_car.color, my_car.make)
    my_car.accelerate()
    my_car.turbo_start()
    my_car.accelerate()
    my_car.brake()


if __name__ == "__main__":
    main()

print()
# ------ page. 13 ------
# --- 多重繼承
class Base(object):
    def __init__(self):
        print('I am Base')

class A(Base):
    def __init__(self):
        print('I am A')
        super().__init__()

class B(Base):
    def __init__(self):
        print('I am B')
        super().__init__()

class C(A,B):
    def __init__(self):
        super().__init__()

def main():
    c = C()


if __name__ == "__main__":
    main()

print()
# --- 多型
class Juicer:
    def open(self):
        print('開啟果汁電源')

    def run(self):
        print('開始打果汁')

class Washer:
    def open(self):
        print('開啟洗衣機電源')

    def run(self):
        print('開始洗衣服')


def auto_run(thing):
        thing.open()
        thing.run()

def main():
    machine = Juicer()
    auto_run(machine)

    machine = Washer()
    auto_run(machine)


if __name__ == "__main__":
    main()

print()
# ------ page. 14 ------
# --- 運算子多載
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        v = Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        return v

    def __sub__(self, other):
        v = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        return v

    def __str__(self):
        s = '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'
        return s

def main():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(1, 1, 0)

    print(v1 - v2)
    print(v1 + v2)


if __name__ == "__main__":
    main()

print()
# --- 迭代器(iterator)
class GiveMeFive:
    def __iter__(self):
        self.a = 5
        return self

    def __next__(self):
        x = self.a
        self.a += 10
        return x

def main():
    gm5 = iter(GiveMeFive())

    print(next(gm5))
    print(next(gm5))
    print(next(gm5))
    print(next(gm5))
    print(next(gm5))
    print(next(gm5))
    print(next(gm5))


if __name__ == "__main__":
    main()














