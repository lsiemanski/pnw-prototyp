import unittest

from app import App
import dialog

class AddUserDialogTest(unittest.TestCase):
    def test_validate(self):
        app = App()
        add_user_dialog = dialog.adduserdialog.AddUserDialog(app.container, app)
        add_user_dialog.username.set('username')
        add_user_dialog.password.set('password')
        add_user_dialog.role.set('Inżynier')
        self.assertTrue(add_user_dialog.validate())

    def test_validate_password(self):
        app = App()
        add_user_dialog = dialog.adduserdialog.AddUserDialog(app.container, app)
        add_user_dialog.username.set('username')
        self.assertTrue(add_user_dialog.validate_login())
