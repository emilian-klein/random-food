import textwrap
import requests as requests
from tkinter import messagebox, filedialog
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

from event_handlers.event_handler import EventHandler
from entity.recipe import Recipe
from windows.about_window import AboutWindow
from windows.settings_window import SettingsWindow


class MainWindowEventHandler(EventHandler):
    def find_random_recipe(self):
        # try:
        recipe_data = self.get_recipe_data()
        recipe = self.create_recipe(recipe_data)
        self.format_recipe(recipe)
        self.update_fields(recipe)
        # except Exception:
        #     messagebox.showwarning("Error", f"Error occurred! Your API key might be invalid!")

    def get_recipe_data(self):
        api_url = self.get_value_from_configuration("recipe_api_url")
        api_key = self.get_value_from_configuration("api_key")
        api_endpoint = api_url.format(api_key)
        response = requests.get(api_endpoint)

        return response.json()["recipes"][0]

    def create_recipe(self, recipe_data):
        title = self.get_recipe_title(recipe_data)
        image = self.get_recipe_image(recipe_data)
        description = self.get_recipe_description(recipe_data)
        ingredients = self.get_recipe_ingredients(recipe_data)
        instructions = self.get_recipe_instructions(recipe_data)

        return Recipe(title=title, image=image, description=description, ingredients=ingredients, instructions=instructions)

    def get_recipe_title(self, recipe_data):
        return recipe_data.get("title", "")

    def get_recipe_image(self, recipe_data):
        image_link = recipe_data.get("image", "")
        response = requests.get(image_link)
        with open("images/recipe_image.jpg", "wb") as file:
            file.write(response.content)

        return image_link

    def get_recipe_description(self, recipe_data):
        return recipe_data.get("summary", "")

    def get_recipe_ingredients(self, recipe_data):
        return recipe_data.get("extendedIngredients", [])

    def get_recipe_instructions(self, recipe_data):
        recipe_id = recipe_data.get("id", "")
        api_url = self.get_value_from_configuration("recipe_instructions_api_url")
        api_key = self.get_value_from_configuration("api_key")
        api_endpoint = api_url.format(recipe_id, api_key)
        response = requests.get(api_endpoint)

        return response.json()[0].get("steps", [])

    def format_recipe(self, recipe):
        recipe.title = self.format_recipe_title(recipe.title)
        recipe.description = self.format_recipe_description(recipe.description)
        recipe.ingredients = self.format_recipe_ingredients(recipe.ingredients)
        recipe.instructions = self.format_recipe_instructions(recipe.instructions)

    def format_recipe_title(self, title):
        title = self.remove_html_tags(title)

        return title

    def remove_html_tags(self, text):
        text_formatter = BeautifulSoup(text, "html.parser")

        return text_formatter.get_text()

    def format_recipe_description(self, description):
        description = self.remove_html_tags(description)
        description = description.split(". ")
        description = ". ".join(description[:-1]) + "."
        description = self.wrap_text(description)

        return description

    def wrap_text(self, text_to_wrap):
        wrapper = textwrap.TextWrapper(width=130)
        wrapped_text = wrapper.wrap(text=text_to_wrap)

        return "\n".join(wrapped_text)

    def format_recipe_ingredients(self, ingredients):
        list_char = u"\u2022"
        listed_ingredients = []
        for ingredient in ingredients:
            listed_ingredients.append(f"{list_char} {ingredient['original']}")
        ingredients = "\n".join(listed_ingredients)

        return ingredients

    def format_recipe_instructions(self, instructions):
        listed_instructions = []
        for instruction in instructions:
            listed_instructions.append(f"{instruction['number']}. {instruction['step']}")
        instructions = "\n".join(listed_instructions)

        return instructions

    def update_fields(self, recipe):
        self.update_label_field(self.window.recipe_title_header, new_text=recipe.title)
        self.update_label_field(self.window.recipe_description_content, new_text=recipe.description)
        self.update_label_field(self.window.recipe_instructions_content, new_text=recipe.instructions)
        self.update_label_field(self.window.recipe_ingredients_content, new_text=recipe.ingredients)
        self.update_label_field(self.window.recipe_image, path_to_image="images/recipe_image.jpg")

    def update_label_field(self, label_field, new_text=None, path_to_image=None):
        if new_text:
            label_field.config(text=new_text)
        if path_to_image:
            new_image = Image.open(path_to_image)
            new_image.thumbnail((300, 300))
            img = ImageTk.PhotoImage(new_image)
            self.window.recipe_image.config(image=img)
            self.window.recipe_image.image = img

    def save_recipe(self):
        title = self.window.recipe_title_header.cget("text")
        description = self.window.recipe_description_content.cget("text").replace("\n", " ")
        ingredients = self.window.recipe_ingredients_content.cget("text")
        instructions = self.window.recipe_instructions_content.cget("text")
        file_types = [("Text Document", "*.txt"), ("Word Document", "*.docx"), ("All Files", "*.*")]
        file = filedialog.asksaveasfile(filetypes=file_types, defaultextension="txt")
        with open(file.name, "w") as recipe_file:
            recipe_file.write(title + "\n" + description + "\n\nIngredients:\n" + ingredients + "\n\nInstructions:\n" + instructions)

    def open_settings(self):
        SettingsWindow(self.window)

    def open_about(self):
        AboutWindow(self.window)

    def exit(self):
        self.window.destroy()
