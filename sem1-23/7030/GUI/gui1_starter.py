# """
# Simple GUI programming exercise to demonstrate component layout
# and event handling.
# """
#
# __copyright__ = "Copyright 2018, University of Queensland"
#
# import tkinter as tk
#
#
# class SampleApp(object):
#     def __init__(self, master):
#         self._colour_entry = None
#         self._master = master
#         master.title("Hello!")
#         master.minsize(430, 200)
#
#         self._lbl = tk.Label(master, text="Choose a button")
#         self._lbl.pack(side=tk.TOP, expand=True)
#
#         btn_frame = tk.Frame(master)
#         btn_frame.pack(side=tk.BOTTOM, pady=10)
#
#         blue_btn = tk.Button(btn_frame, text="Change to Blue",
#                              command=self.change_blue)
#         blue_btn.pack(side=tk.LEFT)
#
#         green_btn = tk.Button(btn_frame, text="Change to Green",
#                               command=self.change_green)
#         green_btn.pack(side=tk.LEFT)
#
#         entry_frame = tk.Frame(master)
#         entry_frame.pack(side=tk.TOP)
#
#         entry_label = tk.Label(entry_frame, text="Change the colour to: ")
#         entry_label.pack(side=tk.LEFT)
#
#         colour_entry = tk.Entry(entry_frame)
#         colour_entry.pack(side=tk.LEFT)
#
#         entry_button = tk.Button(entry_frame, text="Change it!", command=
#         self.colour_custom)
#         entry_button.pack(side=tk.LEFT)
#
#
#
#     def say_hello(self):
#         print('Hello! Thanks for clicking!')
#
#     def change_blue(self):
#         self._lbl.config(text="This label is blue", bg="blue")
#
#     def change_green(self):
#         self._lbl.config(text="This label is blue", bg="green")
#
#     def colour_custom(self):
#         colour = self._colour_entry.get()
#         try:
#             self._lbl.config(text=f"This label is {colour}", bg=colour)
#         except tk.TclError:
#             pass
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SampleApp(root)
#     root.mainloop()


import tkinter as tk

root = tk.Tk()

labe1 = tk.Label(text='abc')
labe1.pack(side=tk.TOP)

labe2 = tk.Label(text='adsds')
labe2.pack(side=tk.LEFT)

labe3 = tk.Label(text='aeeeee')
labe3.pack(side=tk.RIGHT)

root.mainloop()

