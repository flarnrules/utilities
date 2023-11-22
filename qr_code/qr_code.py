import qrcode

def generate_qr_code(url, file_name="qr_code.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    return file_name

# Example usage
url = "https://flarnrules.github.io/thanksgiving-2023/"  # Replace with your GitHub Pages URL
generate_qr_code(url)
