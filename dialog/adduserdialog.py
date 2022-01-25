import tkinter as tk
import style
import dialog
from tkinter import ttk

from logic.dbservice import DataBase, UserError


class AddUserDialog(dialog.abstractdialog.AbstractDialog):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.db = DataBase()

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
            try:
                self.db.insert_user(self.username.get(), self.password.get(), '', self.role.get())
                self.username.set('')
                self.password.set('')
                self.role.set('')
                self.pop_window("Użytkownik dodany!")
                self.controller.show_frame(dialog.menudialog.MenuDialog)
            except UserError as error:
                self.pop_window(str(error))

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

    def pop_window(self, message):
        pop = tk.Toplevel(self)
        pop.geometry("300x150")
        pop.resizable(0, 0)
        label = tk.Label(pop, text=message, pady=style.labelpady, font=style.entryLabelFont)
        label.pack()
        button = tk.Button(pop, text="OK", pady=style.buttonpady, font=style.buttonFont, command=lambda: pop.destroy())
        button.pack()
        x = self.controller.winfo_x()
        y = self.controller.winfo_y()
        w = 300
        h = 90
        c_w = self.controller.winfo_width()
        c_h = self.controller.winfo_width()
        pop.geometry("%dx%d+%d+%d" % (w, h, x + (c_w-w)/2, y + (c_h-h)/2))

