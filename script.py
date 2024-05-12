from rembg import remove
import os
from PIL import Image

def process_image(file_path):
    with open(file_path, 'rb') as img_file:
        img = img_file.read()
    output = remove(img)

    base_name = os.path.basename(file_path)
    name, _ = os.path.splitext(base_name)
    result_name = f"{name}_output_bg_remover_trpsky.png"  # Always use .png extension

    result_path = os.path.join(os.path.dirname(file_path), result_name)
    with open(result_path, 'wb') as f:
        f.write(output)

    return output, result_path