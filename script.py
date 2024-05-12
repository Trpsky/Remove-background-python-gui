import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import io

def open_image():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'rb') as img_file:
        img = img_file.read()
    output = remove(img)
    result = Image.open(io.BytesIO(output))
    result.show()

root = tk.Tk()
button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

root.mainloop()