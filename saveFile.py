from getFood import *
from tkinter.filedialog import asksaveasfile

def saveFile(dish_name_label, dish_description_message, dish_ingredients_message, dish_instructions_message):
    dish_name = dish_name_label['text']
    dish_description = dish_description_message['text']
    dish_ingredients = dish_ingredients_message['text']
    dish_instruction = dish_instructions_message['text']

    file_types = [('Text Document', '*.txt'), ('Word Document', '*.docx'), ('All Files', '*.*')]
    file = asksaveasfile(filetypes = file_types)

    recipe = open(file.name, 'w')
    recipe.write(dish_name + "\n    " + dish_description + "\n\nIngredients:\n" + dish_ingredients + "\n\nInstructions:\n" + dish_instruction)
    recipe.close()
    print(file.name)