import tkinter as tk
from tkinter import messagebox

from sqlalchemy import null
from dialog.menudialog import MenuDialog
import style
import dialog
import logic.dbservice as dataBase
import os


class LoginDialog(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Logowanie", font=style.labelFont)
        label.pack(pady=style.labelpady)


        # TODO: pola tk.Entry z nazwą użytkownika i hasłem

        labelUsrId = tk.Label(self, text="Nazwa użytkownika:", font=style.labelFontDesc)
        labelUsrId.pack(pady=style.labelpady)

        userId = tk.Entry(self)
        userId.pack()

        labelUsrPwd = tk.Label(self, text="Hasło użytkownika:", font=style.labelFontDesc)
        labelUsrPwd.pack(pady=style.labelpady)

        userPwd = tk.Entry(self, show="*")
        userPwd.pack()

        
        

        button = tk.Button(self, text="Zaloguj się", font=style.buttonFont, command=lambda: self.button_click(userId.get(), userPwd.get()))
        button.pack(pady=style.buttonpady)

        
    def button_click(self, userId, userPwd):
        # TODO: logika weryfikacji użytkownika w bazie danych
        # TODO: dane poprawne -> przejście do MenuDialog
        # TODO: dane niepoprawne -> okienko z komunikatem o błędzie logowania
        # TODO: zalogowany użytkownik musi być jakoś trzymany w aplikacji, bo jest potrzebny w innych miejscach
        

        db = dataBase.DataBase()
        result = db.check_login_data(username=userId, password=userPwd)

        if result:
            os.environ['currentUser'] = userId
            self.controller.frames[dialog.menudialog.MenuDialog].update_user()
            self.controller.show_frame(dialog.menudialog.MenuDialog)
            #print('OK')     
        else:
            #print('Wrong')
            messagebox.showerror('Błąd!','Błędny: login lub hasło')
