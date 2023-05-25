import tkinter as tk
from tkinter import filedialog  # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *


# Implement your classes here


class InfoBar(AbstractGrid):
    """
    The InfoBar class represents the information bar in the farm game GUI.
    It displays the current day, money, and energy of the player.

    Attributes:
        SIZE (tuple): The size of the InfoBar in pixels.
        DIMENSIONS (tuple): The dimensions of the InfoBar grid.
    """

    SIZE = (FARM_WIDTH + INVENTORY_WIDTH, INFO_BAR_HEIGHT)
    DIMENSIONS = (2, 3)

    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """
        Initializes the InfoBar.

        Args:
            master (tk.Tk or tk.Frame): The parent widget for the InfoBar.
        """

        super().__init__(master, self.DIMENSIONS, self.SIZE)

    def redraw(self, day: int, money: int, energy: int):
        """
        Redraws the InfoBar with the provided values for day, money, and energy.

        Args:
            day: The current day.
            money: The amount of money the player has.
            energy: The energy level of the player.
        """

        self.clear()
        day_position = (0, 0)
        money_position = (0, 1)
        energy_position = (0, 2)
        self.annotate_position(day_position, text='Day:',
                               font=HEADING_FONT)
        self.annotate_position(money_position, text='Money:',
                               font=HEADING_FONT)
        self.annotate_position(energy_position, text='Energy:',
                               font=HEADING_FONT)

        day_value = (1, 0)
        money_value = (1, 1)
        energy_value = (1, 2)
        self.annotate_position(day_value, text=f'{day}')
        self.annotate_position(money_value, text=f'${money}')
        self.annotate_position(energy_value, text=f'{energy}')


class FarmView(AbstractGrid):
    """
    The FarmView class represents the view of the farm in the farm game GUI.
    It displays the ground, plants, and player's position on the farm.
    """

    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                 size: tuple[int, int], **kwargs) -> None:
        """
        Initializes the FarmView.

        Args:
            master: The parent widget for the FarmView.
            dimensions: The dimensions of the farm grid.
            size: The size of the FarmView in pixels.
            **kwargs: Additional arguments to be passed to the superclass
            constructor.
        """

        super().__init__(master, dimensions=dimensions, size=size, **kwargs)
        self.cache = {}
        self.photo = None

    def redraw(self, ground: list[str], plants: dict[tuple[int, int],
    'Plant'], player_position: tuple[int, int], player_direction:
    str) -> None:
        """
        Redraws the FarmView with the provided data.
        
        Args:
            ground: A list representing the ground tiles on the farm.
            plants: A dictionary mapping plant positions to Plant objects.
            player_position: The position of the player on the farm grid.
            player_direction: The direction the player is facing.
        """

        self.clear()
        for row in range(len(ground)):
            for col in range(len(ground[row])):
                position = row, col
                pic = ground[row][col]
                if pic == 'G':
                    self.photo = GRASS
                elif pic == 'S':
                    self.photo = SOIL
                elif pic == 'U':
                    self.photo = UNTILLED
                self.get_bbox(position)
                image = get_image(f'images/{IMAGES[self.photo]}',
                                  self.get_cell_size(),
                                  self.cache)
                self.create_image(self.get_midpoint(position), image=image)

        for plants_position, plant in plants.items():
            plants = f'images/plants/{plant.get_name()}/stage' \
                     f'_{plant.get_stage()}.png'
            p_pic = get_image(plants, self.get_cell_size(), self.cache)
            self.create_image(self.get_midpoint(plants_position), image=p_pic)

        player_pic = None
        if player_direction == UP:
            player_pic = f'images/{IMAGES[UP]}'
        elif player_direction == DOWN:
            player_pic = f'images/{IMAGES[DOWN]}'
        elif player_direction == LEFT:
            player_pic = f'images/{IMAGES[LEFT]}'
        elif player_direction == RIGHT:
            player_pic = f'images/{IMAGES[RIGHT]}'
        player_image = get_image(player_pic, self.get_cell_size(), self.cache)
        self.create_image(self.get_midpoint(player_position),
                          image=player_image)


