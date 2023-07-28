import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import*
import customtkinter
from reportlab.pdfgen import canvas
from fpdf import FPDF
customtkinter.set_appearance_mode("dark")
class PDFGenerator:
    def __init__(self, root):
        self.root = root
        root.title("PDF Generator")

        # Create the generate button
        generate_button = customtkinter.CTkButton(root, text="Download PDF", command=self.generate_pdf)
        generate_button.place(relx=0.5,rely=0.5,anchor="center")


    def generate_pdf(self):
        # Ask for the output file name
        file_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not file_name:
            return

        # Create the PDF object
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add some sample text to the PDF
        pdf.image("logo.png",12,15,35,15)
        pdf.cell(190, 30, txt="Hospital name", ln=1, align="C",border=True)
        pdf.cell(200, 20, ln=1, align="L")
        pdf.cell(200, 10, txt="Patient Name:", ln=1, align="L")
        pdf.cell(200, 10, txt="Age:", ln=1, align="L")
        pdf.cell(200, 10, txt="Sex:", ln=1, align="L")
        pdf.cell(200, 40, txt="Disease detected:", ln=1, align="L")
        pdf.cell(200, 30, txt="About Disease:", ln=1, align="L")
        
        # Save the PDF to the specified file
        pdf.output(file_name)

        # Show a success message
        messagebox.showinfo("PDF Generator", "PDF generated successfully!")

root=customtkinter.CTk()
root.geometry("700x500")
app = PDFGenerator(root)
root.mainloop()