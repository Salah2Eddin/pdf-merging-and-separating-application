def main_screen():
    """
    Shows the application's main menu
    ::
    """
    print("Hello, Welcome to PDF Merging and Separating Application . ")
    print(
        "You can: \n 1- Merge 2 PDF Files \n 2- Extract a Page From PDF File \n 3- Separate all Pages in a PDF File ""\n 4- Exit")
    main_screen.user_input = int(input("Enter Number Of Operation You Need : "))


def merge_pdf_screen():
    """
    Shows the application's merge pdf screen
    ::
    """
    pdf1_path = input("Enter 1st PDF Path : ")
    pdf2_path = input("Enter 2nd PDF Path : ")
    output_name = input("Enter Merged File Name : ")


def extract_page_screen():
    """
    Shows the application's extract page screen
    ::
    """
    pdf_file_path = input("Enter PDF File Path : ")
    page_number = input("Enter Page Number : ")


def separate_pages_screen():
    """
    Shows the application's separate pages screen
    ::
    """
    pdf_file_path = input("Enter PDF File Path : ")


main_screen()
if main_screen.user_input == 1:
    merge_pdf_screen()
if main_screen.user_input == 2:
    extract_page_screen()
if main_screen.user_input == 3:
    separate_pages_screen()
if main_screen.user_input == 4:
    print("\nThanks For Using Our Application.")
