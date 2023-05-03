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


import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()

