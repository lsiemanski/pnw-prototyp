import unittest

from app import App
import dialog
import logic.dbservice as db
import os

class PredictDialogTest(unittest.TestCase):
    def test_predict(self):
        app = App()
        predict_dialog = dialog.predictdialog.PredictDialog(app.container, app)
        os.environ['current_user'] = 'michal'
        predict_dialog.predict()
        results = db.DataBase().get_results_for_user(os.environ.get('michal'))
        self.assertTrue(len(results) > 0)

