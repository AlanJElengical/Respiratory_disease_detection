import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.geometry('600x600')
root.overrideredirect(True)

# Create a canvas
canvas = tk.Canvas(root, width=600, height=600, bg='#0077be')
canvas.pack()

# Add an image to the canvas
splash_image = tk.PhotoImage(file='logo.png')
canvas.create_image(300,250, image=splash_image)

# Add a label to the canvas
label = ttk.Label(root, text='Loading...', font=('Arial', 20), foreground='#ffffff', background='#0077be')
canvas.create_window(300, 480, window=label)

# Set a timer to close the splash screen after 3 seconds
root.after(3000, root.destroy)

root.mainloop()
