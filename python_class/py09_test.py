# python_09

# 字串操作與正規表示式
#本章內容
#字串操作
#正規表示式及re模組

# 2019/12/15上課內容
# 150上頁 字串的建立
str_a = 'PEP is Python Enhancement Proposals'
print(str_a) # 單引號

str_b = "This is a Python string"
print(str_b) # 雙引號

# str_c = '''Python Weekly is a free weekly newsletter featuring curated news, articles, new release, jobs, etc.'''
# print(str_c) # 三個單引號

# str_d = """Python Weekly is a free weekly newsletter featuring curated news, articles, new release, jobs, etc."""
# print(str_d) # 三個雙引號

# 150下頁 字串與轉義字元
# 參考資料 https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/366541/
print('字串結合\\n_換行: ')
print("This is first string.\nThis is second string.\nThis is third string.\n")

print('字串結合\\n\\t_換行+橫向製表(縮排): ')
print("This is first string.\tThis is second string.\n\tThis is third string.\n")

print('字串結合反斜線_字串加單引號/雙引號: ')
print("\'This is first string.\'\n\'This is second string.\'\n\'This is third string.\'.\n") # 字串結合\' 或 \"

print('字串結合雙反斜線_字串前加一個反斜線: ')
print("\\This is first string.\n\\This is second stri.\n")

print('字串結合\\r_回到第一行: ')
print("This is first string.\rThis is second string.\rThis is third string.\n")

# 151上頁 轉換成字串
a = 100.05 ; b = 20
print(a+b) # 數值轉字串

#a = str(a)
#print(a+b) # 字串無法計算

a = [10,20,30]
print(str(a)) # 串列轉字串

a = (10,20,30)
print(str(a)) # 值組轉字串

dict_a = {0: 'apple', 1: 'orange', 2: 'mango'}
print(str(dict_a)) # 字典轉字串

set_a = {10,20,30}
print(str(set_a)) # 集合轉字串

# 151下頁 字串的連接與重複
print("This is a " + "Python string.") # 字串連接
print("it's important! \n" *3) # 字串重複

print("")
a = 100.05 ; b = 20
print('a=' +str(a)+' b='+str(b)) #數值與字串連接

print("")
list_a = [10,20,30]
str_a =''
for item in list_a:
    str_a =str_a +' '+str(item)
print(str_a) # 串列串連接

print("")
dict_a = {0:'apple',1:'orange',2:'mango'}
for i in range(len(dict_a)):
    print("Item", i,":"+(" "+dict_a[i]*3)) # 字典與字串連接與重複

# p152上頁 字元擷取與切片
# 使用[]與[:]
# 字元擷取
str_t = "\ 'This is a Python string.\'"


# p152上頁 字元擷取與切片
# 使用[]與[:]
# 字元擷取
str_t = "\ 'This is a Python string.\'"
print(str_t)
for i in range(len(str_t)):
    print("str_t[",i,"] = ",str_t[i])

# 序列切片
print(str_t[1:])
print(str_t[:10])
print(str_t[10:17])
print(str_t[17:])
print(str_t[:10]+str_t[17:])
print(str_t[::3])

# p152下頁 字串分割與結合
str_t = "This is a Pythone string."
print(str_t.split()) # 使用 split與空白分割字串

str_p = "Alice , Joe , Bob , Kent , Zoey"
print(str_p.split(',')) # 使用 split與逗號分割字串

print('/'.join(str_p.split(','))) # 使用 join把字串插入串列

str_a = '''Python can be easy to pick up whether you\'re a first time programmer or you\'re experienced with other languages.'''
print(str_a.split('\n')) # 使用 split與換行符號\n分割字串

print('\t'+'\n\t'.join(str_a.split('\n'))) # 使用 join把 \t\n取代\n換行的間隔

# p153上頁 字串的大小寫與對齊方式
# p153上頁 字串的大小寫與對齊方式
str_p = "alicE, joE, boB, kenT, zoeY"
print(str_p.lower()) # 轉成小寫
print(str_p.upper()) # 轉成大寫
print(str_p.title()) # 轉title(第一個字母大寫)
str_t = "python is powerful and fast"
print((str_t.capitalize())) # 轉標題(句字的第一個字母大寫)

str_s = ('Hello')
print(('\''+str_s.rjust(20)+'\'')) # 字串靠右對齊
print(('\''+str_s.ljust(20)+'\'')) # 字串靠左對齊
print(('\''+str_s.center(20)+'\'')) # 字串置中對齊

# p153下頁 刪除字串首尾的字串
str_t = '          [Pyton is easy]          '

# 刪除左右的空白
print('\''+str_t.lstrip()+'\'') # 刪除左邊的空白
print('\''+str_t.rstrip()+'\'') # 刪除右邊的空白
print('\''+str_t.strip()+'\'') # 刪除所的空白

