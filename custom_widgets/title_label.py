import tkinter as tk


class TitleLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Bahnschrift", "14", "bold"), bg="#d1d1d1", anchor="w", justify="left", padx=10, pady=5)
