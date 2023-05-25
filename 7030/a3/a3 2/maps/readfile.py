# with open('map1.txt', 'r') as file:
#     ground = [line.strip() for line in file.readlines()]
# print(ground)

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(master=root, bg='green', width=200, height=83)
frame.pack()
frame2 = tk.Frame(frame, bg='green')
frame2.pack()

label1 = tk.Label(frame2, text='abc\npop\nbbb', bg='green')
label1.pack(side=tk.TOP, anchor='w')


button_frame = tk.Frame(frame, bg='green')
button_frame.pack(side=tk.RIGHT)

button1 = tk.Button(button_frame, text='sss', bg='green')
button1.pack(side=tk.TOP)
button2 = tk.Button(button_frame, text='bbb', bg='green')
button2.pack(side=tk.TOP)

root.mainloop()

"""
Redraws the FarmView with the provided data.

Args:
    ground: A list representing the ground tiles on the farm.
    plants: A dictionary mapping plant positions to Plant objects.
    player_position: The position of the player on the farm grid.
    player_direction: The direction the player is facing.
"""
