import unittest

from app import App
import dialog

class LoginDialogTest(unittest.TestCase):
    def test_login(self):
        app = App()
        log_dialog = dialog.logindialog.LoginDialog(app.container, app)
        log_dialog.buttonClick('michal27', '123456')
        assert(os.environ['currentUser'] = userId)