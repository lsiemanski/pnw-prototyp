import unittest

from app import App
import dialog.historydialog


class HistoryDialogTest(unittest.TestCase):
    def test_update_data(self):
        app = App()
        history_dialog = dialog.historydialog.HistoryDialog(app.container, app)
        history_dialog.update_data()
        self.assertTrue(history_dialog.history != None)