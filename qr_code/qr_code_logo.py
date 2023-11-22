import qrcode
from PIL import Image

def generate_qr_with_logo(url, logo_path, output_file):
    # Generate QR code
    qr = qrcode.QRCode(
        version=4,  # Version 4 gives a 33x33 grid
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=5,  # Size of each box in pixels
        border=4,  # Border thickness in boxes, a quiet zone of 1 is the minimum
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    
    # Load the logo image
    logo_image = Image.open(logo_path).convert('RGBA')
    
    # Calculate the maximum size of the logo
    logo_max_size = min(qr_image.size)
    logo_image.thumbnail((logo_max_size, logo_max_size), Image.LANCZOS)
    
    # Calculate the position to place the logo (centered)
    x = (qr_image.size[0] - logo_image.size[0]) // 2
    y = (qr_image.size[1] - logo_image.size[1]) // 2
    
    # Paste the logo image onto the QR code
    qr_image.paste(logo_image, (x, y), logo_image)
    
    # Save the final image
    qr_image.save(output_file)

# Example usage:
generate_qr_with_logo(
    url="https://flarnrules.github.io/thanksgiving-2023/",
    logo_path='/mnt/c/Users/Benjamin/Documents/flarnchain/holiday/forqrcode.png',
    output_file='qr_turkey_logo.png'
)
