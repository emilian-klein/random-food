import json
import tkinter as tk
from event_handler import EventHandler


class RandomRecipe(tk.Tk):
    """
    Application main class.
    """

    def __init__(self):
        """
        Initialize the RandomRecipe Tkinter application. Sets up the window properties, font styles and widgets.
        """
        super().__init__()
        self.title("Random Recipe")
        self.iconbitmap("images/icon.ico")
        self.geometry("1100x600")
        self.resizable(False, False)
        self.sm_n_font_style = ("Bahnschrift", "11", "normal")
        self.lg_n_font_style = ("Bahnschrift", "14", "normal")
        self.sm_b_font_style = ("Bahnschrift", "11", "bold")
        self.lg_b_font_style = ("Bahnschrift", "14", "bold")
        self.configuration = None
        self.event_handler = EventHandler(self)

        self.left_frame = tk.Frame(bg="#404040")
        self.left_frame.place(x=0, y=0, height=600, width=200)

        self.find_random_recipe_button = tk.Button(self.left_frame, text="Find random recipe", command=self.event_handler.find_random_recipe,
                                                   font=self.sm_b_font_style, cursor="hand2", bg="#439BFF", fg="#FFFFFF")
        self.find_random_recipe_button.place(x=25, y=25, height=50, width=150)

        self.save_recipe_button = tk.Button(self.left_frame, text="Save recipe", command=self.event_handler.save_recipe, font=self.sm_b_font_style,
                                            cursor="hand2", bg="#439BFF", fg="#FFFFFF")
        self.save_recipe_button.place(x=25, y=125, height=50, width=150)

        self.exit_button = tk.Button(self.left_frame, text="Exit", command=self.event_handler.exit_application, font=self.sm_b_font_style, cursor="hand2",
                                     bg="#439BFF", fg="#FFFFFF")
        self.exit_button.place(x=25, y=225, height=50, width=150)

        self.right_frame = tk.Frame()
        self.right_frame.place(x=200, y=0, height=600, width=900)

        self.recipe_title_label = tk.Label(self.right_frame, font=self.lg_b_font_style, bg="#696969", fg="#439BFF", anchor="w", padx=10)
        self.recipe_title_label.place(x=0, y=0, height=50, width=900)

        self.recipe_summary_label = tk.Label(self.right_frame, font=self.sm_b_font_style, bg="#696969", fg="#439BFF", text="- Description -", anchor="w", padx=10)
        self.recipe_summary_label.place(x=0, y=50, height=25, width=600)
        self.recipe_summary_text = tk.Text(self.right_frame, font=self.sm_n_font_style, bg="#696969", fg="#FFFFFF", wrap="word", state="disabled",
                                           relief="flat", padx=10, cursor="double_arrow")
        self.recipe_summary_text.place(x=0, y=75, height=200, width=600)

        self.recipe_instructions_label = tk.Label(self.right_frame, font=self.sm_b_font_style, bg="#696969", fg="#439BFF", text="- Instructions -",
                                                  anchor="w", padx=10)
        self.recipe_instructions_label.place(x=0, y=275, height=25, width=600)
        self.recipe_instructions_text = tk.Text(self.right_frame, font=self.sm_n_font_style, bg="#696969", fg="#FFFFFF", wrap="word", state="disabled",
                                                relief="flat", padx=10, cursor="double_arrow")
        self.recipe_instructions_text.place(x=0, y=300, height=350, width=600)

        self.recipe_ingredients_label = tk.Label(self.right_frame, font=self.sm_b_font_style, bg="#696969", fg="#439BFF", text="- Ingredients -",
                                                 anchor="center")
        self.recipe_ingredients_label.place(x=600, y=50, height=25, width=300)
        self.recipe_ingredients_text = tk.Text(self.right_frame, font=self.sm_n_font_style, bg="#696969", fg="#FFFFFF", wrap="word", state="disabled",
                                               relief="flat", cursor="double_arrow")
        self.recipe_ingredients_text.place(x=600, y=75, height=525, width=300)

    def get_configuration(self):
        with open("configuration.json") as file:
            self.configuration = json.load(file)


if __name__ == "__main__":
    app = RandomRecipe()
    app.get_configuration()
    app.event_handler.find_random_recipe()
    app.mainloop()
