# Generate PDF file of your 3rd Semester Mark-sheet

# ID : 20CE062
# NAME : Ranjit Odedra
# GitHub Repo Link : 


# import canvas
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("Result_Sem_3_20CE062.pdf")
canvas.drawString(50, 830, "Sem 3 Result of Ranjit Odedra")
canvas.drawString(50, 800, "CE244 SOFTWARE GROUP PROJECT-1   PRACTICAL : AA")
canvas.drawString(50, 780, "CE251 JAVA PROGRAMMING PRACTICAL :AA THEORY: AB")
canvas.drawString(50, 760, "CE252 DIGITAL ELECTRONICS PRACTICAL :AB THEORY: BC")
canvas.drawString(50, 740, "CE257 DATA COMMUNICATION & NETWORKING PRACTICAL :AA THEORY: BB")
canvas.drawString(50, 720, "EE284 PYTHON PROGRAMMING PRACTICAL :AA ")
canvas.drawString(50, 700, "HS123.02 A CREATIVITY, PROBLEM SOLVING AND INNOVATION PRACTICAL : AA")
canvas.drawString(50, 680, "MA253 DISTINCT MATHEMATICS AND ALGEBRA THEORY: BB")
canvas.drawString(50, 660, "CGPA : 8.54")
canvas.drawString(50, 640, "SGPA : 8.76")
canvas.save()

from reportlab.lib.units import inch, cm  # noqa

print(cm)
print(inch)

canvas = Canvas("Result_Sem_3_20CE062.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER  # noqa

canvas = Canvas("Result_Sem_3_20CE062.pdf", pagesize=LETTER)
print(LETTER)


canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

# The code below creates a PDF with blue text
from reportlab.lib.colors import blue  # noqa
from reportlab.lib.pagesizes import LETTER  # noqa
from reportlab.lib.units import inch  # noqa
from reportlab.pdfgen.canvas import Canvas  # noqa

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

# Saving PDF
canvas.save()