class ItemView(tk.Frame):
    """
    This class represents a graphical view of an item in the inventory.
    """

    def __init__(self, master: tk.Frame, item_name: str, amount: int,
                 select_command: Optional[Callable[[str], None]] = None,
                 sell_command: Optional[Callable[[str], None]] = None,
                 buy_command: Optional[Callable[[str], None]] = None) -> None:
        """
        Initializes the ItemView.

        Args:
            master: The parent widget for the ItemView.
            item_name: The name of the item.
            amount: The amount of the item.
            select_command: Optional command to be executed when the item is
                            selected.
            sell_command: Optional command to be executed when the item is sold.
            buy_command Optional command to be executed when the item is bought.
        """

        super().__init__(master)
        self.item_name = item_name
        if amount > 0:
            self.config(bg=INVENTORY_COLOUR, width=200, height=500 / 6,
                        borderwidth=1, relief="raised",
                        highlightbackground=INVENTORY_OUTLINE_COLOUR)
        else:
            self.config(bg=INVENTORY_EMPTY_COLOUR, width=200, height=500 / 6,
                        borderwidth=1, relief="raised",
                        highlightbackground=INVENTORY_OUTLINE_COLOUR)

        self.pack_propagate(False)
        if amount > 0:
            self.bg = INVENTORY_COLOUR
        else:
            self.bg = INVENTORY_EMPTY_COLOUR
        if 'Seed' in item_name:
            self.item = tk.Label(self, text=f'{item_name}: {amount}'
                                            f'\nSell price: '
                                            f'${SELL_PRICES[item_name]}'
                                            f'\nBuy price: '
                                            f'${BUY_PRICES[item_name]}',
                                 bg=self.bg)
            self.item.pack(side=tk.LEFT)

            self.buy = tk.Button(self, text='Buy', relief=tk.FLAT, bg=self.bg,
                                 bd=0, command=buy_command,
                                 highlightbackground=self.bg)
            self.sell = tk.Button(self, text='Sell', relief=tk.FLAT,
                                  bg=self.bg, bd=0, command=sell_command,
                                  highlightbackground=self.bg)
            self.buy.pack(side=tk.LEFT)
            self.sell.pack(side=tk.LEFT)
        else:
            self.item = tk.Label(self, text=f'{item_name}: '
                                            f'{amount}\nSell price: $'
                                            f'{SELL_PRICES[item_name]}\n'
                                            f'Buy price: $N/A', bg=self.bg)
            self.item.pack(side=tk.LEFT)
            self.sell = tk.Button(self, text='Sell', relief=tk.FLAT, bg=self.bg,
                                  bd=0,
                                  command=sell_command,
                                  highlightbackground=self.bg)
            self.sell.pack(side=tk.LEFT)

        self.bind("<Button-1>", lambda event: select_command(item_name))
        self.item.bind("<Button-1>", lambda event: select_command(item_name))

    def update(self, amount: int, selected: bool = False) -> None:
        """
        Update the item view with the given amount and selection status.

        Args:
            amount: The amount of the item.
            selected: Whether the item is currently selected.
        """

        if amount == 0:
            if 'Seed' in self.item_name:
                self.config(bg=INVENTORY_EMPTY_COLOUR)
                self.item.config(bg=INVENTORY_EMPTY_COLOUR,
                                 text=f'{self.item_name}:'
                                      f' {amount}'
                                      f'\nSell price: '
                                      f'${SELL_PRICES[self.item_name]}'
                                      f'\nBuy price: '
                                      f'${BUY_PRICES[self.item_name]}')
                self.sell.config(highlightbackground=INVENTORY_EMPTY_COLOUR)
                self.buy.config(highlightbackground=INVENTORY_EMPTY_COLOUR)
            else:
                self.config(bg=INVENTORY_EMPTY_COLOUR)
                self.item.config(bg=INVENTORY_EMPTY_COLOUR,
                                 text=f'{self.item_name}:'
                                      f' {amount}'
                                      f'\nSell price: '
                                      f'${SELL_PRICES[self.item_name]}'
                                      f'\nBuy price: '
                                      f'$N/A')
                self.sell.config(highlightbackground=INVENTORY_EMPTY_COLOUR)

        else:
            if selected:
                if 'Seed' in self.item_name:
                    self.config(bg=INVENTORY_SELECTED_COLOUR)
                    self.item.config(bg=INVENTORY_SELECTED_COLOUR,
                                     text=f'{self.item_name}:'
                                          f' {amount}'
                                          f'\nSell price: '
                                          f'${SELL_PRICES[self.item_name]}'
                                          f'\nBuy price: '
                                          f'${BUY_PRICES[self.item_name]}')
                    self.sell.config(
                        highlightbackground=INVENTORY_SELECTED_COLOUR
                    )
                    self.buy.config(
                        highlightbackground=INVENTORY_SELECTED_COLOUR
                    )
                else:
                    self.config(bg=INVENTORY_SELECTED_COLOUR)
                    self.item.config(bg=INVENTORY_SELECTED_COLOUR,
                                     text=f'{self.item_name}:'
                                          f' {amount}'
                                          f'\nSell price: '
                                          f'${SELL_PRICES[self.item_name]}'
                                          f'\nBuy price: '
                                          f'$N/A')
                    self.sell.config(
                        highlightbackground=INVENTORY_SELECTED_COLOUR
                    )

            else:
                if 'Seed' in self.item_name:
                    self.config(bg=INVENTORY_COLOUR)
                    self.item.config(bg=INVENTORY_COLOUR,
                                     text=f'{self.item_name}:'
                                          f' {amount}'
                                          f'\nSell price: '
                                          f'${SELL_PRICES[self.item_name]}'
                                          f'\nBuy price: '
                                          f'${BUY_PRICES[self.item_name]}')
                    self.sell.config(highlightbackground=INVENTORY_COLOUR)
                    self.buy.config(highlightbackground=INVENTORY_COLOUR)
                else:
                    self.config(bg=INVENTORY_COLOUR)
                    self.item.config(bg=INVENTORY_COLOUR,
                                     text=f'{self.item_name}:'
                                          f' {amount}'
                                          f'\nSell price: '
                                          f'${SELL_PRICES[self.item_name]}'
                                          f'\nBuy price: '
                                          f'$N/A')
                    self.sell.config(highlightbackground=INVENTORY_COLOUR)


