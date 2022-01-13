import tkinter as tk
import style
import dialog


class AddUserDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Dodaj użytkownika", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: pola tk.Entry z nazwą użytkownika i hasłem
        # TODO: pole combobox z rolą użytkownika - role to pracownik laboratorium oraz inżynier
        # TODO: tk.Button dodający użytkownika i wywołujący akcję zapisu do bazy
