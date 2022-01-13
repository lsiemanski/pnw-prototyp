import tkinter as tk
import style
import dialog


class HistoryDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Historia obliczeń", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: wymyślić jak to przedstawiać, bo nie mam pomysłu na teraz (może jakaś tabelka?)
        # TODO: na pewno trzeba będzie komunikację z bazą zrobić
