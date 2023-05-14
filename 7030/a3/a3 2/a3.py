import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Implement your classes here
class InfoBar(AbstractGrid):
    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        super().__init__(master, (2, 3), (FARM_WIDTH + INVENTORY_WIDTH,
                                          INFO_BAR_HEIGHT))
        self.day = 1
        self.money = 0
        self.energy = 100
        self.info_frame = tk.Frame(master, height=90, width=700)

        self.info_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.day_label = tk.Label(self.info_frame, text='Day:',
                                  font=HEADING_FONT)
        self.money_label = tk.Label(self.info_frame, text='Money:',
                                    font=HEADING_FONT)
        self.energy_label = tk.Label(self.info_frame, text='Energy:',
                                   font=HEADING_FONT)
        self.day_value = tk.Label(self.info_frame, text='1')
        self.money_value = tk.Label(self.info_frame, text='$0')
        self.energy_value = tk.Label(self.info_frame, text='100')
        self.next_day = tk.Button(self.info_frame, text='Next day',
                                  command=self.increment_day)

        self.day_label.config(text='Day:')
        self.money_label.config(text='Money:')
        self.energy_label.config(text='Energy:')

        self.day_label.grid(row=0, column=0, ipady=10)
        self.money_label.grid(row=0, column=1)
        self.energy_label.grid(row=0, column=2)
        self.day_value.grid(row=1, column=0, ipady=10)
        self.money_value.grid(row=1, column=1)
        self.energy_value.grid(row=1, column=2)
        self.next_day.grid(row=2, column=1)

        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)
        self.info_frame.columnconfigure(2, weight=1)
    def increment_day(self):
        self.day += 1
        self.redraw(self.day, self.money, self.energy)
    def redraw(self, day: int, money: int, energy: int):
        self.clear()
        self.day_value.configure(text=str(day))
        self.money_value.configure(text='$' + str(money))
        self.energy_value.configure(text=str(energy))
        self.day_value.pack()
        self.money_value.pack()
        self.energy_value.pack()

class FarmView(AbstractGrid):
    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                 size: tuple[int, int], **kwargs) -> None:
        super().__init__(master, dimensions, size, **kwargs)
        self.cache = {}

    def redraw(self, ground: list[str], plants: dict[tuple[int, int], 'Plant'],
               player_position: tuple[int, int], player_direction: str) -> None:
        self.clear()

        for row in range(len(ground)):
            for col in range(len(ground[row])):
                image = None
                if ground[row][col] == 'G':
                    image = 'images/grass.png'
                elif ground[row][col] == 'S':
                    image = 'images/soil.png'
                elif ground[row][col] == 'U':
                    image = 'images/untilled_soil.png'
                if image:
                    if image not in self.cache:
                        self.cache[image] = get_image(self.cache[image], (50, 50))
                    pic = self.cache[image]
                    self.create_image(col * 50, row * 50, image=pic, anchor='nw')


class FarmGame(object):
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        self.master = master
        self.master.title("Farm Game")

        self.master.geometry('725x800')
        self.image = get_image('images/header.png', (700, BANNER_HEIGHT))
        self.label = tk.Label(master, image=self.image)
        self.label.pack()

        self.model = FarmModel(map_file)

        self.info_bar = InfoBar(master)
        self.info_bar.pack()

        self.farm_view = FarmView(master, (10,10),
                                  (FARM_WIDTH, 550))
        self.farm_view.pack()


def play_game(root: tk.Tk, map_file: str) -> None:
    # Implement your play_game function here
    controller = FarmGame(root, map_file)
    root.mainloop()

def main() -> None:
    # Implement your main function here
    root = tk.Tk()
    play_game(root, map_file='maps/map1.txt')

if __name__ == '__main__':
    main()
