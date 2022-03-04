from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


def main_screen():
    """
    Shows the application's main menu
    ::
    """
    print("Hello, Welcome to PDF Merging and Separating Application . ")
    print(
        "You can: \n 1- Merge 2 PDF Files \n 2- Extract a Page From PDF File \n 3- Separate all Pages in a PDF File ""\n 4- Exit")
    user_input = int(input("Enter Number Of Operation You Need : "))
    if user_input == 1:
        merge_pdf_screen()
    if user_input == 2:
        extract_page_screen()
    if user_input == 3:
        separate_pages_screen()
    if user_input == 4:
        print("\nThanks For Using Our Application.")


def merge_pdf_screen():
    """
    Shows the application's merge pdf screen
    ::
    """
    merger = PdfFileMerger()
    pdf1_path = open(input("Enter 1st PDF Path : "), 'rb')
    pdf2_path = open(input("Enter 2nd PDF Path : "), 'rb')
    output_name = input("Enter Merged File Name : ")
    pdf1 = PdfFileReader(pdf1_path)
    pdf2 = PdfFileReader(pdf2_path)
    merger.append(pdf1)
    merger.append(pdf2)
    merger_stream = open(output_name + ".pdf", 'wb')
    merger.write(merger_stream)
    print("\nDone! , Thanks For Using Our Application")


def extract_page_screen():
    """
    Shows the application's extract page screen
    ::
    """
    output = PdfFileWriter()
    pdf_file_path = input("Enter PDF File Path : ")
    page_number = int(input("Enter Page Number : "))
    with open(pdf_file_path, 'rb') as pdf_path:
        pdf = PdfFileReader(pdf_path)
        output.addPage(pdf.getPage(page_number - 1))
        output_stream = open("Extracted_Page.pdf", 'wb')
        output.write(output_stream)
    print("\nDone! , Thanks For Using Our Application")


def separate_pages_screen():
    """
    Shows the application's separate pages screen
    ::
    """

    pdf_file_path = input("Enter PDF File Path : ")
    pdf_path = open(pdf_file_path, 'rb')
    pdf = PdfFileReader(pdf_path)
    for page in range(pdf.getNumPages()):
        output = PdfFileWriter()
        output.addPage(pdf.getPage(page))
        output_stream = open("Page_" + str(page + 1) + ".pdf", 'wb')
        output.write(output_stream)
    print("\nDone! , Thanks For Using Our Application")


main_screen()
