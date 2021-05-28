import requests

api_key = ''

def getFood(dish_name_label, dish_description_message, dish_ingredients_label, dish_ingredients_message, dish_instructions_message):
    response = requests.get('https://api.spoonacular.com/recipes/random?apiKey={}&number=1'.format(api_key))
    recipe = response.json()
    #assign data stored in dictionary to list in order to simplify data in json format
    data_in_list = (recipe['recipes'])

    #NAME
    dish_name = data_in_list[0]['title']
    
    #INGREDIENTS
    #creating variables to store and properly display ingredients
    dish_ingredients = []
    dish_ingredients_string = ''

    #each ingredient (with additional information) stored as dictionary in a list 
    ingredients_in_list = data_in_list[0]['extendedIngredients']

    #creating list containing all ingredients names without duplicates with amount and unit in brackets
    for ingredient in ingredients_in_list:
        dish_ingredients.append(str(ingredient['nameClean']) + ' (' + str(ingredient['amount'])[:5] + ' ' + str(ingredient['unit']) + ')')
    dish_ingredients = list(dict.fromkeys(dish_ingredients))

    dish_ingredients = [x.capitalize() for x in dish_ingredients]

    #adding special symbol to each element in a list 
    list_sign = u'\u2022'
    dish_ingredients = [list_sign + ingredient for ingredient in dish_ingredients]
    
    #creating string to properly display list of ingredients, each in new line
    dish_ingredients_string = '\n'.join([str(ingredient) for ingredient in dish_ingredients])
    
    #DESCRIPTION
    #assigning description to variable and formatting it to readable form from json
    dish_description = data_in_list[0]['summary']

    unwanted_words = ['</b>', '<b>']
    for element in unwanted_words:
        dish_description = dish_description.replace(element, '')

    dish_description = dish_description.split('. ')

    for sentence in dish_description:
        if('href="https://' in sentence):
            dish_description.remove(sentence)

    dish_description = '. '.join(dish_description)
    
    unwanted_words = ['spoonacular']
    for element in unwanted_words:
        dish_description = dish_description.replace(element, '')

    dish_description = dish_description + '.'

    #INSTRUCTIONS
    #assigning instructioins to variable and formatting it to readable form from json
    dish_instructions = data_in_list[0]['instructions']
    
    html_tags = ['</ol>', '<li>', '<ol>', '</li>', '\n', '<p>', '</p>', '<br>', '</br>', '<strong>', '</strong>']
    for element in html_tags:
        dish_instructions = dish_instructions.replace(element, '')
    
    dish_instructions = dish_instructions.split('.')
    
    try:
        dish_instructions.remove('')
    except:
        pass

    for index, sentence in enumerate(dish_instructions):
        temporary_sentence = sentence.lstrip(' ')
        temporary_sentence = temporary_sentence.capitalize()
        dish_instructions[index] = temporary_sentence

    dish_instructions = '. '.join(dish_instructions)
    
    #updating widgets
    dish_name_label.config(text=dish_name, font='Bahnschrift 16 bold')
    dish_description_message.config(text=dish_description)
    dish_ingredients_label.config(text='Ingredients')
    dish_ingredients_message.config(text=dish_ingredients_string)
    #based on lenght of instructions change font so it will fit into gui window
    if(len(dish_instructions)<=300):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 12') 
    elif(300<len(dish_instructions)<=500):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 11')  
    elif(500<len(dish_instructions)<=700):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 10') 
    elif(700<len(dish_instructions)<=900):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 9') 
    elif(900<len(dish_instructions)<=1200):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 8')
    elif(1200<len(dish_instructions)):
        dish_instructions_message.config(text=dish_instructions, anchor='center', font='Bahnschrift 7')