import tkinter as tk
from tkinter import messagebox
from typing import Union

from PIL import Image, ImageTk

from gui3_support import *


# Create your TicTacToeView class here
class TicTacToeView(AbstractGrid):
    SIZE = (300, 300)
    DIMENSIONS = (3, 3)
    IMAGES = {
        TicTacToeModel.FIRST: "images/naught.png",
        TicTacToeModel.SECOND: "images/cross.png",
    }

    def __init__(self, master: tk.Tk | tk.Frame, **kwargs) -> None:
        super().__init__(master, self.DIMENSIONS, self.SIZE, **kwargs)
        self._cache = {}

    def _render_position(self, position: tuple[int, int], marker: Marker) -> None:
        self.create_rectangle(self.get_bbox(position))
        if marker is None:
            return

        image = get_image(self.IMAGES[marker], self.get_cell_size(), self._cache)
        self.create_image(self.get_midpoint(position), image=image)

    def redraw(self, board: list[list[Marker]]) -> None:
        self.clear()
        rows, columns = self.DIMENSIONS
        for row in range(rows):
            for col in range(columns):
                position = row, col
                self._render_position(position, board[row][col])


class TicTacToe:
    def __init__(self, master: tk.Tk):
        self._master = master
        master.title("Tic Tac Toe")

        self._model = TicTacToeModel()
        self._view = TicTacToeView(master)
        self._view.pack()

        # Draw the initial state to the view
        self._redraw()

        # Add your bindings here
        self._view.bind("<Button-1>", self.attempt_move)

    def _redraw(self) -> None:
        self._view.redraw(self._model.get_board_state())

    def _check_game_over(self) -> None:
        winner = self._model.get_winner()
        message_suffix = 'Play again?'

        if winner is not None:
            message = f'{winner} won! {message_suffix}'
        elif self._model.is_board_full():
            message = f'Draw! {message_suffix}'
        else:
            return

        self._master.update()
        if messagebox.askyesno(title="Game Over", message=message):
            self._model.new_game()
            self._redraw()
        else:
            self._master.destroy()


    def attempt_move(self, event: tk.Event) -> None:
        position = self._view.pixel_to_cell(event.x, event.y)

        # so that we can call attempt_move on the model
        self._model.attempt_place_marker(position)
        self._redraw()

        self._check_game_over()


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
