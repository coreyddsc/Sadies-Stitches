import unittest
import os

from src.image_tools import *

class BaseCaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dir = Path(os.getcwd())
        

class TestGetImageNames(BaseCaseTest):
    def test_get_image_names(self):
        imgs = get_image_names(dir = self.dir)
        print(imgs)
        

class TestConvertJPG2PNG(BaseCaseTest):
    def test_convert_jpg2png(self):
        convert_jpg2png(dir = self.dir, unlink=True)
        
        
class TestGetAspectRatio(BaseCaseTest):
    def test_get_aspect_ratio(self):
        imgs = get_image_names(self.dir)
        img_dir = self.dir / "images" / "gallery" / imgs[0]
        aspect_ratio = get_aspect_ratio(img_dir)
        print(f"Test Image Aspect Ratio: {aspect_ratio}")
        
        
class TestClassifyByAspectRatio(BaseCaseTest):
    def test_classify_by_aspect_ratio(self):
        img_class = classify_by_aspect_ratio(self.dir)
        for k, v in img_class.items():
            print(f"Image Name: {k} | Aspect Ratio: {v[0]} | Classification: {v[1]}")