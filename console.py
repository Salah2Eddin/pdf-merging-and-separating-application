"""
    author: Mohamed Alaa Eddin
    date: 1st March 2022
    File with console application functions
"""

from pdf import merge_pdf, separate_pages, extract_page
import exc


def main_screen():
    """
    Shows the application's main menu
    :return:
    """
    print("Hello, Welcome to PDF Merging and Separating Application.\n"
          "You will find output under \"outputs\" folder.\n"
          "You can:\n\t1- Merge 2 PDF Files\n"
          "\t2- Extract a Page From PDF File\n"
          "\t3- Separate all Pages in a PDF File\n"
          "\t4- Exit")
    user_input = int(input("Operation no: "))
    if user_input == 1:
        merge_pdf_screen()
    if user_input == 2:
        extract_page_screen()
    if user_input == 3:
        separate_pages_screen()
    if user_input == 4:
        print("Thanks For Using Our Application.")
        return False
    return True


def merge_pdf_screen():
    """
    Shows the application's merge pdf screen
    :return:
    """
    pdf1_path = input("Enter 1st PDF Path: ")
    pdf2_path = input("Enter 2nd PDF Path: ")
    output_name = input("Enter Merged File Name: ")
    try:
        merge_pdf(pdf1_path, pdf2_path, output_name)
    except exc.NotPath:
        print("One of the two paths is invalid")
    except exc.NotPDF:
        print("One of the two paths doesn't lead to a PDF file!")


def extract_page_screen():
    """
    Shows the application's extract page screen
    :return:
    """
    pdf_file_path = input("Enter PDF File Path: ")
    page_number = int(input("Enter Page Number: "))
    try:
        extract_page(pdf_file_path, page_number)
    except exc.NotPath:
        print("This path is invalid")
    except exc.NotPDF:
        print("This path doesn't lead to a pdf file")


def separate_pages_screen():
    """
    Shows the application's separate pages screen
    :return:
    """
    pdf_file_path = input("Enter PDF File Path: ")
    try:
        separate_pages(pdf_file_path)
    except exc.NotPath:
        print("This path is invalid")
    except exc.NotPDF:
        print("This path doesn't lead to a pdf file")
