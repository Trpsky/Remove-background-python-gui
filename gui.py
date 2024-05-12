import tkinter as tk
from tkinter import filedialog
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import os
import script

def open_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    output, result_path = script.process_image(file_path)
    # picture original
    original = Image.open(file_path)
    original = original.resize((250, 250))
    original_photo = ImageTk.PhotoImage(original)
    original_label.config(image=original_photo)
    original_label.image = original_photo

    # picture result
    result = Image.open(result_path)
    result = result.resize((250, 250))
    result_photo = ImageTk.PhotoImage(result)
    result_label.config(image=result_photo)
    result_label.image = result_photo

    result_label.bind("<Button-1>", lambda e: os.system(f'start {result_path}'))

root = ThemedTk(theme="arc")
root.geometry('600x300')
root.resizable(False, False)
root.title("Background Remover - Made by Trpsky")

button = tk.Button(root, text="Open Image", command=open_image)
button.pack()

original_label = tk.Label(root)
original_label.pack(side="left", padx=10, pady=10)

result_label = tk.Label(root)
result_label.pack(side="right", padx=10, pady=10)

root.mainloop()