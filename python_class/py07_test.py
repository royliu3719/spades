#def f1(x, y):
#    a = x + y
#    return a

#def f2(x, y):
#    a = x - y
#    return a

#def f3(x, y):
#    a = x * y
#    return a

#d = f3(3, 4)
#print(d)

#d = f1('hello','python')
#print(d)
# ------ page. 112 ------
#def function_return_multiple():
#    a = "Hello"
#    b = 10
#    c = 20
#    d = 30
#    return a,b,c,d
#print(function_return_multiple())
# ------ 第二題 ------
#def main():
#    print("This is main function called")
#    sub_function(10, 20)
#def sub_function(p1, p2):
#    print('Received value para1={}para={}'.format(p1, p2))
#if __name__=="__main__":
#    main()

# ------ page. 114 ------
# --- 參數為lmmutable物件 ---
#def main():
#    b = "我是B"
#    f1(b)
#    print(b)
#    b = f2(b)
#    print(b)
#def f1(a):
#    a = "我是A"
#def f2(a):
#    a = "我回傳的是A"
#    return a
#if __name__=="__main__":
#    main()
# --- 參數為mutable物件 ---
#def main():
#    b = ["我", "是", "B"]
#    print(b)
#    f(b)
#    print(b)
#def f(a):
#    a[0] = "換"
#    a[1] = "成"
#    a[2] = "A"
#if __name__=="__main__":
#    main()

# ------ page. 116 ------
# ------關鍵字引數------
#def f1(a = 0, b = 0):
#    c = a + b
#    print(c)

#def main():
#    f(11, 10)
#    f1(b = 10,a = 11)
# ------- 參數預設值 ------
#def f2(a, b, c = 10, d = 11):
#    c = a + b + c + d
#    print(a, b, c, d)

#def main():
#    f1()
#    f1(1,2)
#    f2(5, 4)
#   f2(1, 2, 3, 5)

#if __name__=="__main__":
#    main()

# ------ page.117 ------
# --- 不定長度參數 ---
# --- 第一題 ---
#def main():
#    print_info(10,20,30,40)

#def print_info(para1, *var_tuple):
#    print(para1)
#    print(var_tuple)
#    print(var_tuple[-1])

#if __name__=="__main__":
#    main()
# --- 第二題 ---
# --- 使用兩個** ---
#def main():
#   print_info(50,a = 10, b = 20)

#def print_info(para1, **var_dict):
#   print(para1)
#    print(var_dict)

#if __name__=="__main__":
#    main()
# --- 第三題 ---
#def print_info(para1, *var):
#    print(para1)
#    print(var)
#    print(var[1])
#print_info(10, 20, 30, 40, 50)
# --- 第四題 ---
#def print_info1(para1,a=0,b=0,c=0):
#    print(para1)
#    print(a,b,c)
#d = {'a':10,
#     'b':20,
#     'c':30
#    }
#print_info1(5,**d)
# --- 第五題 ---
#def print_info2(para1, **var):
#    print(para1)
#    print(var)
#print_info2(10, a = 20, b = 30, c = 40, d = 50)

# ------ page. 118 ------
# ---- 巢狀函式 ----
# --- 用除錯一步步跑 ---

# ------ page. 119 ------
# --- 非區域變數的兩種比較 ---

# ------ page . 120 匿名函式 ------
#AVG = lambda arg1, arg2: (arg1 + arg2)/2
#print("平均值:", AVG(10, 20))
#print("平均值:", AVG(20, 20))
#AVG = lambda arg1, arg2, arg3: arg1 * arg2 - arg3
#print(AVG(8, 11, 1))
# ------ yield ------
#def main():
#    print(list(my_range(8)))
#    g = my_range(8)
#    next(g)
#    next(g)
#    print(next(g))
#def my_range(n):
#    x = 0
#    while True:
#        yield x
#        x += 1
#        if x == n:
#            break
#if __name__ == "__main__":
#    main()

# ------ page. 121 ------
#import logging
#def use_logging ( fun ):
#    def wrapper ():
#        logging.warning(" %s is running" % fun . __name__ )
#        return fun()
#    return wrapper
#@use_logging
#def function_a():
#    print('function_a is called')
#@use_logging
#def function_b():
#   print('function_b is called')
#function_a()
#function_b()
# --- 老師補充 ---
#def my_deco ( func ):
#    def wrapper_func (*args):
#        print('### {} is going to run ###'.format(func.__name__))
#        func(*args)
#        print('### {} is going to run ###'.format(func))
#    return wrapper_func
#@my_deco
#def function_a(s):
#    print(s)
#@my_deco
#def function_b(a,b):
#    print(a+b)
#function_a('Hello! I am Function A.')
#function_b(1,2)

# ------ page. 123 ------
#def main():
#    L = [10,20,30,40,50,60]
#    print(L[2:-1])
#    print(sum(L[2:-1],3))
#if __name__ == "__main__":
#    main()

# ------ page. 125 ------
#week_day = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#for day in iter(week_day):
#    print(day)
#for i in range(len(week_day)):
#    print(week_day[i])
#for day in iter(list(reversed(week_day))):
#    print(day)
#it = iter(week_day)
#print(next(it))
#print(next(it))
#print(next(it))


#def add_ten(x):
#    x += 10

#def add_ten_r(x):
#    return x+10

#def main():
#    L = [1,2,3,4,5,6]
#    M = map(lambda x : x * 10, L)
#    print(M)
#    print(list(M))

#    N = list(map(add_ten, L))
#    print(N)
#    N = list(map(add_ten_r, L))
#    print(N)

#if __name__ == "__main__":
#    main()

# ------ page. 126 ------
#def main():
#    L = []
#    M = [1, '', 2, 0]
#    print(any(L))
#    print(any(M))
#    print(all(M))

#if __name__ == "__main__":
#    main()

# ------ page. 128 ------
#def main():
#    x = 10
#    s1 = 'x+3'
#    s2 = 'pow(2, 3)'
#    s3 = '1, 2, 3, 4'
#    print(eval('3*x'))
#    print(eval('pow(2, 2)'))
#    print(eval(s1))
#    print(eval(s2))
#    print(eval(s3))
#if __name__ == "__main__":
#    main()
# --- 第二題 ---
#def main():
#    exec('print("Hello World")')
#    exec("""for i in range(5): print("iter time:%d" %i) """)
#    print('\n')

#    str = "for i in range(5): print(\"iter time: %d\" %i)"
#    c = complie(str,'','exec')
#    exec(c)

#if __name__ == "__main__":
#    main()


# ------ 作業 ------
def main():
    #print(list(my_range(10)))
    g = my_range(10)
    #next(g)
    for i in range(0, 10):
        print(next(g))

def my_range(x):
    c = 0
    a = 0
    b = 1
    while c < x:
            yield b
            c += 1
            a, b = b, a + b


if __name__ == "__main__":
    main()


#a = 0
#b = 1
#(a, b)= (b, a + b)
#print(a, b)


# --- 另一種寫法 ---
# --- 不能有任何條件,直接表達費是數列的意思 ---
a = [0, 1]
for b in range(0, 10):
    b = (a[-2] + a[-1])
    a.append(b)
print(a)

