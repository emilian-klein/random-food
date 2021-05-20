import tkinter as tk
import requests, json

#formatting data from GET request to json
api_key = ''
response = requests.get('https://api.spoonacular.com/recipes/random?apiKey={}&number=1&'.format(api_key))
recipe = response.json()

#assign data stored in dictionary to list to simplify recived data
data_in_list = (recipe['recipes'])

#retreiving dish name and description
dish_name = data_in_list[0]['title']
dish_description = data_in_list[0]['summary']

#ingredients stored as list of dictionaires 
ingredients_in_list = data_in_list[0]['extendedIngredients']

print(recipe)
print(type(dish_name))
print(type(dish_description))
for ingredient in ingredients_in_list:
    print(ingredient['nameClean'])

#application window
root = tk.Tk()
root.title('Random Food')
root.iconbitmap('icon.ico')
root.geometry('1000x600')
root.resizable(False, False)

background = tk.Frame(bg='lightblue')
background.pack()
background.place(width=900, height=500, x=50, y=50)

dish_name_label = tk.Label(background, text=dish_name)
dish_name_label.pack()

dish_description_label = tk.Message(background, text=dish_description)
dish_description_label.pack()

dish_ingredients_label = tk.Label(background, text="Hello")
dish_ingredients_label.pack()

root.mainloop()