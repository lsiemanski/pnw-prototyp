import tkinter as tk
import style
import dialog


class LoginDialog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Logowanie", font=style.labelFont)
        label.pack(pady=style.labelpady)

        # TODO: pola tk.Entry z nazwą użytkownika i hasłem

        button = tk.Button(self, text="Zaloguj się", font=style.buttonFont, command=self.button_click)
        button.pack(pady=style.buttonpady)

    def button_click(self):
        # TODO: logika weryfikacji użytkownika w bazie danych
        # TODO: dane poprawne -> przejście do MenuDialog
        # TODO: dane niepoprawne -> okienko z komunikatem o błędzie logowania
        # TODO: zalogowany użytkownik musi być jakoś trzymany w aplikacji, bo jest potrzebny w innych miejscach
        self.controller.show_frame(dialog.menudialog.MenuDialog)
