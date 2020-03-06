# ------ page. 132 ------
Animals = ['Bat','Rat','Elephant','Cat']
print(Animals)

words = list("ABCDEFGH")
print(words)

pairs = ['('+str(i)+','+str(j)+')'
         for i in range(0,3) for j in range(0,4)]
print(pairs)

print()
# --- 第二題 ---
words = list('CAT')
print(words)

a_tuple = ('a', 'b', 'c')
print(list(a_tuple))

birthday = '1/6/1952'
blist = birthday.split('/')
print(blist)

splistr = 'a/b//c//d///e'
splitlist = splistr.split('//')
print(splitlist)

print()

# ------ page.133 ------
Animals = ['Bat','Rat','Elephant','Cat']

print(Animals[0])
print(Animals[1])
print(Animals[2])
print(Animals[-1])
print(Animals[-2])

numbers = [10, 11, 12, 13, 14, 15, 16, 17]

print(numbers[0:3])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

print()
# --- 第二題 ---
numbers = [[10, 11], [12, 13], [14, 15], [16, 17]]

print(numbers[0])
print(numbers[1])
print(numbers[0][1])
print(numbers[::2])
print(numbers[::2][1])
print(numbers[::2][1][0])

print()

# ------ page.134 ------
Animals = ['Bat','Rat','Elephant','Cat']

Animals[0] = 'Bull'
Animals[2] = 'Eagle'
print(Animals)

Animals[0:2] = ['', '']
print(Animals)

print()
# --- 第二題 ---
Animals = ['Bat','Rat','Elephant','Cat']

Animals.append("Dog")
print(Animals)

Animals.insert(1, 'Tiger')
print(Animals)

print()

# ------ page. 135 ------
Animals = ['Bat','Rat','Elephant','Cat']

Others = ['There','are']
Others.extend(Animals)
print(Others)
Others += '.'
print(Others)

print()
# --- 第二題 ---
Animals = ['Bat','Rat','Elephant','Cat']

for item in Animals:
    print(Animals.index(item))
print(Animals.index('Rat'))

print()

# ------ page. 136 ------
Animals = ['Bat','Rat','Elephant','Cat','Dog','Lion']

print(Animals)
Animals.remove('Elephant')
print(Animals)

del Animals[-1]
print(Animals)

print('pop:'+Animals.pop())
print(Animals)

print('pop:'+Animals.pop(1))
print(Animals)

print()
# --- 第二題 ---
Animals = ['Bat','Rat','Elephant','Cat']
seprator = ' , '
join_str = seprator.join(Animals)
print(join_str)
splitlist = join_str.split(',')
print(splitlist)

print()
# ------ page. 137 ------
char_list = ['A', 'A', 'B', 'C', 'B', 'A', 'B', 'A']
if 'A' in char_list:
    print('A Count:'+str(char_list.count('A')))
if 'B' in char_list:
    print('B Count:'+str(char_list.count('B')))
if 'C' in char_list:
    print('C Count:'+str(char_list.count('C')))
print('length of char_list:'+str(len(char_list)))

print()
# --- 第二題 ---
a_list = [6, 2, 5, 4, 3, 1]
print(a_list)

a_list.sort()
print(a_list)

a_list.sort(reverse=True)
print(a_list)

b_list = ['b', 'd', 'e', 'a', 'c', 'f']
b_list_sorted = b_list.copy()
b_list_sorted.sort()
print(b_list)
print(b_list_sorted)

print()
# ------ page. 138 ------
a_list = [1, 2, 4, 5, 6]
b_list = a_list
print(a_list)
print(b_list)
b_list[2] = 8
print(b_list)
print(a_list)
print('a_list id:'+str(id(a_list)))
print('b_list id:'+str(id(b_list)))

print()
# --- 第二題 ---
a_list = [1, 2, 4, 5, 6]
b_list = a_list.copy()
c_list = list(a_list)
d_list = a_list[:]

print(a_list); print(b_list); print(c_list); print(d_list)
b_list[2] = 10; c_list[2] = 20; d_list[2] = 30
print(a_list); print(b_list); print(c_list); print(d_list)
print('a_list id:'+str(id(a_list)))
print('b_list id:'+str(id(b_list)))
print('c_list id:'+str(id(c_list)))
print('d_list id:'+str(id(d_list)))

print()
# ------ page. 139 ------
city_name_tuple = ()
print(city_name_tuple)
print(type(city_name_tuple))

city_name_tuple = 'Taoyuan'
print(city_name_tuple)
print(type(city_name_tuple))

city_name_tuple = ('Taoyuan')
print(city_name_tuple)
print(type(city_name_tuple))

city_name_tuple = 'Taoyuan', 'Tokyo', 'New York', 'London'
print(city_name_tuple)
print(type(city_name_tuple))

city_name_tuple = ('Taoyuan', 'Tokyo', 'New York', 'London')
print(city_name_tuple)
print(type(city_name_tuple))

print()
# ------ page. 140 ------
number_tuple = 10, 30, 20, 40, 50, 10, 20, 30
print('值組中20的數量:', number_tuple.count(20))
for number in number_tuple:
    print(number, 'index:', number_tuple.index(number))
value_tuple = 1, 2, 3, 4
a, b, c, d = value_tuple
print(' a=', a, ' b=', b, ' c=', c, ' d=', d)

print()
# ------ page. 141 ------
custom_dict = {
    'Alice' : '0913001002',
    'Amy' : '0310123456',
    'John' : '0970033586',
    'Bob' : '0918845100'
}
print(custom_dict)

