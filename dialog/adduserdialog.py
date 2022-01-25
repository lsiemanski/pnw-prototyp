import tkinter as tk
import style
import dialog
from tkinter import ttk, messagebox
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


    def add_user(self):
        if self.username_entry.get() == '' or self.password_entry.get() == '' or self.role_combobox.get() == '':
            messagebox.showerror('Błąd','Żadne z pól nie może być puste!')
            return

        try:
            self.db.insert_user(self.username.get(), self.password.get(), '', self.role.get())
            self.username.set('')
            self.password.set('')
            self.role.set('')
            messagebox.showinfo("Sukces!", "Użytkownik dodany!")
            self.controller.show_frame(dialog.menudialog.MenuDialog)
        except UserError as error:
            messagebox.showerror("Błąd!", str(error))



