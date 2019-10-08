import tkinter
import numpy as np
import cv2

import PIL.Image, PIL.ImageTk

# Callback for the "Blur" button
# Callback for the "Blur" button
def blur_image():
      global photo
      global cv_img
  
      cv_img = cv2.blur(cv_img, (3, 3))
      photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
      canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# Create a window
window = tkinter.Tk()
# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("background.jpg"), cv2.COLOR_BGR2RGB)
# Get the image dimensions 
height, width, channels = cv_img.shape
# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width = width , height = height)
canvas.pack()
# Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
# Button that lets the user blur the image
btn_blur=tkinter.Button(window, text="Blur", width=50, command=blur_image)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)

window.mainloop()
