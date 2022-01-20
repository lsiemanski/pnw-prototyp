import tkinter as tk
import style
import dialog
from tkinter import ttk

from logic.entity.User import User


class AddUserDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.add_go_to_main_menu_button()

        label = tk.Label(self, text="Dodaj użytkownika", font=style.labelFont)
        label.pack(pady=style.labelpady)

        self.username = tk.StringVar()
        username_label = tk.Label(self, text="Nazwa użytkownika", font=style.entryLabelFont)
        username_label.pack()
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.username_entry.pack()

        self.password = tk.StringVar()
        password_label = tk.Label(self, text="Hasło", font=style.entryLabelFont)
        password_label.pack()
        self.password_entry = tk.Entry(self, textvariable=self.password, show="*")
        self.password_entry.pack()

        self.role = tk.StringVar()
        role_label = tk.Label(self, text="Rola", font=style.entryLabelFont)
        role_label.pack()
        self.role_combobox = ttk.Combobox(self, textvariable=self.role, width=30)
        self.role_combobox['values'] = ('Inżynier', 'Pracownik laboratorium')
        self.role_combobox['state'] = 'readonly'
        self.role_combobox.pack()

        button = tk.Button(self, text="Dodaj", font=style.buttonFont, command=self.add_user)
        button.pack(pady=style.buttonpady)

        self.empty_username_label = tk.Label(self, text="Wprowadź nazwę użytkownika!", font=style.errorLabelFont,
                                             fg=style.errorLabelFontColor)
        self.empty_password_label = tk.Label(self, text="Wprowadź hasło!", font=style.errorLabelFont,
                                        fg=style.errorLabelFontColor)
        self.empty_role_label = tk.Label(self, text="Wybierz rolę!", font=style.errorLabelFont,
                                    fg=style.errorLabelFontColor)

    def add_user(self):
        if self.validate():
            user = User(self.username.get(), self.password.get(), self.role.get())
            self.username.set('')
            self.password.set('')
            self.role.set('')
        # TODO: zapisz usera w bazie
        # TODO: komunikat jak się udało
        # TODO: powrót do menu głównego po zapisie

    def validate(self):
        correct_login = self.validate_login()
        correct_password = self.validate_password()
        correct_role = self.validate_role()
        return correct_login and correct_password and correct_role

    def validate_login(self):
        if self.username.get():
            self.empty_username_label.forget()
        else:
            self.empty_username_label.pack()
        return self.username.get() != ''

    def validate_password(self):
        if self.password.get():
            self.empty_password_label.pack_forget()
        else:
            self.empty_password_label.pack()
        return self.password.get() != ''

    def validate_role(self):
        if self.role.get():
            self.empty_role_label.pack_forget()
        else:
            self.empty_role_label.pack()
        return self.role.get() != ''
