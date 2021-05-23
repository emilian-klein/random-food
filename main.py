import tkinter as tk
from tkinter.constants import CENTER, LEFT, W
import requests, os
from tkinter import filedialog

#formatting data from GET request to json
api_key = ''
response = requests.get('https://api.spoonacular.com/recipes/random?apiKey={}&number=1&'.format(api_key))
recipe = response.json()

#assign data stored in dictionary to list in order to simplify recived data
data_in_list = (recipe['recipes'])

#retreiving dish name and description
dish_name = data_in_list[0]['title']
dish_description = data_in_list[0]['summary']

#creating variables to store and properly display ingredients
dish_ingredients = []
dish_ingredients_string = ''

#each ingredient (with additional information) stored as dictionary in a list 
ingredients_in_list = data_in_list[0]['extendedIngredients']

#creating list containing all ingredients names
for ingredient in ingredients_in_list:
    dish_ingredients.append(str(ingredient['nameClean']))

#adding special symbol to each element in a list 
list_sign = u"\u2022"
dish_ingredients = [list_sign + ingredient for ingredient in dish_ingredients]

#creating string to properly display list of ingredients, each in new line
dish_ingredients_string = '\n'.join([str(ingredient) for ingredient in dish_ingredients])

#formatting description to readable form from json
characters = ['</b>', '<b>', 'spoonacular ']
for element in characters:
    dish_description = dish_description.replace(element, '')

dish_description = dish_description.split('. ')

for sentence in dish_description:
    if('href="https://' in sentence):
        dish_description.remove(sentence)

dish_description = ". ".join(dish_description)
dish_description = dish_description + '.'

#application window
root = tk.Tk()
root.title('Random Food')
root.iconbitmap('icon.ico')
root.geometry('1000x600')
root.resizable(False, False)

#left side
left_background = tk.Frame(bg='orange')
left_background.pack()
left_background.place(width=200, height=500, x=50, y=50)

random_button = tk.Button(left_background, text='Find random food')
random_button.pack()
random_button.place(width=100, height=50, x=50, y=50)

quit_button = tk.Button(left_background, text='Exit')
quit_button.pack()
quit_button.place(width=100, height=50, x=50, y=150)

#right side
right_background = tk.Frame()
right_background.pack()
right_background.place(width=700, height=500, x=250, y=50)

dish_name_label = tk.Label(right_background, text=dish_name, bg='lightblue', anchor=W, relief='groove', font='Helvetica 18 bold')
dish_name_label.pack()
dish_name_label.place(width=700, height=100)

dish_description_label = tk.Message(right_background, text=dish_description, bg='lightgreen', relief='groove', font='Helvetica 12', justify=LEFT, width=450)
dish_description_label.pack()
dish_description_label.place(width=500, height=400, x=0, y=100)

ingredients_label = tk.Label(right_background, text='Ingredients', bg='pink', anchor=CENTER, relief='groove', font='Helvetica 12 bold')
ingredients_label.pack()
ingredients_label.place(width=200, height=50, x=500, y=100)

dish_ingredients_label = tk.Message(right_background, text=dish_ingredients_string, bg='pink', relief='groove')
dish_ingredients_label.pack()
dish_ingredients_label.place(width=200, height=350, x=500, y=150)

# folder = filedialog.askdirectory(initialdir=os.path.expanduser('~'))
# print(folder)

root.mainloop()