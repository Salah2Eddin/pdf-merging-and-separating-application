"""
    author: Mohamed Alaa Eddin & Salah Eddin Mohamed
    date: 4th March 2022
"""
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import os


def read_pdf(pdf_path):
    """
    Reads PDF file from given path and returns PdfFileReader Object.
    :param pdf_path: The path of the file to be read.
    :return: PdfFileReader Object
    """
    if os.path.isfile(pdf_path) and pdf_path.endswith(".pdf"):
        return PdfFileReader(pdf_path)
    elif not os.path.isfile(pdf_path):
        print("Not Correct Path. if there is any \" remove them")
        return None
    else:
        print("Not PDF File")
        return None


def merge_pdf(first_pdf_path, second_pdf_path, output_name):
    """
    Merges 2 PDFs then saves the result as "output_name.pdf".
    :param first_pdf_path:The first PDF's Path.
    :param second_pdf_path: The second PDF's Path.
    :param output_name: The name of the output file.
    :return:
    """

    merger = PdfFileMerger()
    pdf1 = read_pdf(first_pdf_path)
    pdf2 = read_pdf(second_pdf_path)

    if not (pdf1 and pdf2):
        return

    merger.append(pdf1)
    merger.append(pdf2)

    merger_stream = open(os.path.join(os.getcwd(), "outputs",
                                      f"{output_name}.pdf"), 'wb')
    merger.write(merger_stream)


def extract_page(pdf_path, page_number):
    """
    Extracts the page with the given page number than saves it as
    "pdf_filename.pdf".
    :param pdf_path: The PDF file's path.
    :param page_number: The page number.
    :return:
    """
    pdf = read_pdf(pdf_path)

    if not pdf:
        return

    filename = os.path.split(pdf_path)[-1]
    output = PdfFileWriter()
    output.addPage(pdf.getPage(page_number - 1))
    output_stream = open(os.path.join(os.getcwd(), "outputs",
                                      f"{filename}"), 'wb')
    output.write(output_stream)


def separate_pages(pdf_path):
    """
    Extracts each page in the given pdf file and saves them individually.
    Output will be in a folder named after the pdf and each page will be
    named as "pdf_filename_pagenumber.pdf"
    :param pdf_path: The PDF file's path
    :return:
    """
    pdf = read_pdf(pdf_path)

    if not pdf:
        return

    filename = os.path.split(pdf_path)[-1]
    for i in range(pdf.getNumPages()):
        output = PdfFileWriter()
        output.addPage(pdf.getPage(i))
        output_stream = open(os.path.join(os.getcwd(), "outputs",
                                          filename + f"_{i + 1}.pdf"), 'wb')
        output.write(output_stream)
