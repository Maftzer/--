# def f():
#     s = '-- Inside f()'
#     print(s)
# print('Before calling f()')
# f()
# print('After calling f()')

# def f(qty = 6, item = 'bananas', price = 1.74):
#     print(f'{qty} {item} cost ${price:.2f}')
# f()

# def f():
#     print('foo')
#     print('bar')
#     return
# f()

# def f(x):
#     if x < 0:
#         return
#     if x >100:
#         return
#     print(x)
# f(-3)   # nqma da printira
# f(105)  # nqma da printira
# f(64)    

# def f():
#     return 'foo'
# s = f()
# print(s)

# def psum(*k):
#     result=0
#     for i in k:
#         result+=i
#     return result
# s = psum(1,2,3,4)
# print(s)   

# num = 10
# L = lambda n: 2*n+1
# for i in range(num):
#     print(L(i), end = ' ')
# for k in range(num):
#     print((lambda x:x*x) (k+1), end = ' ')

def func():
    global var1
    var1 = 10
    var1 = 5
    print(var1)
func()
print(var1)

