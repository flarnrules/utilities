from tkinter import Tk, Label, Button, filedialog, Frame
from PIL import Image
import os

def open_file(start_directory=None):
    file_path = filedialog.askopenfilename(initialdir=start_directory)
    if not file_path:
        return
    img = Image.open(file_path)
    
    # Normalize the image to 512x512 without distortion
    base_width, base_height = img.size
    aspect_ratio = base_width / base_height
    new_width = 512
    new_height = int(new_width / aspect_ratio)

    if new_height > 512:
        new_height = 512
        new_width = int(new_height * aspect_ratio)
    
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Centering the image on a 512x512 canvas
    new_img = Image.new("RGB", (512, 512))
    offset = ((512 - new_width) // 2, (512 - new_height) // 2)
    new_img.paste(img, offset)
    
    # Get old file name and append _512 for the new file
    old_file_name = os.path.basename(file_path)
    name, ext = os.path.splitext(old_file_name)
    new_file_name = f"{name}_512{ext}"
    
    # Save the normalized image
    new_img.save(new_file_name)

def create_quick_access_button(frame, directory):
    button = Button(frame, text=f"Quick Access: {os.path.basename(directory)}")
    button.config(command=lambda dir=directory: open_file(dir))
    button.pack(side="left")

# Initialize tkinter
root = Tk()
root.title("Image Normalizer")

# Add components
label = Label(root, text="Click 'Open' to select an image.")
label.pack()

frame = Frame(root)
frame.pack()

button_open = Button(frame, text="Open", command=open_file)
button_open.pack(side="left")

# Quick Access Buttons
quick_access_dirs = ["/mnt/c/users/Benjamin/Pictures"]
for directory in quick_access_dirs:
    create_quick_access_button(frame, directory)

# Run the app
root.mainloop()
