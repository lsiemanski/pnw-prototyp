import unittest

from numpy import double

from app import App
import logic.nnlogic
from os.path import exists


class NNLogicTest(unittest.TestCase):
    def test_train_model(self):
        nn = logic.nnlogic.NN()
        nn.train_network()
        self.assertTrue(exists('../trained_NN.json'))

    def test_predict(self):
        nn = logic.nnlogic.NN()
        data = {'rozpietosc' : 100,
         'wysokosc przekroju' : 100, 
         'Modul Younga stali' : 100.0, 
         'stopien zbrojenia' : 5, 
         'Obciazenie' : 21,
         'szerokosc przekroju' : 43, 
         'otulina' : 98.1,
         'srednica zbrojenia' : 77, 
         'Wytrzymalosc betonu na rozciaganie' : 51.2,
         'Modul Younga betonu' : 97}
        predicted = nn.predict(data)
        self.assertTrue(predicted != None and predicted is double)

    def test_create_model(self):
        nn = logic.nnlogic.NN()
        model = nn.create_model()
        self.assertTrue(model != None)

