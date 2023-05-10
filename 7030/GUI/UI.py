# # # # import tkinter as tk
# # # #
# # # # window = tk.Tk()
# # # # greeting = tk.Label(text="Hello,World!",
# # # #                     fg="white",
# # # #                     bg="red",
# # # #                     width=10,
# # # #                     height=10)
# # # # greeting.pack()
# # # # # fg = foreground bg = background
# # # #
# # # # button = tk.Button(
# # # #     text="Click me!",
# # # #     width=25,
# # # #     height=5,
# # # #     bg="blue",
# # # #     fg="yellow",
# # # # )
# # # # button.pack()
# # # #
# # # # entry = tk.Entry(fg="yellow", bg="blue", width=50)
# # # # entry.pack()
# # # #
# # # # window.mainloop()
# # #
# # # # import tkinter as tk
# # # # window = tk.Tk()
# # # #
# # # # label = tk.Label(text="Name")
# # # # label.pack()
# # # # entry = tk.Entry()
# # # # entry.pack()
# # # # name = entry.get()
# # # # name
# # # # entry.delete(0)
# # # #
# # # # window.mainloop()
# # #
# # # import tkinter as tk
# # # window = tk.Tk()
# # # frame_a = tk.Frame()
# # # label_a = tk.Label(master=frame_a, text="im in frame A")
# # # label_a.pack()
# # #
# # # frame_b = tk.Frame()
# # # label_b = tk.Label(master=frame_b, text="im in frame B")
# # # label_b.pack()
# # #
# # # frame_a.pack()
# # # frame_b.pack()
# # #
# # # window.mainloop()
# #
# # import tkinter as tk
# # border_effects = {
# #     "flat": tk.FLAT,
# #     "sunken": tk.SUNKEN,
# #     "raised": tk.RAISED,
# #     "groove": tk.GROOVE,
# #     "ridge": tk.RIDGE,
# # }
# #
# # window = tk.Tk()
# #
# # for relief_name, relief in border_effects.items():
# #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
# #     frame.pack(side=tk.LEFT)
# #     label = tk.Label(master=frame, text=relief_name)
# #     label.pack()
# #
# # window.mainloop()
#
#
# import tkinter as tk
# window = tk.Tk()
#
# frame = tk.Frame()
# entry = tk.Entry()
# entry.pack()
# label = tk.Label(master=frame, text=entry.get(), bg="white", fg="black")
# frame.pack()
# label.pack()
# entry = tk.Entry(width=40, bg="white", fg="black")
# entry.pack()
#
# entry.insert(0, "What is your name?")
#
# window.mainloop()


# import tkinter as tk
#
# window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# window.mainloop()

# import tkinter as tk
#
# window = tk.Tk()
#
# frame = tk.Frame(master=window, width=150, height=150)
# frame.pack()
#
# label1 = tk.Label(master=frame, text="im at (0, 0)", bg="red")
# label1.place(x=0, y=0)
#
# label2 = tk.Label(master=frame, text="im at (75, 75)", bg="yellow")
# label2.place(x=75, y=75)
#
# window.mainloop()
import tkinter as tk

root = tk.Tk()

# my_label = tk.Label(root, text='hello world!')
# my_label2 = tk.Label(root, text="my name is jesse")
# my_label.grid(row=0, column=0)
# my_label2.grid(row=1, column=0)
root.title('simple calculator')

e = tk.Entry(root, width=35, borderwidth=5, fg="white", bg='black')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, 'entry your name: ')

# def myClick():
#     hello = "Hello " + e.get()
#     myLabel = tk.Label(root, text=hello)
#     myLabel.pack()
def button_click(number):
    e.delete(0, tk.END)
    e.insert(0, number)
button_1 = tk.Button(root, text='1', padx=40, pady=20, command=button_click)
button_2 = tk.Button(root, text='2', padx=40, pady=20, command=button_click)
button_3 = tk.Button(root, text='3', padx=40, pady=20, command=button_click)
button_4 = tk.Button(root, text='4', padx=40, pady=20, command=button_click)
button_5 = tk.Button(root, text='5', padx=40, pady=20, command=button_click)
button_6 = tk.Button(root, text='6', padx=40, pady=20, command=button_click)
button_7 = tk.Button(root, text='7', padx=40, pady=20, command=button_click)
button_8 = tk.Button(root, text='8', padx=40, pady=20, command=button_click)
button_9 = tk.Button(root, text='9', padx=40, pady=20, command=button_click)
button_0 = tk.Button(root, text='0', padx=40, pady=20, command=button_click)
button_add = tk.Button(root, text='+', padx=39, pady=20, command=button_click)
button_equal = tk.Button(root, text='=', padx=91, pady=20, command=button_click)
button_clear = tk.Button(root, text='Clear', padx=79, pady=20,
                         command=button_add)
#put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
# myButton = tk.Button(root, text="enter your name!", command=myClick)


root.mainloop()