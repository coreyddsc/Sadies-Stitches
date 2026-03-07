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


