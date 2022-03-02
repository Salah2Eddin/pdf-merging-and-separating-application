"""
    author: Mohamed Alaa Eddin
    date: 1st March 2022
    File with console application functions
"""


def main_screen():
    """
    Shows the application's main menu
    :return:
    """
    print("""
    Hello, Welcome to PDF Merging and Separating Application .
    You can:
        1- Merge 2 PDF Files
        2- Extract a Page From PDF File
        3- Separate all Pages in a PDF File
        4- Exit
    """)
    user_input = int(input("Operation no: "))
    if user_input == 1:
        merge_pdf_screen()
    if user_input == 2:
        extract_page_screen()
    if user_input == 3:
        separate_pages_screen()
    if user_input == 4:
        print("\nThanks For Using Our Application.")
    print("You will find output under \"outputs\" folder.")


def merge_pdf_screen():
    """
    Shows the application's merge pdf screen
    :return:
    """
    pdf1_path = input("Enter 1st PDF Path: ")
    pdf2_path = input("Enter 2nd PDF Path: ")
    output_name = input("Enter Merged File Name: ")


def extract_page_screen():
    """
    Shows the application's extract page screen
    :return:
    """
    pdf_file_path = input("Enter PDF File Path: ")
    page_number = input("Enter Page Number: ")



def separate_pages_screen():
    """
    Shows the application's separate pages screen
    :return:
    """
    pdf_file_path = input("Enter PDF File Path: ")
