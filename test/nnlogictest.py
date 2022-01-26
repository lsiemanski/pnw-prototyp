import unittest

from numpy import double

from app import App
import logic.nnlogic
from os.path import exists
import numpy as np

from logic.dbservice import DataBase


class NNLogicTest(unittest.TestCase):
    def test_train_model(self):
        DataBase().insert_sample({
            "span": 0.1,
            "section_height": 0.1,
            "steel_young_modulus": 0.1,
            "reinforcement_grade": 0.1,
            "load": 0.1,
            "section_width": 0.1,
            "cover": 0.2,
            "reinforcement_diameter": 0.1,
            "concrete_tensile_strength": 0.1,
            "concrete_young_modulus": 0.1
        }, 0.1)
        nn = logic.nnlogic.NN()
        nn.train_network()
        self.assertTrue(exists('../trained_NN.json'))

    def test_predict(self):
        nn = logic.nnlogic.NN()
        data = np.array([[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]])
        predicted = nn.predict(data)
        self.assertTrue(predicted != None)

    def test_create_model(self):
        nn = logic.nnlogic.NN()
        model = nn.create_model()
        self.assertTrue(model != None)

