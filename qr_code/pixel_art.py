import numpy as np
from PIL import Image

def create_pixel_art(image_path, pixel_art_size=(29, 29)):
    # Open the turkey image
    img = Image.open(image_path)
    
    # Resize the image to the size of the QR code grid
    small_img = img.resize(pixel_art_size, Image.NEAREST)
    
    # Convert to pixel art
    result = small_img.convert("RGB")
    
    # Save or return the pixel art image
    result.save('turkey_pixel_art.png')
    return result

# Call the function with the path to your turkey drawing
create_pixel_art('/mnt/c/users/Benjamin/Documents/flarnchain/holiday/turkey.png')
