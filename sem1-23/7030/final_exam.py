# # var = (0 < 2 < 4 and not 3 > 0 > 1)
# # print(var)
# #
# #

# a = 12 + 4.2 // 2
# print(a)
#
# b = -1<= -1 >= -2
# print(b)
#
# c = 5 % -3
# print(c)
#
# d = bool(not('c') and 'b')
# print(d)
#
# e = 'hard to work'.split()[-1]
# print(e)
#
# for i, c in enumerate(['to', 'do']):
#     print((c, i))
#
# def route():
#     t = 0
#     r = int(input('number'))
#     while r != 0:
#         if r // 5 ==0:
#             t += r
#         r = int(input("number"))
#     return t
#
# # print(route())
#
# s1 = 'strategic initiative'
# s2 = s1[-17:6]
# print(s2)
#
# def g():
#     w.append(9)
#
# w = [4, 6]
# g()
# print(w)
#
# d1 = {1:'c', 2:'d', 3:'e'}
# d2 = d1.update({4:['f']})
# print(d2)
#
# a = 1
# b = 2
# while a < 3:
#     a *= b
#     b += 1
# print(a)
#
# # x = [10, 20 ,30 ,40]
# #
# # i = 0
# # j = 0
# # for p in x:
# #     i += p
# #     j += 1
# # print(i / j)
# f = lambda x, y : x - y
# g = lambda x : x*2
# zs = [g(x) for x in [1,2,3] if f(x,2)]
# print(zs)
#
# d = {'Brown' : {'ID': 732, 'Orders': ['chisel', 'spanner']},
#    'Black': {'ID': 461, 'Orders':
#    ['lathe', 'crowbar']}}
# x = d.get('White',{}).get('Orders',[])
# print(x)
#
# d = {'Brown' : {'ID': 732, 'Orders': ['chisel', 'spanner']},
#    'Black': {'ID': 461, 'Orders':
#    ['lathe', 'crowbar']}}
# x = d.get('Brown',{}).get('Orders',[]).append('hammer')
# print(x)
#
# # def product(xs):
# #     (a, b) = ###
# #     if len(xs) == a:
# #         return b
# #     return xs[0] * product(xs[1:])
# #
# # print(product([1,2,3]))
# #
# # print(len([]))
#
#
#
# class A(object):
#     def __init__(self, x):
#         self._x = 2 * x
#     def m1(self, x):
#         return self.m2(x) + 2
#     def m2(self, x):
#         return x - 1
# class B(A):
#     def m2(self, y):
#          self._y = y
#          return self._x + self._y
# class C(B):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self._y = y + 2
#     def m1(self, x) :
#         return self._x + self._y
# class D(B):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self._x += y
#         self._y = y + 2
#     def m1(self, y):
#         return self._y + y
#     def m2(self, x):
#         return super().m2(x) - x
# a = A(1)
# b = B(2)
# c = C(1, 1)
# d = D(2, 1)
#
# print(a.m1(2))
# print(b.m2(1))
# print(c.m2(3))
# print(d.m1(3))
# print(d.m2(1))
#
#
# import tkinter as tk
import readline

from pandas._libs import join


# class ButtonsFrame(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         b1 = tk.Button(self, text="A")
#         b2 = tk.Button(self, text="B")
#         b1.pack()
#         b2.pack()
#
# class MainWindow(object):
#     def __init__(self, root):
#         self.root = root
#         label = tk.Label(root, text="Buttons")
#         label.pack(side=tk.LEFT,expand=True)
#         bf = ButtonsFrame(self.root)
#         bf.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# root = tk.Tk()
# window = MainWindow(root)
# root.mainloop()
# def foo(n:int,xs:list[int])->list[int]:
#     i, ys = 0, []
#     for k, x in enumerate(xs[:n]):
#         ys.append((n-k-i, xs[i]))
#         i += 1
#     return ys
#
# print(foo(0, list(range(4,9))))

# s = 'the brown fox jumped'
# s = s[::-1]
# print(s)
# x=s[:-4:-1]
# print(x)

# xs=['a',(3,4),{1:'b'}]
# ys=xs
# ys[2]={2:'c'}
# z=xs[2]
# print(z)
#
# print((2,3) + (3,))

# def foo(ys):
#     for y in ys:
#         if y in 'aeiou':
#             return True
#         elif y not in 'aeiou':
#             return False
#     return -1

# print(foo())

#
# a = [1, '2', 3, 'fout']
# print(a)
# a = [1, int(2), 3, 4.0]
# print(a)
# a = [1, int(2), True, [True, False]]
# print(a)

# xs = [1,2,3,4,5]
# p = xs[:-1]
# xl = 'abc asd ttt hhh'.split()
# print(p)
#
# def foo(a, b):
#     a = 2
#     b.append(3)
# a= 1
# b =[]
# foo(a, b)
# print(a,b)
#
# def foo(x, xs):
#     return x in xs
# print(foo('', ' '))

