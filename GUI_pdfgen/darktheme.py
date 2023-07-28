import tkinter as tk
from tkinter import*
import customtkinter
from tkinter import filedialog
customtkinter.set_appearance_mode("dark")
def upload_audio():
    file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Audio files", "*.mp3;*.wav;*.m4a"), ("all files", "*.*")))
    print(file_path)
root=customtkinter.CTk()
# root = Tk()
root.title("Respiratory disease recognitionizer")
root.geometry("500x500")
upload_button = customtkinter.CTkButton(root, text = "Upload Audio",font=("Inter",14), command = upload_audio)
upload_button.place(relx=0.5,rely=0.5,anchor="center")

root.mainloop()