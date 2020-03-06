#n, o, p = 1, 2, 3456
#print(n, o, p)

#q = 'hello'+'python'
#print(q)

#a = 1
#b = 10
#c = 100
#del a
#print(a)
#print(type(a))
#print(id(a))

#b = 4.56
#print(b)
#print(type(b))
#print(id(b))

#A = 10
#print(id(A))
#A = A + 3
#print(A)
#print(id(A))

#W = ['MON', 'TUE', 'WND']
#W[2] = ['WED']
#W+= ['THU']
#print(W)

#L = [10, 20, 30]
#print(L)
#print(id(L))
#L[0] = 11
#print(L)
#M = L
#print(id(M))
#M[1] = 21
#print(M)
#print(L)
#print(id(L[0]))
#print(id(L[1]))
#print(id(M[1]))
#print(type(L))
#print(type(L[0]))

#L = [1,2,3,4,5,]
#a = 3
#print(a in L)
#b = 30
#print(b in L)
#M = L
#print(M is L)

#s = 'abcdefghijk'
#print(s[0:2])
#print(s[1:5])
#print(s[:])
#print(s[:4])
#print(s[:-1])
#print(s[-1])
#print(s.index('e'))
#print(s.count('a'))
#print(len(s))
#print('a' in s)

#a = [2, 3, 4]
#b = [6, 7, 8.5, "XYZ"]
#c = []
#d = [2, [a, b]]
#e = a + b
#x = a[1]
#print(x)
#print(b[1:3])
#print(d[1])
#print(d[1][0])
#print(d[1][0][2])
#b[0] = 4
#print(b)
#print(e)

#f = (2, 3, 4, 5)
#g = ()
#h = (2, [3, 4], (10, 11, 12))
#x = f[1]
#print(x)
#y = f[1:3]
#print(y)
#z = h[1][1]
#print(z)

#S1 = {1, 2, 3, 1, 1, 2, 3, 4, 5, 1}
#S2 = {5, 3, 2, 1, 2, 1, 4}
#print(S1)
#print(S2)
#print(S1 == S2)
#print(S1 is S2)

#D = {}
#D['G'] = "google"
#D['Y'] = "youtube"
#D['F'] = "facebook"
#print(D)
#print(D['G'])

#S3 = {'e', 'e', 'y', 'd', 's', 'a', 'd'}
#print(S3)

#Dic = {'a' : ['a', 'b', 'c'],
#      'b' : [1, 2, 3, 4],
#      'c' : [10, 20, 30, 40]}
#print(Dic['b'][2])

#a = 100
#print(type(a))
#print('test',a)
#a = str(a)
#print(type(a))
#print('test'+a)

#print(chr(65))

#input_args = eval(input("請輸入多個字,以逗號隔開"))
#print(str(input_args))
#print(type(input_args))

# ------ 作業 ------
# ------ 第一題 ------
S = 'abcdefghijklm'
print(S[8:])
# ------ 第二題 ------
z = 'abc'
print(z*5)
# ------ 第三題 ------
D = {}
D['010'] = "華僑銀行"
D['011'] = "上海銀行"
D['012'] = "台北富邦"
D['013'] = "國泰世華"
D['016'] = "高雄銀行"
D['017'] = "兆豐商銀"
D['018'] = "農業金庫"
D['021'] = "花旗銀行"
D['024'] = "運通銀行"
D['025'] = "首都銀行"
for i in D:
       print(i, D[i])
#print(D)

#S4 = {'一', '三', '六', '八', '一', '六', '七'}
#print(S4)
