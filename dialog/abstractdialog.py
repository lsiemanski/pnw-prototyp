import tkinter as tk
import style
import dialog


class AbstractDialog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def go_to_main_menu(self):
        self.controller.show_frame(dialog.menudialog.MenuDialog)

    def add_go_to_main_menu_button(self):
        button = tk.Button(self, text="Wróć do menu głównego", font=style.buttonFont, command=self.go_to_main_menu)
        button.pack(anchor=tk.NE, pady=style.buttonpady, padx=style.buttonpadx)

