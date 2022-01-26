import unittest

from app import App
import dialog
import logic.dbservice as db
import os

class PredictDialogTest(unittest.TestCase):
    def test_predict(self):
        predict_dialog = dialog.predictdialog.PredictDialog()
        predict_dialog.predict()
        os.environ['current_user'] = 'michal'
        results = db.DataBase().get_results_for_user(os.environ.get('michal'))
        assert(len(results) > 0)

