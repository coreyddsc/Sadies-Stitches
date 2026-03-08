import os
from pathlib import Path

try:
	from src.image_tools import *
except:
	from .image_tools import *
	
def generate_image_tags(dir: Path):
	if isinstance(dir, Path):
		pass
	else:
		dir = Path(dir)
	img_dir = "images/gallery"	
	aspect_class = classify_by_aspect_ratio(dir)
	image_tags = []
	for img, cls in aspect_class.items():
		img_path = rf"{img_dir}/{img}"
		classification = cls[1]
		img_tag = rf'<img src="{img_path}" class="{classification}" alt="">'
		image_tags.append(img_tag)
	return image_tags


def html_gallery_generator():
    pass