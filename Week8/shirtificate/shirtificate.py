from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "", 50)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("./shirtificate.png", "C", 60, 190)
pdf.set_font_size(25)
pdf.set_text_color(255, 255, 255)
pdf.text(x=60, y=130, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")
