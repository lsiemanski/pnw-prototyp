import unittest

from app import App
import dialog.logindialog
import os
import logic.dbservice

class LoginDialogTest(unittest.TestCase):
    def test_login(self):
        app = App()
        db = logic.dbservice.DataBase()
        db.insert_user('michal27', '123456', 'm@example.com', 'Inzynier')
        log_dialog = dialog.logindialog.LoginDialog(app.container, app)
        log_dialog.buttonClick('michal27', '123456')
        self.assertTrue(os.environ['currentUser'] == 'michal27')