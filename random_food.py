import tkinter as tk
# from tkinter import *
# from datetime import datetime
# from quitApp import quitApp
# from getFood import getFood
# from saveFile import saveFile

# button_color = '#81b214'
# right_frame_color = '#536162'
# left_frame_color = '#393e46'
#
# date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# date_and_time = date_and_time.split(' ')
# date_and_time = '\n   '.join(date_and_time)
#
# #application window
# root = tk.Tk()
# root.title('Random Food')
# root.iconbitmap('icon.ico')
# root.geometry('1000x700')
# root.resizable(False, False)
#
# #right GUI side
# right_background = tk.Frame()
# right_background.pack()
# right_background.place(width=700, height=600, x=250, y=50)
#
# dish_name_label = tk.Label(right_background, text='Welcome to Random Food!', bg=right_frame_color, anchor=W, font='Bahnschrift 18 bold', fg='#81b214', relief='ridge')
# dish_name_label.pack()
# dish_name_label.place(width=700, height=100)
#
# dish_description_message = tk.Message(right_background, text='You have no idea what to eat for breakfast? Maybe you are bored of constantly ordering food from local restaurants? This is where Random Food comes in handy. Find an idea for a new meal with one click. Then save the meal of your choice, print a list of ingredients you need, and go shopping. Afterwards prepare it yourself, additionaly learning new recipes. Enjoy your meal!', bg=right_frame_color, font='Bahnschrift 12', justify=LEFT, width=450,  fg='#f4eee8', relief='ridge')
# dish_description_message.pack()
# dish_description_message.place(width=500, height=250, x=0, y=100)
#
# dish_instructions_message = tk.Message(right_background, text='Created by emilian-klein', bg=right_frame_color, anchor=SW, font='Bahnschrift 10', justify=LEFT, width=450,  fg='#f4eee8', relief='ridge')
# dish_instructions_message.pack()
# dish_instructions_message.place(width=500, height=250, x=0, y=350)
#
# dish_ingredients_label = tk.Label(right_background, text='Today is:', bg=right_frame_color, anchor=CENTER, font='Bahnschrift 14 bold', fg='#81b214', relief='ridge')
# dish_ingredients_label.pack()
# dish_ingredients_label.place(width=200, height=50, x=500, y=100)
#
# dish_ingredients_message = tk.Message(right_background, text=date_and_time, bg=right_frame_color, font='Bahnschrift 11', width=180, fg='#f4eee8', relief='ridge')
# dish_ingredients_message.pack()
# dish_ingredients_message.place(width=200, height=450, x=500, y=150)
#
# #left GUI side
# left_background = tk.Frame(bg=left_frame_color, relief='ridge')
# left_background.pack()
# left_background.place(width=200, height=600, x=50, y=50)
#
# random_button = tk.Button(left_background, text='Find random food', font='Bahnschrift 11', command=lambda: getFood(dish_name_label, dish_description_message, dish_ingredients_label, dish_ingredients_message, dish_instructions_message), relief='raised', bg=button_color, fg='#f4eee8')
# random_button.pack()
# random_button.place(width=150, height=50, x=25, y=25)
#
# save_button = tk.Button(left_background, text='Save to text file', font='Bahnschrift 11', command=lambda: saveFile(dish_name_label, dish_description_message, dish_ingredients_message, dish_instructions_message), relief='raised', bg=button_color, fg='#f4eee8')
# save_button.pack()
# save_button.place(width=150, height=50, x=25, y=125)
#
# quit_button = tk.Button(left_background, text='Exit', font='Bahnschrift 11', command=lambda: quitApp(root), relief='raised', bg=button_color, fg='#f4eee8')
# quit_button.pack()
# quit_button.place(width=150, height=50, x=25, y=225)
#
# root.mainloop()


class RandomFood(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Food")
        self.iconbitmap("images/icon.ico")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.sm_n_font_style = ("Bahnschrift", "11", "normal")
        self.lg_n_font_style = ("Bahnschrift", "14", "normal")
        self.sm_b_font_style = ("Bahnschrift", "11", "bold")
        self.lg_b_font_style = ("Bahnschrift", "14", "bold")

        self.left_frame = tk.Frame(relief="ridge", bg="#EAD7BB")
        self.left_frame.place(x=0, y=0, height=600, width=200)

        self.find_random_food_button = tk.Button(self.left_frame, text="Find random food", font=self.sm_b_font_style, relief="raised", bg="#113946", fg="white")
        self.find_random_food_button.place(x=25, y=25, height=50, width=150)

        self.save_recipe_button = tk.Button(self.left_frame, text="Save recipe", font=self.sm_b_font_style, relief="raised", bg="#113946", fg="white")
        self.save_recipe_button.place(x=25, y=125, height=50, width=150)

        self.exit_button = tk.Button(self.left_frame, text="Exit", font=self.sm_b_font_style, relief="raised", bg="#113946", fg="white")
        self.exit_button.place(x=25, y=225, height=50, width=150)

        self.right_frame = tk.Frame(relief="ridge", bg="#BCA37F")
        self.right_frame.place(x=200, y=0, height=600, width=800)

        self.dish_name_label = tk.Label(self.right_frame, text="dish_name_label", font=self.sm_n_font_style, anchor="w", bg="#BCA37F")
        self.dish_name_label.place(x=0, y=0, height=100, width=800)

        self.dish_description_message = tk.Message(self.right_frame, text="dish_description_message", bg="#BCA37F", font=self.sm_n_font_style, justify="left")
        self.dish_description_message.place(x=0, y=100, height=250, width=500)

        self.dish_instructions_message = tk.Message(self.right_frame, text="dish_instructions_message", bg="#BCA37F", font=self.sm_n_font_style, justify="left")
        self.dish_instructions_message.place(x=0, y=350, height=250, width=500)

        self.dish_ingredients_label = tk.Label(self.right_frame, text="dish_ingredients_label", bg="#BCA37F", font=self.sm_n_font_style, anchor="center")
        self.dish_ingredients_label.place(x=500, y=100, height=50, width=100)

        self.dish_ingredients_message = tk.Message(self.right_frame, text="dish_ingredients_message", bg="#BCA37F", font=self.sm_n_font_style)
        self.dish_ingredients_message.place(x=500, y=150, height=450, width=200)


if __name__ == "__main__":
    app = RandomFood()
    app.mainloop()
