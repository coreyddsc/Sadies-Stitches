import unittest
import os

from src.image_tools import *

class BaseCaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = os.getcwd()
        

class TestGetImageNames(BaseCaseTest):
    def test_get_image_names(self):
        imgs = get_image_names(dir = self.dir)
        print(imgs)
        

class TestConvertJPG2PNG(BaseCaseTest):
    def test_convert_jpg2png(self):
        convert_jpg2png(dir = self.dir, unlink=True)