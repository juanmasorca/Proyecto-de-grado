import tkinter as tk
from tkinter import ttk
import pydicom
import os
from PIL import Image, ImageTk

# Crear la ventana principal y el slider
root = tk.Tk()
root.title("Visor de imágenes DICOM")

# Crear el slider
slider = ttk.Scale(root, from_=0, to=60, orient="horizontal")
slider.pack()

# Leer las imágenes DICOM de la carpeta
dcm_images = []

folder_path = "./Prueba2/"
for filename in os.listdir(folder_path):
    if filename.endswith(".dcm"):
        dcm_image = pydicom.dcmread(os.path.join(folder_path, filename))
        dcm_images.append(dcm_image)

def update_image(val):
    # Obtener la imagen correspondiente al valor del slider
    index = int(float(val))
    dcm_image = dcm_images[index]

    # Convertir la imagen DICOM a una imagen PIL
    image_array = dcm_image.pixel_array
    image = Image.fromarray(image_array)

    # Mostrar el tamaño de la imagen en la consola
    print(f"Tamaño de la imagen: {image.size} píxeles")

    # Mostrar la imagen en la pantalla
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

# Crear un widget para mostrar la imagen
label = tk.Label(root)
label.pack()

slider.config(command=update_image)

root.mainloop()
