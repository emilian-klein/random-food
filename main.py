import tkinter as tk
from tkinter import *
from quitApp import quitApp
from getFood import randomFood

button_color = '#a43737'
right_frame_color = '#4592af'
left_frame_color = '#226089'

#application window
root = tk.Tk()
root.title('Random Food')
root.iconbitmap('icon.ico')
root.geometry('1000x600')
root.resizable(False, False)

#right GUI side
right_background = tk.Frame()
right_background.pack()
right_background.place(width=700, height=500, x=250, y=50)

dish_name_label = tk.Label(right_background, text='', bg=right_frame_color, anchor=W, font='Bahnschrift 16 bold', fg='#f4eee8', relief='ridge')
dish_name_label.pack()
dish_name_label.place(width=700, height=100)

dish_description_message = tk.Message(right_background, text='', bg=right_frame_color, font='Bahnschrift 12', justify=LEFT, width=450,  fg='#f4eee8', relief='ridge')
dish_description_message.pack()
dish_description_message.place(width=500, height=400, x=0, y=100)

dish_ingredients_label = tk.Label(right_background, text='', bg=right_frame_color, anchor=CENTER, font='Bahnschrift 14 bold', fg='#f4eee8', relief='ridge')
dish_ingredients_label.pack()
dish_ingredients_label.place(width=200, height=50, x=500, y=100)

dish_ingredients_message = tk.Message(right_background, text='', bg=right_frame_color, font='Bahnschrift 12', width=180, fg='#f4eee8', relief='ridge')
dish_ingredients_message.pack()
dish_ingredients_message.place(width=200, height=350, x=500, y=150)

#left GUI side
left_background = tk.Frame(bg=left_frame_color, relief='ridge')
left_background.pack()
left_background.place(width=200, height=500, x=50, y=50)

random_button = tk.Button(left_background, text='Find random food', font='Bahnschrift 12', command=lambda: randomFood(dish_name_label, dish_description_message, dish_ingredients_label, dish_ingredients_message), relief='raised', bg=button_color, fg='#f4eee8')
random_button.pack()
random_button.place(width=150, height=50, x=25, y=25)

quit_button = tk.Button(left_background, text='Button1', font='Bahnschrift 12', command=lambda: quitApp(root), relief='raised', bg=button_color, fg='#f4eee8')
quit_button.pack()
quit_button.place(width=150, height=50, x=25, y=125)

quit_button = tk.Button(left_background, text='Button2', font='Bahnschrift 12', command=lambda: quitApp(root), relief='raised', bg=button_color, fg='#f4eee8')
quit_button.pack()
quit_button.place(width=150, height=50, x=25, y=225)

quit_button = tk.Button(left_background, text='Button3', font='Bahnschrift 12', command=lambda: quitApp(root), relief='raised', bg=button_color, fg='#f4eee8')
quit_button.pack()
quit_button.place(width=150, height=50, x=25, y=325)

quit_button = tk.Button(left_background, text='Exit', font='Bahnschrift 12', command=lambda: quitApp(root), relief='raised', bg=button_color, fg='#f4eee8')
quit_button.pack()
quit_button.place(width=150, height=50, x=25, y=425)

root.mainloop()