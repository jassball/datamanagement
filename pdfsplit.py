from PyPDF2 import PdfReader, PdfWriter

# Function to split a PDF
def split_pdf(input_pdf, start_page, end_page, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Select the pages you want to include in the new PDF
    for i in range(start_page - 1, end_page):  # Pages are 0-indexed in PyPDF2
        writer.add_page(reader.pages[i])

    # Write the selected pages to the output PDF
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

# Input PDF file
input_pdf = "pythonskip.pdf"

# Total number of pages in the PDF
total_pages = 1470

# Split ranges (each part will have around 245 pages)
split_pdf(input_pdf, 1, 245, "output_part1.pdf")     # Pages 1 to 245
split_pdf(input_pdf, 246, 490, "output_part2.pdf")   # Pages 246 to 490
split_pdf(input_pdf, 491, 735, "output_part3.pdf")   # Pages 491 to 735
split_pdf(input_pdf, 736, 980, "output_part4.pdf")   # Pages 736 to 980
split_pdf(input_pdf, 981, 1225, "output_part5.pdf")  # Pages 981 to 1225
split_pdf(input_pdf, 1226, total_pages, "output_part6.pdf")  # Pages 1226 to 1470
