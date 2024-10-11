import textwrap
import requests
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

from event_handlers.event_handler import EventHandler
from entity.recipe import Recipe
from windows.about_window import AboutWindow
from windows.settings_window import SettingsWindow


class MainWindowEventHandler(EventHandler):
    def __init__(self, window):
        super().__init__(window)
        self.recipe = Recipe()

    def find_random_recipe(self):
        try:
            recipe_data = self.get_recipe_data()
            self.recipe = self.create_recipe(recipe_data)
            self.update_fields_in_window()
            self.enable_button(self.window.save_recipe_button)
        except Exception as e:
            messagebox.showerror("Error", "An error occurred! Try again or check your API key!")

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
        source_url = self.get_recipe_source_url(recipe_data)
        return Recipe(title=title, image=image, description=description, ingredients=ingredients, instructions=instructions, source_url=source_url)

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

    def get_recipe_source_url(self, recipe_data):
        return recipe_data.get("sourceUrl", "")

    def update_fields_in_window(self):
        self.update_label_field(self.window.recipe_title_header, new_text=self.format_recipe_title(self.recipe.title))
        self.update_label_field(self.window.recipe_image, new_image="images/recipe_image.jpg")
        self.update_label_field(self.window.recipe_description_header, new_text="Description")
        self.update_label_field(self.window.recipe_description_content, new_text=self.format_recipe_description(self.recipe.description, "window"))
        self.update_label_field(self.window.recipe_ingredients_header, new_text="Ingredients")
        self.update_label_field(self.window.recipe_ingredients_content, new_text=self.format_recipe_ingredients(self.recipe.ingredients))
        self.update_label_field(self.window.recipe_instructions_header, new_text="Instructions")
        self.update_label_field(self.window.recipe_instructions_content, new_text=self.format_recipe_instructions(self.recipe.instructions, "window"))
        self.update_label_field(self.window.recipe_source_header, new_text="Recipe source")
        self.update_label_field(self.window.recipe_source_content, new_text=self.recipe.source_url)

    def update_label_field(self, label_field, new_text=None, new_image=None):
        if new_text:
            label_field.config(text=new_text)
        if new_image:
            image = Image.open(new_image)
            image.thumbnail((300, 300))
            label_img = ImageTk.PhotoImage(image)
            label_field.config(image=label_img)
            label_field.image = label_img

    def format_recipe_title(self, title):
        title = self.remove_html_tags(title)
        return title

    def remove_html_tags(self, text):
        text_formatter = BeautifulSoup(text, "html.parser")
        return text_formatter.get_text()

    def format_recipe_description(self, description, destination):
        description = self.remove_html_tags(description)
        description = description.split(". ")
        description = ". ".join(description[:-1]) + "."
        if destination == "window":
            return self.wrap_text(description)
        if destination == "file":
            return description

    def wrap_text(self, text_to_wrap):
        wrapper = textwrap.TextWrapper(width=130)
        wrapped_text = wrapper.wrap(text=text_to_wrap)
        return "\n".join(wrapped_text)

    def format_recipe_ingredients(self, ingredients):
        list_char = u"\u2022"
        formatted_ingredients = []
        for ingredient in ingredients:
            name = ingredient["originalName"]
            amount = int(ingredient["measures"]["metric"]["amount"])
            unit = ingredient["measures"]["metric"]["unitLong"]
            if unit:
                formatted_ingredients.append(f"{list_char} {name} ({amount} {unit})")
            else:
                formatted_ingredients.append(f"{list_char} {amount} {name}")
        ingredients = "\n".join(formatted_ingredients)
        return ingredients

    def format_recipe_instructions(self, instructions, destination):
        formatted_instructions = []
        for instruction in instructions:
            number = instruction["number"]
            step = instruction["step"]
            if destination == "window":
                formatted_instructions.append(self.wrap_text(f"{number}. {step}"))
            if destination == "file":
                formatted_instructions.append(f"{number}. {step}")
        instructions = "\n".join(formatted_instructions)
        return instructions

    def save_recipe(self):
        title = self.format_recipe_title(self.recipe.title)
        description = self.format_recipe_description(self.recipe.description, "file")
        ingredients = self.format_recipe_ingredients(self.recipe.ingredients)
        instructions = self.format_recipe_instructions(self.recipe.instructions, "file")
        source_url = self.recipe.source_url
        file_types = [("Text Document", "*.txt"), ("Word Document", "*.docx"), ("All Files", "*.*")]
        file = filedialog.asksaveasfile(filetypes=file_types, defaultextension="txt")
        if file:
            with open(file.name, "w", encoding="utf-8") as recipe_file:
                recipe_file.write(title + "\n\n")
                recipe_file.write(description + "\n\n")
                recipe_file.write("Ingredients" + "\n" + ingredients + "\n\n")
                recipe_file.write("Instructions" + "\n" + instructions + "\n\n")
                recipe_file.write("Link to original recipe: " + source_url)
            messagebox.showinfo("Information", "Recipe has been saved!")

    def open_settings(self):
        SettingsWindow(self.window)

    def open_about(self):
        AboutWindow(self.window)

    def exit(self):
        self.window.destroy()
