# ----- page. 18 -----
# --- 例外攔截
#try:
#    10*(1/0)

#except ZeroDivisionError:
#    print('I will catch you!')

#print()
# --- 完整版例外攔截
#import traceback
#try:
#    10*(1/0)
#    print(a)
#    b = [1, 2, 3]
#    print(b[5])
#    c = 1
#    print("c="+c)
#    print(traceback.print_exc())
#    print('攔截到其他錯誤')

#except ZeroDivisionError:
#   print('攔截到除以0的錯誤')

#except NameError:
#    print('攔截到未宣告變數的錯誤')

#except ImportError:
#    print('攔截到存取串列索引值超過範圍的錯誤')

#except:
#    print('攔截到其他錯誤')

#else:
#    print('都沒有出現例外,會到這裡')

#finally:
#    print('最後都會進到這裡')

#print()
# ------ page. 19 ------
# --- 引發例外
#try:
#    raise NameError('引起 NameError 例外')

#except NameError:
#    print('攔截到例外 NameError')
#    raise

#print()
# --- 函式的前置條件檢查
#def boxPrint(symbol, width, height):
#    if len(symbol) != 1:
#        raise Exception('Symbol must be a single character string')
#    if width <= 2:
#        raise Exception('Width must be great than 2')
#    if height <= 2:
#        raise Exception('Height must be great than 2')

#    print(symbol * width)
#    for i in range(height - 2):
#       print(symbol + (' ' * (width - 2)) + symbol)
#    print(symbol * width)

#for sym, w, h in (('*', 3, 3), ('@', 6, 4), ('x', 1, 3), ('zz', 3, 4)):
#    try:
#        boxPrint(sym, w, h)
#    except Exception as err:
#        print('An exception happend: ' + str(err))

#print()
# ------ page. 20 ------
# --- 自訂例外
#class MyError(Exception):
#    def __init__(self, value):
 #       self.value = value

#    def __str__(self):
#        return repr(self.value)

#try :
#    my_month_buget = 6000
#    cost_of_month = 7000

#    if cost_of_month > my_month_buget:
#        raise MyError('Out Of My Buget')

#except MyError as e:
#    print('My exception occurred, value :', e.value)

#print()
# ------ page. 21 ------
# --- Assertion Erroe
#try :
#    buget = 6000
#    while(True):
#        cost_of_month = input('請輸入每月花費 :')
#        if cost_of_month.strip() =='' :
#            break
#        assert  int(cost_of_month) <= buget, 'The Cost is Over Buget !'

#except AssertionError as err:
#    print('Assertion Error : ' + str(err))


# ------ page. 23 ------
#import sys
#print(sys.argv)

#buget = int(sys.argv[1])
#while(True):
#    try:
#        cost_of_month = input('請輸入每月花費 :')
#        if cost_of_month.strip() =='' :
#            break
#        assert  int(cost_of_month) <= buget, 'The Cost is Over Buget !'

#    except AssertionError as err:
#        print('Assertion Error : ' + str(err))

#print()
# ------ page. 25 ------
# --- 建立一個文字檔
f = open('wiki.txt', 'w', encoding='utf-8')

my_text = '''Python（英國發音：/ˈpaɪθən/ 美國發音：/ˈpaɪθɑːn/）是一種廣泛使用
的直譯式、進階程式、通用型程式語言，由吉多·范羅蘇姆創造，第一版釋出於1991年。
可以視之為一種改良（加入一些其他程式語言的優點，如物件導向）的LISP。
[來源請求]Python的設計哲學強調代碼的可讀性和簡潔的語法
（尤其是使用空格縮排劃分代碼塊，而非使用大括號或者關鍵詞）。
相比於C++或Java，Python讓開發者能夠用更少的代碼表達想法。
不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明了。
'''
f.write(my_text)
f.close()

# ------ page. 26 ------
# --- 附加一個文字檔
f = open('wiki.txt', 'a', encoding='utf-8')
f.write('\n')
my_text = '''與Scheme、Ruby、Perl、Tcl等動態型別程式語言一樣，
Python擁有動態型別系統和垃圾回收功能，能夠自動管理記憶體使用，
並且支援多種程式範式，包括物件導向、命令式、函數式和程序式程式。
其本身擁有一個巨大而廣泛的標準庫。'''
f.write(my_text)
f.close()

# --- read()
'''f = open('data.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()'''

# ------ page. 27 ------
# --- reading()
f = open('data.txt', 'r', encoding='utf-8')
print('{:3d}'.format(f.tell()), end=' ')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
    print('{:3d}'.format(f.tell()), end=' ')
f.close()

# --- seek()
f = open('data.txt', 'r', encoding='utf-8')
empty_line = []
while True:
    line = f.readline()
    if not line:
        break
    if len(str(line).strip()) == 0:
        empty_line.append(f.tell())

print('empty line :', empty_line)
f = open('data.txt', 'r+', encoding='utf-8')
for pos in empty_line:
    f.seek(pos-2)
    f.write('**************\n')

# ------ page. 28 ------
# --- print()
text = '''
What is a PEP?
**************
design
document providing information to the Python community, or describing
a new feature for Python or its processes or environment.  The PEP
should provide a concise technical specification of the feature and a
rationale for the feature.

'''
print(text,end='',file=open('print_out.txt', 'w', encoding='utf-8'))
print('ok')

# --- with
food_cal_list = [
    ['種類', '單位', '重量(g)', '熱量(卡)'],
    ['白米飯', '1碗', 205, 225],
    ['意大利肉醬麵', '1份', 248, 330],
    ['白吐司', '1片', 25, 75],
    ['全麥吐司', '1片', 25, 65],
    ['花生醬', '1湯匙', 16, 95],
    ['果醬', '1湯匙', 18, 50],
]

with open('food_cal.csv', mode='w', encoding='big5') as f:
    for line in range(len(food_cal_list)):
        text = str(food_cal_list[line])\
                    .replace('[', '').replace(']', '').replace('\'', '')+'\n'
        f.write(text)
    else:
        print('ok')

















