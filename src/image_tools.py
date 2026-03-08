import os
from pathlib import Path
import cv2

def get_image_names(dir: Path):
	if isinstance(dir, Path):
		pass
	else:
		dir = Path(dir)
	
	img_dir = dir / "images" / "gallery"
	imgs = os.listdir(img_dir)
	return imgs

def convert_jpg2png(dir: Path, unlink: bool = False):
	if isinstance(dir, Path):
		pass
	else:
		dir = Path(dir)
	img_dir = dir / "images" / "gallery"
	imgs = get_image_names(dir)
	for img_fname in imgs:
		if img_fname.endswith('.png'):
			continue
		
		jpg_path = img_dir / img_fname
		png_path = img_dir / rf"{Path(img_fname).stem}.png"

		img = cv2.imread(str(jpg_path))
		if img is not None:
			cv2.imwrite(str(png_path), img)
			if unlink:
				jpg_path.unlink()
			print(f"Converted {jpg_path.name} to {png_path.name}")
		else:
			print(f"Failed to read {jpg_path.name}")


def get_aspect_ratio(image_path: Path):
    img = cv2.imread(str(image_path))
    if img is None:
        return None
    
    height, width = img.shape[:2]
    aspect_ratio = width / height
    return aspect_ratio

def classify_aspect_ratio(aspect: float):
	if aspect > 1.1:  # Wider than tall
		classification = "landscape"
	elif aspect < 0.8:  # Taller than wide
		classification = "portrait"
	else:  # Roughly square
		classification = "square"
	return classification

def classify_by_aspect_ratio(dir: Path):
	if isinstance(dir, Path):
		pass
	else:
		dir = Path(dir)
	img_dir = dir / "images" / "gallery"
	imgs = get_image_names(dir)
	img_classifier = {}
	for img in imgs:
		img_path = img_dir / img
		aspect_ratio = get_aspect_ratio(img_path)
		classification = classify_aspect_ratio(aspect_ratio)
		img_classifier.setdefault(img, (aspect_ratio, classification))

	return img_classifier