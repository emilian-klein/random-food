import tkinter as tk

from event_handlers.settings_window_event_handler import SettingsWindowEventHandler


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.iconbitmap("images/icon.ico")
        self.geometry("420x100")
        self.resizable(False, False)
        self.configure(bg="#696969")
        self.event_handler = SettingsWindowEventHandler(self)

        self.api_key_frame = tk.Frame(self, bg="#696969")
        self.api_key_frame.pack(fill="x", pady=10)

        self.api_key_label = tk.Label(self.api_key_frame, text="API key", font=("Bahnschrift", "11", "bold"), bg="#696969", fg="#FFFFFF", width=13, anchor="w")
        self.api_key_label.pack(side="left", padx=5)

        self.api_key_sv = tk.StringVar()
        self.api_key_sv.set(self.event_handler.get_value_from_configuration("api_key"))
        self.api_key_entry = tk.Entry(self.api_key_frame, textvariable=self.api_key_sv, font=("Bahnschrift", "11", "normal"), width=35)
        self.api_key_entry.pack(side="left")

        self.buttons_frame = tk.Frame(self, bg="#696969")
        self.buttons_frame.pack(fill="x", padx=5)

        self.save_settings_button = tk.Button(self, text="Save", command=self.event_handler.save_settings, font=("Bahnschrift", "11", "bold"), width=15, bg="#75a832", fg="#FFFFFF", cursor="hand2")
        self.save_settings_button.pack(side="left", expand=True)
        self.bind("<Return>", self.event_handler.save_settings)

        self.close_settings_button = tk.Button(self, text="Close", command=self.event_handler.close_settings, font=("Bahnschrift", "11", "bold"), width=15, bg="#787878", fg="#FFFFFF", cursor="hand2")
        self.close_settings_button.pack(side="left", expand=True)

        self.transient(parent)
        self.grab_set()
        parent.wait_window(self)
