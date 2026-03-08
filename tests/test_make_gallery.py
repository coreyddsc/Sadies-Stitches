import unittest
import os

from src.make_gallery import *

class BaseCaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = Path(os.getcwd())
        
class TestGenerateImageTags(BaseCaseTest):
    def test_generate_image_tags(self):
        img_tags = generate_image_tags(self.dir)
        print(f"Gallery Image Tags:\n{img_tags}")