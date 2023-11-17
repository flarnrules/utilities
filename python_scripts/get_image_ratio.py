from PIL import Image

image_name = ''
image_path = string('/mnt/c/Users/Benjamin/Pictures/Screenshots/{}', image_name)

def analyze_image(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    aspect_ratio = width/height
    return width, height, aspect_ratio


width, height, aspect_ratio = analyze_image(image_path)
print(f"Width: {width} pixels, Height: {height} pixels, Aspect Ratio: {aspect_ratio:.2f}")