import tkinter as tk
import re
from fpdf import FPDF
from tkinter import messagebox
import customtkinter
from reportlab.pdfgen import canvas
from tkinter import filedialog
customtkinter.set_appearance_mode("dark")
# Create the splash screen

splash = tk.Tk()
splash.title("Loading")
splash.geometry("700x500")

splash.overrideredirect(True)

# Create a canvas
canvas = tk.Canvas(splash, width=700, height=500, bg='#FFFFFF')
canvas.pack(fill="both", expand=True)

# Add an image to the canvas
splash_image = tk.PhotoImage(file='logos.png')
canvas.create_image(340,240, image=splash_image)

# Center the window on the screen
window_width = splash.winfo_width()
window_height = splash.winfo_height()
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = int((screen_width - window_width) / 5)
y = int((screen_height - window_height) / 5)
splash.geometry(f"+{x}+{y}")

"""
# Add a label to the canvas
label = tk.Label(splash, text='Loading...', font=('Arial', 20), foreground='#ffffff', background='#0077be')
canvas.create_window(250,200, window=label)

# Design the layout for the splash screen
label = tk.Label(splash, text="Loading...")
label.pack(pady=50)
loading = tk.Label(splash, text="Loading Animation Here")
loading.pack()
"""
customtkinter.set_appearance_mode("dark")
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)
def validate_contact(contact):
    pattern = r"^[0-9]{10}$"
    return re.match(pattern, contact)
def validate_sex(sex):
    return sex in ["male", "female","Male","Female","M","m","F","f"]
# Define a callback function for the splash screen
def show_main_window():
    # Hide the splash screen
    splash.withdraw()
    class PDF(FPDF):
        def print_info(self, name, age, sex, email, number):
            self.set_font('Arial', 'B', 16)
            self.image("logo.png",12,15,35,15)
            self.cell(190, 30, txt="Perinchery Memorial Hospital", ln=1, align="C",border=True)
            self.cell(0, 20, 'Patient Details', 0, 1)
            self.ln(2)
            self.set_font('Arial', '', 12)
            self.cell(0, 15, f'Name               : {name}', 0, 1)
            self.cell(0, 15, f'Age                  : {age}', 0, 1)
            self.cell(0, 15, f'Sex                  : {sex}', 0, 1)
            self.cell(0, 15, f'Email               : {email}', 0, 1)
            self.cell(0, 15, f'phone no         : {number}', 0, 1)
            self.cell(200, 40, txt="Disease detected:", ln=1, align="L")
            self.cell(200, 30, txt="About Disease   :", ln=1, align="L")
    def upload_audio():
        file_path = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("Audio files", "*.mp3;*.wav;*.m4a"), ("all files", "*.*")))
        print(file_path)
# Function to generate the PDF file
    def generate_pdf(name, age, sex, email,number):
        if name.isdigit()==True:
            messagebox.showerror("Error", "Invalid name")
            return    
        try:
            age = int(age)
            if age <= 0 or age>120:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid age. Please enter a valid age.")
            return
        if not validate_sex(sex):
            messagebox.showerror("Invalid Sex", "Please enter in valid format.")
            return
        if not validate_email(email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return
        if not validate_contact(number):
            messagebox.showerror("Invalid Contact", "Please enter a valid 10-digit phone number.")
            return
        
        file_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not file_name:
            return
        pdf = PDF()
        pdf.add_page()
        pdf.print_info(name, age, sex, email, number)
        pdf.output(file_name)
        messagebox.showinfo("PDF Generator", "PDF generated successfully!")
# Create the main window
    root=customtkinter.CTk()
    root.geometry("700x600")
    root.title("Main Window")

    # Add a label and entry field for name
    name_label = customtkinter.CTkLabel(root, text="Name:")
    name_label.pack(pady=10)
    name_entry = customtkinter.CTkEntry(root)
    name_entry.pack(pady=5)

    # Add a label and entry field for age
    age_label = customtkinter.CTkLabel(root, text="Age:")
    age_label.pack(pady=10)
    age_entry = customtkinter.CTkEntry(root)
    age_entry.pack(pady=5)

    # Add a label and entry field for sex
    sex_label = customtkinter.CTkLabel(root, text="Sex:")
    sex_label.pack(pady=10)
    sex_entry = customtkinter.CTkEntry(root)
    sex_entry.pack(pady=5)

    # Add a label and entry field for email
    email_label = customtkinter.CTkLabel(root, text="Email:")
    email_label.pack(pady=10)
    email_entry = customtkinter.CTkEntry(root)
    email_entry.pack(pady=5)

    number_label = customtkinter.CTkLabel(root, text="Phone no:")
    number_label.pack(pady=10)
    number_entry = customtkinter.CTkEntry(root)
    number_entry.pack(pady=5)

    # Add a button to upload an audio file
    audio_button = customtkinter.CTkButton(root, text="Upload Audio",font=("Inter",14), command = upload_audio)
    audio_button.pack(pady=10)

    # Add a button to generate a PDF file with the user's information
    pdf_button = customtkinter.CTkButton(root, text="Generate PDF", command=lambda: generate_pdf(name_entry.get(), age_entry.get(), sex_entry.get(), email_entry.get(),number_entry.get()))
    pdf_button.pack(pady=10)
    # Run the main event loop
    root.mainloop()

# Use the after() method to delay the display of the main window
splash.after(3000, show_main_window)

# Run the splash screen event loop
splash.mainloop()