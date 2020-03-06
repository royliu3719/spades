"""""# ------ page. 98 ------
a = '商品數量'
print(a)
s = '商品數量 : %d' % 10
print(s)
# --- 可寫回圈 ---
b = 10
c = '商品數量 : %d' % b
print(c)
# --- 第二題 ---
d = '商品數量 : %d   重量 : %.2f   品名 : %s' % (10, 800.456, '鮮奶')
print(d)

# ------ page. 99 ------
int_num = 108
money = 10.987654321
# ---
print("$%*.2f" % (7, money))
print('\n 字元格式 :')
# --- 用ASCLL---
print("%c" % 65)

print('\n 整數字串格式 :')
print("%d" % int_num )
print("%  d" % int_num)
print("%8d" % int_num)
print("%-8d" % int_num)
print("%08d" % int_num)

print('\n 十六進位格式 :')
print("%x" % int_num )
print("%X" % int_num )
print("%#x" % int_num )
print("%#X" % int_num )

# ------ page. 100 ------
float_num = 9876543.43210
num = 123
print("\n 浮點數與科學記號 :")
print("%f" % float_num)
print("%12.2f" % float_num)
print("%E" % float_num)
print("%e" % float_num)
print("%G" % float_num)
print("%g" % float_num)
print("%e" % (11111111111111111111111111))

print("\n 整數和字串輸出 :")
print("%+d" % 4)
print("%+d" % -4)
print("We are at %d%%" % 100)
print("Your host is: %s" % "earth")
print("Host : %s\tPort : %d" % ("Localhost", 80))
print("dec : %d/oct : %#o/hex : %#X" % (num, num, num))
print("MM/DD/YY = %02d/%02d/%d" % (2, 15, 67))
print("There are %(count)d %(lang)s" % {'lang' : 'Python', 'count' : 3})

# ------ page. 103 ------
# --- 按位置代入格式 ---
print('{0}, {1}, {2}'.format('a','b','c'))
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra', 'cad'))
# --- 按參數名稱代入格式 ---
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord={'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

# ------ page. 104 ------
# --- 按參數的屬性代入格式 ---
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}').format(c))
# --- 按照參數的項次代入格式 ---
coord = (3, 5)
print('X:{0[0]}; Y:{0[1]}'.format(coord))

# ------page. 105 ------
# --- 對齊以及指定寬度 ---
print('{:<30}'.format('left aligned'))   # -- 靠左對齊 --
print('{:>30}'.format('right aligned'))  # -- 靠右對齊 --
print('{:^30}'.format('centered'))       # -- 靠中對齊 --
print('{:*^30}'.format('centered'))      # -- 靠中對齊,然後用*補滿 --

# ------ page. 107 ------
# --- 使用逗號作為千分位分隔符號 ---
print('{:,}'.format(1234567980))
# --- 顯示兩位小數點與百分比 ---
points = 19
total = 22
print('Corrent answers: {:.2%}'.format(points/total))

# ------ page. 108 ------
# --- 特定類型的專屬格式化 ---
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# ------ 上課練習 ------
d={'a':3.141,'b':5.456}
print('{a:.2f} {b:.2f}'.format(**d))

print('{a:.2f} {b:.2f}'.format(a=3.141, b=5.456))"""


# ------ 作業 ------
# --- 格式化字串印出九九乘法表 ---
for n in range(1, 10):
    for X in range(2, 6):
        c = X*n
        print(X,'x',n,'=', '{:<2}'.format(c), " ", end='')
    print()
print()
for n in range(1, 10):
    for X in range(6, 10):
        c = X*n
        print(X,'x',n,'=', '{:<2}'.format(c), " ", end='')
    print()

print()
# ------ 另一種寫法 ------
for y in range(1,10):
    for x in range(2,6):
        print('{:<2}{:<2}{:<2}{:}{:<2}  '.format(x,'×',y,'= ',x*y),end='')
    else:
        print('\n',end='')

print('')

for y in range(1, 10):
    for x in range(6,10):
        print('{} {} {:<2}= {:<2}  '.format(x,'×',y,x*y),end='')
    else:
        print('\n',end='')





