"""
    author:
    date:
"""
def read_pdf(pdf_path):
    """
    Reads PDF file from given path and returns PdfFileReader Object.
    :param pdf_path: The path of the file to be read.
    :return: PdfFileReader Object
    """
    pass


def merge_pdf(first_pdf_path, second_pdf_path, output_name):
    """
    Merges 2 PDFs then saves the result as "output_name.pdf".
    :param first_pdf_path:The first PDF's Path.
    :param second_pdf_path: The second PDF's Path.
    :param output_name: The name of the output file.
    :return:
    """
    pass


def extract_page(pdf_path, page_number):
    """
    Extracts the page with the given page number than saves it as
    "pdf_filename.pdf".
    :param pdf_path: The PDF file's path.
    :param page_number: The page number.
    :return:
    """
    pass


def separate_pages(pdf_path):
    """
    Extracts each page in the given pdf file and saves them individually.
    Output will be in a folder named after the pdf and each page will be
    named as "pdf_filename_pagenumber.pdf"
    :param pdf_path: The PDF file's path
    :return:
    """
    pass
