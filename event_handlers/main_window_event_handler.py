import textwrap
import requests as requests
from tkinter import messagebox
from bs4 import BeautifulSoup

from event_handlers.event_handler import EventHandler
from data_models.recipe import Recipe
from windows.about_window import AboutWindow
from windows.settings_window import SettingsWindow


class MainWindowEventHandler(EventHandler):
    def find_random_recipe(self):
        recipe_data = self.get_recipe_data()
        recipe = self.create_recipe(recipe_data)
        self.format_recipe(recipe)
        self.update_fields(recipe)

    def get_recipe_data(self):
        api_url = self.get_value_from_configuration("base_api_url")
        api_key = self.get_value_from_configuration("api_key")
        api_endpoint = api_url.format(api_key)
        try:
            response = requests.get(api_endpoint)

            return response.json()["recipes"][0]
        except requests.HTTPError as exception:
            messagebox.showwarning("Error", f"Error: {exception}")

    def create_recipe(self, recipe_data):
        title = self.get_recipe_title(recipe_data)
        description = self.get_recipe_description(recipe_data)
        instructions = self.get_recipe_instructions(recipe_data)
        ingredients = self.get_recipe_ingredients(recipe_data)

        return Recipe(title=title, description=description, instructions=instructions, ingredients=ingredients)

    def get_recipe_title(self, recipe_data):
        return recipe_data.get("title", "")

    def get_recipe_description(self, recipe_data):
        return recipe_data.get("summary", "")

    def get_recipe_instructions(self, recipe_data):
        recipe_id = recipe_data.get("id", "")
        api_url = self.get_value_from_configuration("additional_api_url")
        api_key = self.get_value_from_configuration("api_key")
        api_endpoint = api_url.format(recipe_id, api_key)
        try:
            response = requests.get(api_endpoint)

            return response.json()[0].get("steps", [])
        except requests.HTTPError as exception:
            messagebox.showwarning("Error", f"Error: {exception}")

    def get_recipe_ingredients(self, recipe_data):
        return recipe_data.get("extendedIngredients", [])

    def format_recipe(self, recipe):
        recipe.title = self.format_recipe_title(recipe.title)
        recipe.description = self.format_recipe_description(recipe.description)
        recipe.instructions = self.format_recipe_instructions(recipe.instructions)
        recipe.ingredients = self.format_recipe_ingredients(recipe.ingredients)

    def format_recipe_title(self, title):
        title = self.remove_html_tags(title)

        return title

    def format_recipe_description(self, description):
        description = self.remove_html_tags(description)
        description = description.split(". ")
        description = ". ".join(description[:-1]) + "."
        description = self.wrap_text(description)

        return description

    def wrap_text(self, text_to_wrap):
        wrapper = textwrap.TextWrapper(width=120)
        wrapped_text = wrapper.wrap(text=text_to_wrap)

        return "\n".join(wrapped_text)

    def format_recipe_instructions(self, instructions):
        listed_instructions = []
        for instruction in instructions:
            listed_instructions.append(self.wrap_text(f"{instruction['number']}. {instruction['step']}"))
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
        self.update_label_field(self.window.recipe_title_header, recipe.title)
        self.update_label_field(self.window.recipe_description_content, recipe.description)
        self.update_label_field(self.window.recipe_instructions_content, recipe.instructions)
        self.update_label_field(self.window.recipe_ingredients_content, recipe.ingredients)

    def update_label_field(self, label_field, new_text):
        label_field.config(text=new_text)

    # def save_recipe(self):
    #     recipe_title = self.app.recipe_title_label.cget("text")
    #     recipe_summary = self.app.recipe_summary_text.get(1.0, "end")
    #     recipe_instructions = self.app.recipe_instructions_text.get(1.0, "end")
    #     recipe_ingredients = self.app.recipe_ingredients_text.get(1.0, "end")
    #     file_types = [("Text Document", "*.txt"), ("Word Document", "*.docx"), ("All Files", "*.*")]
    #     file = asksaveasfile(filetypes=file_types)
    #     recipe = open(file.name, "w")
    #     recipe.write(recipe_title + "\n" + recipe_summary + "\n\nIngredients:\n" + recipe_ingredients + "\n\nInstructions:\n" + recipe_instructions)
    #     recipe.close()

    def open_settings(self):
        settings_window = SettingsWindow(self.window)

    def open_about(self):
        about_window = AboutWindow(self.window)

    def exit(self):
        self.window.destroy()

    def save_recipe(self):
        self.window.destroy()