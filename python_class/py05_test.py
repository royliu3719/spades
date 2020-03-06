#A = input("請輸入一個整數")
#C = int(A)
#if (C > 100) and (C % 2 == 0):
#    print("您輸入的整數超過100")
#   print("您輸入的是 : " + A)
#    print("bbbbbb")
#print("您輸入的是", C)

#A = input("請輸入一個整數")
#C = int(A)
#if (C % 2) == 0 :
#    print(C, "是偶數")
#else:
#    print(C, "是奇數")

#A = int(input("請輸入數字A:"))
#B = int(input("請輸入數字B:"))
#if A == B:
#    print('數字A等於數字B')
#elif A < B:
#    print('數字A小於數字B')
#else :
#    print('數字A大於數字B')

#sites = ["Facebook", "Google", "Amazon", "Twitter", "Youtube", "Yahoo"]
#print(sites.index("Twitter"))
#for site in sites:
#    print("編號", sites.index(site), "站台" + site)
#print("完成python for Loop")

#a = list(range(10))
#print(a)
#for i in range(10):
#    print(i)

#sites = ["Facebook", "Google", "Amazon", "Twitter", "Youtube", "Yahoo"]
#for i in range(len(sites)):
#    print("編號", i, "站台" + sites[i])
#    if sites[i] == 'Amazon':
#      break
#print('\n')

#sites = ["Facebook", "Google", "Amazon", "Twitter", "Youtube", "Yahoo"]
#print(len(sites))
#for r in range(6):
#   print(r)
#for r in range(len(sites)):
#   print(r, sites[r])
#for r in range(2, 5):
#    print(r)
#for i in range(2, 5):
#   print(i, sites[i])

#L = [10, 20, 30, 40, 50]
#for site in L:
#    print("L", [L.index(site)], '=', site)

#L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for item in L:
#    if item == 7:
#        continue
#    print(item)
#for item in L:
#    if item == 7:
#        pass
#    print(item)

#for n in range(2, 20):
#    for x in range(2, n):
#        if n % x == 0:
#            print(n, '可被', x, '整除')
#            break
#    else:
#        print(n, '是質數')

#print([x * 2 + 10 for x in range(10)])
#print([x for x in range(10) if x % 3 == 0])

# ------ 作業 ------
# ------ 第一題 ------
#for n in range(0, 101):
#   for x in range(2,3):
#        if n % x == 0:
#            print(n)
#            break
# ------ 第二題 ------
#D = {'台北市中正區': 100, '台北市大同區': 103, '台北市中山區': 104, '台北市松山區': 105, '台北市大安區': 106, '台北市萬華區': 108, '台北市信義區': 110}
#A = input("請輸入區名")
#if A in D:
#    print("郵遞區號:", D[A])
#else:
#    print('看不懂中文喔?')
# ------ page. 95 ------
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name =='':
        break

    if name in birthdays:
        print(birthdays[name] , 'is the birthday of', name)
    else:
#        print('I do not have birthday information for', name)
#        print('What is their birthday ?')
        bday = input()
        birthdays[name] = bday
#        print('Birthday Data updated.')

