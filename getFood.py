import requests

api_key = ''

def randomFood(dish_name_label, dish_description_message, dish_ingredients_label, dish_ingredients_message):
    #formatting data from GET request to json
    response = requests.get('https://api.spoonacular.com/recipes/random?apiKey={}&number=1&'.format(api_key))
    recipe = response.json()

    #assign data stored in dictionary to list in order to simplify recived data
    data_in_list = (recipe['recipes'])

    #NAME
    #retreiving dish name
    dish_name = data_in_list[0]['title']
    
    #INGREDIENTS
    #creating variables to store and properly display ingredients
    dish_ingredients = []
    dish_ingredients_string = ''

    #each ingredient (with additional information) stored as dictionary in a list 
    ingredients_in_list = data_in_list[0]['extendedIngredients']

    #creating list containing all ingredients names without duplicates and 'None' value
    for ingredient in ingredients_in_list:
        dish_ingredients.append(str(ingredient['nameClean']))
    dish_ingredients = [x.capitalize() for x in dish_ingredients]
    
    try:
        dish_ingredients.remove('None')
    except:
        pass

    dish_ingredients = list(dict.fromkeys(dish_ingredients))

    #adding special symbol to each element in a list 
    list_sign = u"\u2022"
    dish_ingredients = [list_sign + ingredient for ingredient in dish_ingredients]
    
    #creating string to properly display list of ingredients, each in new line
    dish_ingredients_string = '\n'.join([str(ingredient) for ingredient in dish_ingredients])
    
    #DESCRIPTION
    #assigning description to variable and formatting it to readable form from json
    dish_description = data_in_list[0]['summary']
    
    unwanted_words = ['</b>', '<b>', 'spoonacular ']
    for element in unwanted_words:
        dish_description = dish_description.replace(element, '')

    dish_description = dish_description.split('. ')

    for sentence in dish_description:
        if('href="https://' in sentence):
            dish_description.remove(sentence)

    dish_description = ". ".join(dish_description)
    dish_description = dish_description + '.'

    #updating widgets
    dish_name_label.config(text=dish_name)
    dish_description_message.config(text=dish_description)
    dish_ingredients_label.config(text='Ingredients')
    dish_ingredients_message.config(text=dish_ingredients_string)