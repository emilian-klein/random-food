import tkinter as tk
from tkinter import ttk

from custom_widgets.menu_button import MenuButton
from custom_widgets.content_label import ContentLabel
from custom_widgets.title_label import TitleLabel
from event_handlers.main_window_event_handler import MainWindowEventHandler


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Recipe")
        self.iconbitmap("images/icon.ico")
        self.geometry("1100x600")
        self.resizable(False, False)
        self.configuration = None
        self.event_handler = MainWindowEventHandler(self)

        self.left_frame = tk.Frame(bg="#404040")
        self.left_frame.pack(side="left", fill="both")

        self.find_random_recipe_button = MenuButton(self.left_frame, text="Find random recipe", command=self.event_handler.find_random_recipe)
        self.find_random_recipe_button.pack(fill="x", padx=15, pady=(20, 0), ipady=5)

        self.save_recipe_button = MenuButton(self.left_frame, text="Save recipe", command=self.event_handler.save_recipe)
        self.save_recipe_button.pack(fill="x", padx=15, pady=(20, 0), ipady=5)

        self.settings_button = MenuButton(self.left_frame, text="Settings", command=self.event_handler.open_settings)
        self.settings_button.pack(fill="x", padx=15, pady=(20, 0), ipady=5)

        self.about_button = MenuButton(self.left_frame, text="About", command=self.event_handler.open_about)
        self.about_button.pack(fill="x", padx=15, pady=(20, 0), ipady=5)

        self.exit_button = MenuButton(self.left_frame, text="Exit", command=self.event_handler.exit)
        self.exit_button.pack(fill="x", padx=15, pady=(20, 0), ipady=5)

        self.right_frame_wrapper = tk.Frame()
        self.right_frame_wrapper.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(self.right_frame_wrapper, highlightthickness=0, bd=0, bg="#d1d1d1")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.right_frame_wrapper, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.right_frame = tk.Frame(self.canvas)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.right_frame, anchor="nw")

        self.right_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_frame, width=e.width))

        self.recipe_title_header = TitleLabel(self.right_frame, text="Welcome in Random Recipe!")
        self.recipe_title_header.pack(fill="x")

        self.recipe_image = tk.Label(self.right_frame, bg="#d1d1d1")
        self.recipe_image.pack(fill="x")

        self.recipe_description_header = TitleLabel(self.right_frame)
        self.recipe_description_header.pack(fill="x")

        self.recipe_description_content = ContentLabel(self.right_frame)
        self.recipe_description_content.pack(fill="x")

        self.recipe_ingredients_header = TitleLabel(self.right_frame)
        self.recipe_ingredients_header.pack(fill="x")

        self.recipe_ingredients_content = ContentLabel(self.right_frame)
        self.recipe_ingredients_content.pack(fill="x")

        self.recipe_instructions_header = TitleLabel(self.right_frame)
        self.recipe_instructions_header.pack(fill="x")

        self.recipe_instructions_content = ContentLabel(self.right_frame)
        self.recipe_instructions_content.pack(fill="x")

        self.event_handler.disable_button(self.save_recipe_button)
