# mogrify -gravity center -crop 3000x3000+0+0 -resize 600x600 -strip -quality 75 *.jpg

from pathlib import Path

from jinja2 import Template


TEMPLATE_PATH = Path("index.html.template")
RESULT_PATH = Path("index.html")
IMAGE_DIR = Path("images")
THUMBNAIL_DIR = Path("thumbnails")

def get_image_info(img: Path):
    thumbnail = THUMBNAIL_DIR / img.name
    return {"image": "{}/{}".format(IMAGE_DIR.relative_to("."), img.name),
            "thumbnail": "{}/{}".format(THUMBNAIL_DIR.relative_to("."), img.name)}


assert IMAGE_DIR.exists()
assert THUMBNAIL_DIR.exists()
images = [get_image_info(i) for i in sorted(IMAGE_DIR.glob("**/*.jpg"))]

template = Template(TEMPLATE_PATH.read_text())
result = template.render(images=images)
RESULT_PATH.write_text(result)
