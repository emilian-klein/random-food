import tkinter as tk
from PIL import ImageTk, Image


class AboutWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("About")
        self.iconbitmap("images/icon.ico")
        self.geometry("480x120")
        self.resizable(False, False)
        self.configure(bg="#d1d1d1")

        self.app_icon_image = ImageTk.PhotoImage(Image.open("images/icon.ico").resize((20, 20)))
        self.app_icon = tk.Label(self, image=self.app_icon_image, bg="#d1d1d1")
        self.app_icon.pack(pady=5)

        self.first_label = tk.Label(self, font=("Bahnschrift", "11", "bold"), text="Random Recipe", bg="#d1d1d1")
        self.first_label.pack()

        self.second_label = tk.Label(self, font=("Bahnschrift", "11", "normal"), text="Created by emilian-klein (www.github.com/emilian-klein).", bg="#d1d1d1")
        self.second_label.pack()

        self.third_label = tk.Label(self, font=("Bahnschrift", "11", "normal"), text="Recipe data provided using Spoonacular API (www.spoonacular.com).",
                                    bg="#d1d1d1")
        self.third_label.pack()

        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)