class FarmGame:
    """
    The FarmGame class represents the main game interface for the farm game.
    """

    def __init__(self, master: tk.Tk, map_file: str) -> None:
        """
        Initializes the FarmGame.

        Args:
            master: The root Tkinter window.
            map_file: The file path to the map file.
        """

        self.item = None
        self.item_details = None
        self.items = {}
        self.cache = {}
        self.master = master
        self.master.title("Farm Game")

        menu = tk.Menu(master)
        master.config(menu=menu)
        file_menu = tk.Menu(menu)

        menu.add_cascade(
            label='File',
            menu=file_menu
        )

        file_menu.add_command(
            label='Quit',
            command=master.destroy
        )

        file_menu.add_command(
            label='Map selection',
            command=self.map_selection
        )

        self.image = get_image('images/header.png', (700, BANNER_HEIGHT),
                               self.cache)
        self.label = tk.Label(master, image=self.image)
        self.label.pack(side=tk.TOP)

        self.model = FarmModel(map_file)
        self.info_bar = InfoBar(master)
        self.day_button = tk.Button(master, text='Next day',
                                    command=self.next_day)
        self.day_button.pack(side=tk.BOTTOM)
        self.info_bar.pack(side=tk.BOTTOM)

        self.farm_view = FarmView(master, self.model.get_dimensions(),
                                  (FARM_WIDTH, FARM_WIDTH))
        self.farm_view.redraw(self.model.get_map(), self.model.get_plants(),
                              self.model.get_player().get_position(),
                              self.model.get_player().get_direction())
        self.farm_view.pack(side=tk.LEFT)
        for item in ITEMS:
            if item in self.model.get_player().get_inventory().keys():
                self.amount = self.model.get_player().get_inventory()[item]
            else:
                self.amount = 0
            self.item_view = ItemView(master, item, self.amount,
                                      lambda item_name=item: self.select_item(
                                          item_name),
                                      lambda item_name=item: self.sell_item(
                                          item_name),
                                      lambda item_name=item: self.buy_item(
                                          item_name)
                                      )
            self.items[item] = self.item_view
            self.item_view.pack(side=tk.TOP, anchor='n')

        master.bind('<KeyPress>', self.handle_keypress)
        self.redraw()

    def next_day(self):
        """
        Proceeds to the next day in the game.
        """

        self.model.new_day()
        self.redraw()

    def redraw(self) -> None:
        """
        Redraws the game interface.
        """

        self.farm_view.redraw(self.model.get_map(), self.model.get_plants(),
                              self.model.get_player().get_position(),
                              self.model.get_player().get_direction())

        self.info_bar.redraw(self.model.get_days_elapsed(),
                             self.model.get_player().get_money(),
                             self.model.get_player().get_energy())

        self.item_details = self.model.get_player().get_inventory()
        self.item = self.model.get_player().get_selected_item()

        for item in self.items.values():
            if item.item_name in self.item_details.keys():
                item.update(self.item_details[item.item_name],
                            self.item == item.item_name)
            else:
                item.update(0, self.item == item.item_name)

    def handle_keypress(self, event: tk.Event) -> None:
        """
        Handles keypress events.

        Args:
            event: The keypress event.
        """

        if event.char == UP:
            self.model.move_player(UP)
        elif event.char == DOWN:
            self.model.move_player(DOWN)
        elif event.char == LEFT:
            self.model.move_player(LEFT)
        elif event.char == RIGHT:
            self.model.move_player(RIGHT)
        elif event.char == 't':
            self.model.till_soil(self.model.get_player_position())
        elif event.char == 'u':
            self.model.untill_soil(self.model.get_player_position())
        elif event.char == 'p':
            player_position = self.model.get_player_position()
            plants = self.model.get_player().get_selected_item()
            map_p = self.model.get_map()[player_position[0]][player_position[1]]
            inventory = self.model.get_player().get_inventory().keys()
            plant_number = 0
            if plants in inventory:
                plant_number = self.model.get_player().get_inventory()[plants]
            if map_p == 'S':
                if plants:
                    if 'Seed' in plants:
                        if plant_number > 0:
                            if plants == 'Potato Seed':
                                plant = PotatoPlant()
                                self.model.add_plant(player_position, plant)
                                self.model.get_player().remove_item((plants, 1))
                            elif plants == 'Kale Seed':
                                plant = KalePlant()
                                self.model.add_plant(player_position, plant)
                                self.model.get_player().remove_item((plants, 1))
                            elif plants == 'Berry Seed':
                                plant = BerryPlant()
                                self.model.add_plant(player_position, plant)
                                self.model.get_player().remove_item((plants, 1))
        elif event.char == 'h':
            player_position = self.model.get_player_position()
            plant = self.model.get_plants()[player_position]
            if plant:
                if plant.can_harvest():
                    harvest = self.model.harvest_plant(player_position)
                    self.model.get_player().add_item(harvest)
                    self.model.remove_plant(player_position)
        elif event.char == 'r':
            player_position = self.model.get_player_position()
            position = []
            for all_position in self.model.get_plants().keys():
                position.append(all_position)
            if player_position in position:
                plant = self.model.get_plants()[player_position]
                if plant:
                    self.model.remove_plant(player_position)

        self.redraw()

    def select_item(self, item_name: str) -> None:
        """
        Selects an item from the inventory.

        Args:
            item_name: The name of the item.
        """

        self.model.get_player().select_item(item_name)
        self.redraw()

    def buy_item(self, item_name: str) -> None:
        """
        Buys an item from the store.

        Args:
            item_name: The name of the item.
        """

        if item_name in BUY_PRICES.keys():
            self.model.get_player().buy(item_name, BUY_PRICES[item_name])
        self.redraw()

    def sell_item(self, item_name: str) -> None:
        """
        Sells an item from the inventory.

        Args:
            item_name: The name of the item.
        """

        self.model.get_player().sell(item_name, SELL_PRICES[item_name])
        self.redraw()

    def map_selection(self):
        """
        Change game map

        """

        file_path = filedialog.askopenfilename()
        self.model = FarmModel(file_path)
        self.farm_view.cache = {}
        self.farm_view.set_dimensions(self.model.get_dimensions())
        self.redraw()


def play_game(root: tk.Tk, map_file: str) -> None:
    """
    Plays the farm game.

    Args:
        root: The root Tkinter window.
        map_file: The file path to the map file.
    """

    FarmGame(root, map_file)
    root.mainloop()


def main() -> None:
    """
    The main function to start the farm game.
    """

    root = tk.Tk()
    play_game(root, 'maps/map1.txt')


if __name__ == '__main__':
    main()
