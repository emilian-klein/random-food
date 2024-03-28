import tkinter as tk
from tkinter import ttk
from custom_widgets.custom_button import CustomButton
from custom_widgets.custom_content_label import CustomContentLabel
from custom_widgets.custom_header_label import CustomHeaderLabel
from custom_widgets.custom_separator import CustomSeparator
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

        self.find_random_recipe_button = CustomButton(self.left_frame, text="Find random recipe", command=self.event_handler.find_random_recipe)
        self.find_random_recipe_button.pack(fill="x", padx=10, pady=10, ipady=5)

        self.save_recipe_button = CustomButton(self.left_frame, text="Save recipe", command=self.event_handler.save_recipe)
        self.save_recipe_button.pack(fill="x", padx=10, pady=10, ipady=5)

        self.settings_button = CustomButton(self.left_frame, text="Settings", command=self.event_handler.open_settings)
        self.settings_button.pack(fill="x", padx=10, pady=10, ipady=5)

        self.about_button = CustomButton(self.left_frame, text="About", command=self.event_handler.open_about)
        self.about_button.pack(fill="x", padx=10, pady=10, ipady=5)

        self.exit_button = CustomButton(self.left_frame, text="Exit", command=self.event_handler.exit)
        self.exit_button.pack(fill="x", padx=10, pady=10, ipady=5)

        self.right_frame = tk.Frame(bg="#696969")
        self.right_frame.pack(fill="both", expand=1)

        self.canvas = tk.Canvas(self.right_frame, bg="#696969", bd=0, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.right_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.second_right_frame = tk.Frame(self.canvas)
        self.second_right_frame.bind("<Configure>", self.configure_interior)

        self.canvas.create_window((0, 0), window=self.second_right_frame, anchor="nw")

        self.recipe_title_header = CustomHeaderLabel(self.second_right_frame, text="Title")
        self.recipe_title_header.pack(fill="x")

        self.first_separator = CustomSeparator(self.second_right_frame)
        self.first_separator.pack(fill="x")

        self.recipe_description_header = CustomHeaderLabel(self.second_right_frame, text="Description")
        self.recipe_description_header.pack(fill="x")

        self.recipe_description_content = CustomContentLabel(self.second_right_frame, text="Description text")
        self.recipe_description_content.pack(fill="x")

        self.second_separator = CustomSeparator(self.second_right_frame)
        self.second_separator.pack(fill="x")

        self.recipe_instructions_header = CustomHeaderLabel(self.second_right_frame, text="Instructions")
        self.recipe_instructions_header.pack(fill="x")

        self.recipe_instructions_content = CustomContentLabel(self.second_right_frame, text="Instructions text")
        self.recipe_instructions_content.pack(fill="x")

        self.third_separator = CustomSeparator(self.second_right_frame)
        self.third_separator.pack(fill="x")

        self.recipe_ingredients_header = CustomHeaderLabel(self.second_right_frame, text="Ingredients")
        self.recipe_ingredients_header.pack(fill="x")

        self.recipe_ingredients_content = CustomContentLabel(self.second_right_frame, text="Ingredients text")
        self.recipe_ingredients_content.pack(fill="x")

    def configure_interior(self, event):
        size = (self.second_right_frame.winfo_reqwidth(), self.second_right_frame.winfo_reqheight())
        self.canvas.config(scrollregion=(0, 0, size[0], size[1]))
        if self.second_right_frame.winfo_reqwidth() != self.canvas.winfo_reqwidth():
            self.canvas.config(width=self.second_right_frame.winfo_reqwidth())


