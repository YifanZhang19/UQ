# import tkinter as tk
# from tkinter import messagebox
# from a3 import *
#
#
# # root = tk.Tk()
# # root.title('test function')
# # root.geometry('400x200')
# # button = tk.Button(root, text='click me!')
# #
# # button.pack()
# #
# #
# # def flower(b):
# #     messagebox.showinfo("wow", 'Isis')
# #     print("abc")
# #
# #
# # button.bind("press", flower)
# # root.mainloop()
# # class Application(tk.Frame):
# #     def __init__(self, master=None):
# #         super().__init__(master)
# #         self.master = master
# #         self.pack()
# #         self.createWidget()
# #
# #     def createWidget(self):
# #         # self.button1 = tk.Button(self, text='click me', command=self.fuuu)
# #         # self.button1.pack()
# #         #
# #         # self.exitBu = tk.Button(self, text='quit', command=root.destroy)
# #         # self.exitBu.pack()
# #     #     self.label1 = tk.Label(self, text='woooooow', width=10, height=10,
# #     #                            bg='blue', fg='white')
# #     #     self.label1.pack()
# #     #
# #     #     # global photo
# #     #     # photo = tk.PhotoImage(file='a3 2/images/grass.png')
# #     #     # self.label2 = tk.Label(self, image=photo)
# #     #     # self.label2.pack()
# #     #     self.button = tk.Button(self, text='abc', width=10, height=10)
# #     #     self.button.pack()
# #     #     self.button.config(anchor='n')
# #     # def fuuu(self):
# #     #     tk.messagebox.showinfo('title', 'woooooooooo!')
# #         self.label1 = tk.Label(self, text='user')
# #         self.label1.pack()
# #         v1 = tk.StringVar()
# #         self.entry1 = tk.Entry(self, textvariable=v1)
# #         self.entry1.pack()
# #         v1.set('admin: ')
# #
# #         self.label2 = tk.Label(self, text='password')
# #         self.label2.pack()
# #         v2 = tk.StringVar()
# #         self.entry2 = tk.Entry(self, textvariable=v2, show='*')
# #         self.entry2.pack()
# #         v2.set('password: ')
# #
# #         self.button = tk.Button(self, text='log', command=self.login)
# #         self.button.pack()
# #     def login(self):
# #         print('user:' + self.entry1.get())
# #         print('password:' + self.entry2.get())
# #
# #         tk.messagebox.showinfo('welcome', 'woooow!')
#
# ground = read_map(map_file="/Users/meviusz/UQ/7030/a3/a3 2/maps/map1.txt")
# print(ground)
# cache = {}
# for row in range(len(ground)):
#     for col in range(len(ground[row])):
#         image = None
#         if ground[row][col] == 'G':
#             image = '/Users/meviusz/UQ/7030/a3/a3 2/images/grass.png'
#         elif ground[row][col] == 'S':
#             image = '/Users/meviusz/UQ/7030/a3/a3 2/images/soil.png'
#         elif ground[row][col] == 'U':
#             image = '/Users/meviusz/UQ/7030/a3/a3 2/images/untilled_soil.png'
#         if image:
#             if image not in cache:
#                 cache[image] = get_image(cache[image], (50, 50))
#             pic = cache[image]
#             tk.create_image(col * 50, row * 50, image=pic, anchor='nw')
#
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.geometry('400x200')
#     root.title('Test')
#     # app = Application(master=root)
#     root.mainloop()
# import tkinter as tk
#
# root = tk.Tk()
#
# root.geometry('400x200')
#
# info_frame = tk.Frame(master=root, bg='blue', height=90, width=700)
# info_frame.pack(side=tk.BOTTOM, fill=tk.X)
#
#
# label_frame = tk.Frame(info_frame)
# label_frame.pack(side=tk.TOP, fill=tk.X)
# day_label = tk.Label(label_frame, text='Day:')
# money_label = tk.Label(label_frame, text='Money:')
# energy_label = tk.Label(label_frame, text='Energy:')
# day_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# money_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# energy_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
#
#
# value_frame = tk.Frame(info_frame)
# value_frame.pack(side=tk.TOP, fill=tk.X)
# day_value = tk.Label(value_frame, text='1')
# money_value = tk.Label(value_frame, text='$0')
# energy_value = tk.Label(value_frame, text='100')
# day_value.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# money_value.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# energy_value.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
#
# button_frame = tk.Frame(info_frame)
# button_frame.pack(side=tk.BOTTOM, fill=tk.X)
# day_button = tk.Button(button_frame, text='Next Day')
# day_button.pack(side=tk.BOTTOM)
#
#
#
# root.mainloop()



import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# class InfoBar(AbstractGrid):
#     SIZE = (FARM_WIDTH + INVENTORY_WIDTH, INFO_BAR_HEIGHT)
#     DIMENSIONS = (2, 3)
#     def __init__(self, master: tk.Tk | tk.Frame) -> None:
#         super().__init__(master, size=self.SIZE, dimensions=self.DIMENSIONS)
#         self.redraw(1, 0, 100)
#     def redraw(self, day: int, money: int, energy: int):
#         self.clear()
#         self.day_position = (0, 0)
#         self.money_position = (0, 1)
#         self.energy_position = (0, 2)
#         self.annotate_position(self.day_position, text='Day:', font=HEADING_FONT)
#         self.annotate_position(self.money_position, text='Money:', font=HEADING_FONT)
#         self.annotate_position(self.energy_position, text='Energy:', font=HEADING_FONT)
#
#         self.day_value = (1, 0)
#         self.money_value = (1, 1)
#         self.energy_value = (1, 2)
#         self.annotate_position(self.day_value, text=f'{day}')
#         self.annotate_position(self.money_value, text=f'${money}')
#         self.annotate_position(self.energy_value, text=f'{energy}')


plant = {(1, 2): "apple"}
for plant_position, value in plant.items():
    print(plant_position)