char_dict = {ch_index : chr(ch_index) for ch_index in range(80, 90)}
print(char_dict)

print()
# --- 第二題 ---
list_a = [[0, 0], [1, 1], [2, 2]]
dict_a = dict(list_a)
print(dict_a)

list_b = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'a3']]
dict_b = dict(list_b)
print(dict_b)

list_c = ['ab', 'cd', 'ef']
dict_c = dict(list_c)
print(dict_c)

tuple_d = 'ab', 'cd', 'ef'
dict_d = dict(tuple_d)
print(dict_d)

print()
# ------ page. 142 ------
fruits = ['Apple', 'Orange', 'Banana']
fruits_zh = ['蘋果', '橘子', '香蕉']
fruits_dict = dict(zip(fruits,fruits_zh))
print(fruits_dict)

print()
# --- 第二題 ---
custom_dict = {'Alice' : '0913001002', 'Amy' : '0310123456',
               'John' : '0970033586', 'Bob' : '0918845100'}
print(custom_dict['Bob'])
print(custom_dict.get('Alice'))
print(custom_dict.keys())
print(custom_dict.values())
print(custom_dict.items())

print()
# ------ page. 143 ------
custom_dict = {
    'Alice' : '0913001002',
    'Amy' : '0310123456',
    'John' : '0970033586',
    'Bob' : '0918845100'
}
print(custom_dict)
custom_dict['Amy'] = '0910123123'
custom_dict['Amber'] = '0910123456'
print(custom_dict)

print()
# --- 第二題 ---
custom_dict_1 = {'Alice' : '0913001002', 'Amy' : '0310123456',
                 'John' : '0970033586', 'Bob' : '0918845100'}
print('custom_dict_1筆數:',len(custom_dict_1))
custom_dict_2 = {'Ace' : '0913002002', 'Henry' : '0310123455',
                 'Johnson' : '0980033586', 'Dog' : '0918845200'}
print('custom_dict_2筆數:',len(custom_dict_2))
custom_dict_1.update(custom_dict_2)
print('custom_dict_1 更新後:',custom_dict_1)
print('custom_dict_1 更新後 筆數:',len(custom_dict_1))

print()
# ------ page. 144 ------
custom_dict = {'Alice' : '0913001002', 'Amy' : '0310123456',
                'John' : '0970033586', 'Bob' : '0918845100'}
print(custom_dict)
del custom_dict['John']
print('del John')
print(custom_dict)

print('pop :', custom_dict.pop('Amy'))
print(custom_dict)

print('popitem: ', custom_dict.popitem())
print(custom_dict)

custom_dict.clear()
print(custom_dict)

print()
# --- 第二題 ---
custom_dict = {'Alice' : '0913001002', 'Amy' : '0310123456',
                'John' : '0970033586', 'Bob' : '0918845100'}
if 'Amy' in custom_dict:
    print(custom_dict['Amy'])

print()
#  ------ page. 145 ------
custom_dict = {
    'Alice' : '0913001002',
    'Amy' : '0310123456',
    'John' : '0970033586',
    'Bob' : '0918845100'
}
dict_a = custom_dict
dict_b = custom_dict.copy()

dict_a['Bob'] =''
dict_b['Amy'] = ''

print('custom_dict', custom_dict)
print('dict_a', dict_a)
print('dict_b',dict_b)

print()
# ------ page. 146 ------
empt_set = set()
print(type(empt_set))

even_set = {0, 2, 4, 6, 8, 10, 0, 2, 4}
print(even_set)

odd_set = {1, 3, 5, 7, 9}
print(odd_set)

print()
# --- 第二題 ---
set_A = set('letters')
print(set_A)

set_B = set([10,15,20,20,30,40])
print(set_B)

set_C = set((10,15,20,20,30,40))
print(set_C)

set_D = set({'a': 10, 'b': 20, 'c': 30})
print(set_D)

print()
# ------ page. 147 ------
set_A = {2, 8, 10, 22, 11, 12}

set_A.add(25)
print(set_A)

set_A.remove(2)
print(set_A)

set_A.discard(2)
print(set_A)

set_A.discard(8)
print(set_A)

#set_A.remove(8)
#print(set_A)

print()
# --- 第二題 ---
set_A = {2, 8, 10, 22, 11, 12}
set_B = {6, 7, 10, 11, 15}
set_C = {8, 12}

print('set_A 交集 set_B',set_A.intersection(set_B))
print('set_A 聯集 set_B',set_A.union(set_B))
print('set_A 差集 set_B',set_A.difference(set_B))
print('set_A 與 set_B 對稱差',set_A.symmetric_difference(set_B))
print('set_C 是 set_A 的子集嗎?',set_C.issubset(set_A))

print()
# ------ page. 148 ------
set_A = {2, 8, 10, 22, 11, 12}
set_B = {6, 7, 10, 11, 15}
set_C = {8, 12, 22}

if set_C & set_B:
    print(len(set_C & set_B))
else:
    print('0')

if set_C & set_A:
    print(len(set_C & set_A))
else:
    print('0')

print()
# ------ 作業 ------
# ------ 第一題 ------
custom_dict = {'Alice' : '0913001002', 'Amy' : '0310123456',
               'John' : '0970033586', 'Bob' : '0918845100'}
print(sorted(custom_dict.items()))

print()
# ------ 第二題 ------
names = ['Mary', 'Tom', 'John', 'Kevin']
seprator = ' / '
join_str = seprator.join(names)
print(join_str)