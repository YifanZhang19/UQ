import tkinter as tk
from tkinter import messagebox


# root = tk.Tk()
# root.title('test function')
# root.geometry('400x200')
# button = tk.Button(root, text='click me!')
#
# button.pack()
#
#
# def flower(b):
#     messagebox.showinfo("wow", 'Isis')
#     print("abc")
#
#
# button.bind("press", flower)
# root.mainloop()
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # self.button1 = tk.Button(self, text='click me', command=self.fuuu)
        # self.button1.pack()
        #
        # self.exitBu = tk.Button(self, text='quit', command=root.destroy)
        # self.exitBu.pack()
    #     self.label1 = tk.Label(self, text='woooooow', width=10, height=10,
    #                            bg='blue', fg='white')
    #     self.label1.pack()
    #
    #     # global photo
    #     # photo = tk.PhotoImage(file='a3 2/images/grass.png')
    #     # self.label2 = tk.Label(self, image=photo)
    #     # self.label2.pack()
    #     self.button = tk.Button(self, text='abc', width=10, height=10)
    #     self.button.pack()
    #     self.button.config(anchor='n')
    # def fuuu(self):
    #     tk.messagebox.showinfo('title', 'woooooooooo!')
        self.label1 = tk.Label(self, text='user')
        self.label1.pack()
        v1 = tk.StringVar()
        self.entry1 = tk.Entry(self, textvariable=v1)
        self.entry1.pack()
        v1.set('admin: ')

        self.label2 = tk.Label(self, text='password')
        self.label2.pack()
        v2 = tk.StringVar()
        self.entry2 = tk.Entry(self, textvariable=v2, show='*')
        self.entry2.pack()
        v2.set('password: ')

        self.button = tk.Button(self, text='log', command=self.login)
        self.button.pack()
    def login(self):
        print('user:' + self.entry1.get())
        print('password:' + self.entry2.get())

        tk.messagebox.showinfo('welcome', 'woooow!')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x200')
    root.title('Test')
    app = Application(master=root)
    root.mainloop()
