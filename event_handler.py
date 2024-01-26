import requests as requests
from tkinter.filedialog import asksaveasfile
from bs4 import BeautifulSoup
from recipe import Recipe


class EventHandler:
    def __init__(self, app):
        self.app = app

    def find_random_recipe(self):
        recipe_data = self.get_recipe_data()
        recipe = self.create_recipe(recipe_data)
        self.format_recipe(recipe)
        self.update_fields(recipe)

    def get_recipe_data(self):
        api_endpoint = f"https://api.spoonacular.com/recipes/random?apiKey={self.app.configuration['api_key']}"
        response = requests.get(api_endpoint)
        return response.json()["recipes"][0]

    def create_recipe(self, recipe_data):
        title = self.get_recipe_title(recipe_data)
        summary = self.get_recipe_summary(recipe_data)
        instructions = self.get_recipe_instructions(recipe_data)
        ingredients = self.get_recipe_ingredients(recipe_data)
        return Recipe(title=title, summary=summary, instructions=instructions, ingredients=ingredients)

    def get_recipe_title(self, recipe_data):
        return recipe_data.get("title", "")

    def get_recipe_summary(self, recipe_data):
        return recipe_data.get("summary", "")

    def get_recipe_instructions(self, recipe_data):
        return recipe_data["analyzedInstructions"][0].get("steps", [])

    def get_recipe_ingredients(self, recipe_data):
        return recipe_data.get("extendedIngredients", [])

    def format_recipe(self, recipe):
        recipe.title = self.format_recipe_title(recipe.title)
        recipe.summary = self.format_recipe_summary(recipe.summary)
        recipe.instructions = self.format_recipe_instructions(recipe.instructions)
        recipe.ingredients = self.format_recipe_ingredients(recipe.ingredients)

    def format_recipe_title(self, title):
        title = self.remove_html_tags(title)
        title = f"- {title} -"
        return title

    def format_recipe_summary(self, summary):
        summary = self.remove_html_tags(summary)
        summary = summary.split(". ")
        summary = ". ".join(summary[:-1]) + "."
        return summary

    def format_recipe_instructions(self, instructions):
        listed_instructions = []
        for instruction in instructions:
            listed_instructions.append(f"{instruction['number']}. {instruction['step']}")
        instructions = "\n".join(listed_instructions)
        return instructions

    def format_recipe_ingredients(self, ingredients):
        list_char = u"\u2022"
        listed_ingredients = []
        for ingredient in ingredients:
            listed_ingredients.append(f"{list_char} {ingredient['original']}")
        ingredients = "\n".join(listed_ingredients)
        return ingredients

    def remove_html_tags(self, text):
        text_formatter = BeautifulSoup(text, "html.parser")
        return text_formatter.get_text()

    def update_fields(self, recipe):
        self.update_label_field(self.app.recipe_title_label, recipe.title)
        self.update_text_field(self.app.recipe_summary_text, recipe.summary)
        self.update_text_field(self.app.recipe_instructions_text, recipe.instructions)
        self.update_text_field(self.app.recipe_ingredients_text, recipe.ingredients)

    def update_label_field(self, label_field, new_text):
        label_field.config(text=new_text)

    def update_text_field(self, text_field, new_text):
        self.enable_text_field(text_field)
        text_field.delete("1.0", "end")
        text_field.insert("end", new_text)
        self.disable_text_field(text_field)

    def enable_text_field(self, text_field):
        text_field.config(state="normal")

    def disable_text_field(self, text_field):
        text_field.config(state="disabled")

    def save_recipe(self):
        recipe_title = self.app.recipe_title_label.cget("text")
        recipe_summary = self.app.recipe_summary_text.get(1.0, "end")
        recipe_instructions = self.app.recipe_instructions_text.get(1.0, "end")
        recipe_ingredients = self.app.recipe_ingredients_text.get(1.0, "end")
        file_types = [("Text Document", "*.txt"), ("Word Document", "*.docx"), ("All Files", "*.*")]
        file = asksaveasfile(filetypes=file_types)
        recipe = open(file.name, "w")
        recipe.write(recipe_title + "\n" + recipe_summary + "\n\nIngredients:\n" + recipe_ingredients + "\n\nInstructions:\n" + recipe_instructions)
        recipe.close()

    def exit_application(self):
        self.app.destroy()