# s1 = "Monty"
# s2 = "Python"
# s3 = "Spam"
# s3 = s1
# print(s3)
# s3 = "Parrot"
# print(s3)
# s4 = s1 + s2
# print(s4)
# x = ['a', 0, 'b']
# y=x
# y[2] = 0
# x = (1, 2)
# x += (3, 4)
# print(x)
#
# d = {'CA': 'Maple Syrup', 'AU': 'Vegemite',
#      'NZ': 'Pavlova', 'FR': 'Escargot'}
# d['SP'] = 'Churro'
# d.get('JP', 'Sushi')
# print(d)
#
# x=0
# if x == 0:
#     print("zero")
# elif x >= 0:
#     print("positive")
# elif x <= 0:
#     print("negative")
#     print(x)
#
#
# def f(x: int) -> None:
#     if x <= 0:
#         raise ValueError("value must be positive")
#     while x > 0:
#         print(x, end=',')
#         x -= 1
# try:
#     f(-5)
# except ValueError as e:
#     print(str(e))
# def g(w):
#     w = w+25
#     return w
# w=40
# a = g(w)
#
# print(a)
#
#
# def g(x):
#     if x == 1:
#         return 1
#     x -= 1
#     return g(x - 1) * x
#
# print(g(3))
#
#
# s1 = 'ode to grogramming'
# s2 = s1[-7:-10:-1]
# print(s2)
#
# g = lambda u,v: u+v
# vs = 'trot'
# z = [g(u,v) for u in 'same' if u not in 'amps' for v in vs]
# print(z)
# z = 'ministry of silly walk'
# z = '-----'.join(z.split('silly'))
# print(z)
#
# def foo(xs:list):
#     if not xs:
#         return [[]]
#     else:
#         ys = foo(xs[1:])
#         x = xs[0]
#     return [y + [x] for y in ys] + ys
# ans=foo([1,2,3])
# print(ans)
#
#
# def foo(f_path: str) -> bool:
#     # min_numbers = []
#     with open(f_path, 'r') as file:
#
#         min_numbers = [min([int(number) for number in line.strip().split()])
#                            for line in file.readlines()]
#     if len(set(min_numbers)) != len(min_numbers):
#         return False
#     else:
#         if sorted(min_numbers) == min_numbers:
#             return True
#         else:
#             return False
# print(foo('number.txt'))

# a = {1:'b', 2:'c'}
# # for i in a:
# a[3] = 'c'
# print(a)
#
# for i, j in a.items():
#     print(j)
# import random
# xs=[1,2,3,4]
# new_list=[(x,random.random()) for x in xs]
# new_list.sort()
# z=[ (y,y) for y,x in new_list]
# print(z)

# import tkinter as tk
# root = tk.Tk()
# b1 = tk.Button(root, text= "A")
# b2 = tk.Button(root, text = "B")
#
# b1.pack(side=tk.LEFT, fill=tk.BOTH)
# b2.pack(side=tk.LEFT, fill=tk.Y)
# root.mainloop()
# s1 = "Hello"
# s2 = "World"
# s3 = "Ni Hao"
# s3 = s1
# print(s1)
# print(s3)
# s3 = "Hi"
# print(s3)
# s4 = s1 + s2
# print(s4)
#
# x = [1, 2, 3]
# x.pop(1)
# y=x.extend([4, 5, 6])
#
# x.pop(3)
# print(x)
#
# x=0
# stars = '*'
# while x > 0 :
#     print(stars)
#     stars += '*'
#     x -= 1

# a = list(('a' , 'b') + (1, 2,))
# print(a)
# print(5!=4)
# v = (['a', 'b'],[ 'c', 'd'])
# x,y = v
# print(x,y)
# z=y
# z[-1] = 3
# print(y
# def foo(file: str):
#     min_number = []
#     with open (file, 'r') as files:
#         lines = files.readlines()
#     for line in lines:
#         line = line.strip().split()
#         number = [int(numbers) for numbers in line]
#         min_number.append(min(number))
#     if len(min_number) != len(set(min_number)):
#         return False
#     else:
#         if sorted(min_number) != min_number:
#             return False
#         else:
#             return True
# print(foo('number.txt'))
#
# a = 'abcdefg'
# b = a[0::-1]
# print(b)
# xs=['a',(3,4),{1:'b'}]
# ys=xs
# ys[2]={2:'c'}
# z=xs[2][2]
# print(z)

# def f(l, a, b):
#     l.append(a)
#     l = l + [b]
#     print(x)
#
#
#     return l
# x = [5, 9]
#
# x = f(x, 2, 1) + x
# print(x)

# def g(y):
#     y+=25
#     return y
# y=40
# g(y)
# print(y)

# class A():
#     def __init__(self, x):
#         self.x = x
#         self.y = 3
#     def f(self, x):
#         return 2*x
#     def g(self, x):
#         return self.f(self.y)
#
# class B(A):
#     def __init__(self,x, y):
#         super().__init__(x)
#         self.y = y
#
#     def f(self, x):
#         return A.f(self, self.y) + x
# class C(B):
#     def __init__(self, x):
#         super().__init__(x, 5)
#     def h(self):
#         return self.g(self.y) + super().f(self.x)
#
# class D(C):
#     def __init__(self, x, y, z):
#         super().__init__(x)
#         self.y += 5
#         self.z = z
#     def g(self, x, y, z):
#         return x*y*z + self.x +self.y+self.z
#
# a = A(1)
# b = B(1, 2)
# c = C(3)
# d = D(4, 5, 6)
#
# print(a.g(5))
# print(b.f(4))
# print(c.h())
# print(d.g(1,2,3))

# d = {'Brown' : {'ID': 732, 'Orders': ['chisel', 'spanner']},
#    'Black': {'ID': 461, 'Orders':
#    ['lathe', 'crowbar']}}
# d.get('Brown',{}).get('Orders',[]).append('hammer')
# x = d.get('Brown').get('Orders')
# print(d)
# print(x)
#
# x = input("ooooo")
# y = input('pppppp')
# print(f'{x+y}')
# def foo(x,y):
#     return  x/y
# print(type(foo(1,2)))