# 沒有刪除空白,無法刪除左右特定字元
print(str_t.strip('[').strip(']'))

# 刪除特定字元
str_m = str_t.strip().strip('[').strip(']')
print(str_m)

# 老師的範例
print("")
print(str_t.lstrip())
print(str_t.rstrip())
print(str_t.strip())
print(str_t.strip().strip('[').strip(']'))

print()
# p154上頁 字串的尋找與取代
str_p = 'Python is easy to learn, and simple to use.'

# 尋找特定字串
print(str_p.find('to')) # 回傳索引值
print(str_p.rfind('to')) # 回傳索引值(從右邊找)
print(str_p.count('to')) # 統計 特定字串出現的次數

str_m = str_p.replace('to', '', str_p.count('to')) # 取代特定字串

# 特定否存在字串中
print("to" in str_m) # to是否有在字串中
print(str_m)
print('to' not in str_m) # to是否沒有在字串中

# 是否以特定字串開始或結束
print(str_p.startswith('Python')) # 是否以'Python'為開頭字
print(str_p.endswith('.')) # 是否以'.'為結尾字

print()
# p154下頁 字串的檢查
def input_check(input_str):
    print('\n')
    print(input_str)
    print('is space: ', input_str.isspace())
    print('is a numberic or alph: ', input_str.isalnum())
    print('is numberic: ', input_str.isnumeric())
    print('is decimal: ', input_str.isdecimal())
    print('is digit: ', input_str.isdigit())
    print('is alpha: ', input_str.isalpha())
    print('is lower: ', input_str.islower())
    print('is upper: ', input_str.isupper())
    print('is title: ', input_str.istitle())
    print('is ascii: ', input_str.isascii())

#input_check('ABC')
#input_check('123456')
#input_check('!!2344abc')
#input_check('100.01')
#input_check('')
#input_check('　')

print()
# ------ page. 158 ------
import re
ret_match = re.match(r'^\d{4}-\d{2}-\d{2}$', '1988-07-25')

if(ret_match):
    print('ret_match:', ret_match)
    print('ret_match:', ret_match.group())
else:
    print('ret_match:None')

ret_match = re.match(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', '1988-07-25')

if(ret_match):
    print('ret_match:', ret_match.groups())
    print('ret_match:', ret_match.group())
    print('ret_match:', ret_match.group(1))
else:
    print('ret_match:None')

print()
# ------ page. 159 ------
import re
input_str = "Terry, 1983-04-04, Marry, 1985-07-22, Joe, 1978-05-22"
ret_search = re.search(r'\d{4}-\d{2}-\d{2}',input_str)

if(ret_search):
    print("ret_search", ret_search)
    print("ret_search", ret_search.group())
else:
    print('ret_search:None')

ret_search = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', input_str)
if(ret_search):
    print("ret_search", ret_search.groups())
    print("ret_search", ret_search.group())
    print("ret_search", ret_search.group(1))
    print("ret_search", ret_search.group(2))
    print("ret_search", ret_search.group(3))
else:
    print('ret_search:None')

print()
# ------ 第二題 ------
import re
input_str = "amy,amylee@yahoo.com,robert,robert_wang@gmail.com,martin, \
            martin.chen@outlook.com"
ret_match = re.findall(r'[a-zA-Z0-9\._]+@[a-zA-Z0-9\._]+',input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")

print()
# ------ page. 160 -----
import re
input_str = "A running <div>dog</div> rams a walking <div>pig</div>.";
ret_match = re.findall(r'<div>(.*)</div>',input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")

ret_match = re.findall(r'<div>(.*?)</div>',input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")

print()
# ------ 第二題 ------
import re
input_str = '(1) Jack Wu (2) Jay Chou (3) JJ Lin'
ret_match = re.split(r'\(\d\)',input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")

print()
# ------ page. 161 ------
import re
input_str = "a001.jpg, b02.gif, aacc0908.jpg, aaajpg"
ret_match = re.sub(r'.(gif|jpg)', '.png', input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")
# --- 更好的寫法.抓得更加精準 ---
r = re.sub(r'\.(gif|jpg)', '.png', input_str)
print(r)

print()
# ------ 第二題 ------
import re
input_str = "amy,amylee@yahoo.com,robert,robert_wang@gmail.com,martin, \
            martin.chen@outlook.com"
email_regx = re.compile(r'[a-zA-Z0-9\._]+@[a-zA-Z0-9\._]+')
ret_match = email_regx.findall(input_str)
if ret_match:
    print(ret_match)
else:
    print("ret_match:None")

print()
# ------ 作業 ------
s = 'alice, joe, bob, kent, zoey'
str = s[::-1]
print(str)
y = str.title()
print(y)
print(y[::-1])

str = 'Python is easy to learn, easy to write and simple to use.'
a = str.find('to')
a1 = a + 1
print(str.index('to'), str.index('to', a1), str.rindex('to'))





