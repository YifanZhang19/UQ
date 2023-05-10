import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here
class FarmGame(object):
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        self.master = master
        self.master.title("Farm Game")
        self.master.geometry('1000x1000')
        self.label = tk.Label(master)
        self.image = get_image('header.png', (900, 200))
        self.label.config(image=self.image)
        self.label.pack()



def play_game(root: tk.Tk, map_file: str) -> None:
    # Implement your play_game function here
    game = FarmGame(root, map_file)
    root.mainloop()

def main() -> None:
    # Implement your main function here
    root = tk.Tk()
    play_game(root, map_file='maps/map1.txt')

if __name__ == '__main__':
    main()
