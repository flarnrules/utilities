from PIL import Image
import qrcode

def generate_qr_code_with_turkey(url, turkey_image_path, output_path):
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

    # Open the turkey image
    turkey_img = Image.open(turkey_image_path).convert('RGBA')

    # Resize turkey image to match QR code size
    turkey_img = turkey_img.resize(qr_img.size, Image.LANCZOS)


    # Blend the QR code with the turkey image
    blended_img = Image.blend(qr_img, turkey_img, alpha=0.5)

    # Save the blended image
    blended_img.save(output_path)

# Example usage
url = 'https://flarnrules.github.io/thanksgiving-2023/'  # Your URL here
turkey_image_path = '/mnt/c/users/Benjamin/Documents/flarnchain/holiday/turkey.png'  # Your turkey image path here
output_path = 'turkey_qr_code.png'  # Desired output file name
generate_qr_code_with_turkey(url, turkey_image_path, output_path)
