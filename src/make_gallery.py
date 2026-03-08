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


def html_gallery_generator(dir: Path):
	if isinstance(dir, Path):
		pass
	else:
		dir = Path(dir)
    # HTML template as a raw string
	html_template = '''<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<style>
		body {
			padding: 20px;
		}

		.grid {
			column-count: 3;
			column-gap: 20px;
			max-width: 1600px;
			margin: 0 auto;
		}

		img {
			width: 100%;
			height: auto;
			border-radius: 8px;
			display: block;
			margin-bottom: 20px;
			break-inside: avoid;
		}

		@media (min-width: 1200px) {
			.grid {
				column-count: 3;
				column-gap: 25px;
				max-width: 1600px;
			}
		}

		/* Optional: adjust columns for smaller screens */
		@media (max-width: 768px) {
			.grid {
				column-count: 2;
				column-gap: 15px;
			}
		}
		</style>
	</head>
	<body>
		<div class="grid">
			{image_tags}
		</div>
	</body>
	</html>'''

	# Format the template with your image tags
	# Join the tags with newline and proper indentation (8 spaces)
	image_tags = generate_image_tags(dir)
	formatted_tags = '\n        '.join(image_tags)
	# final_html = html_template.format(image_tags=formatted_tags)
	final_html = html_template.replace('{image_tags}', formatted_tags)

	# Write to file
	output_path = Path("gallery.html")
	with open(output_path, 'w', encoding='utf-8') as f:
		f.write(final_html)