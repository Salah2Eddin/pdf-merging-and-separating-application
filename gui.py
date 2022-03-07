"""
    author: Salah Eddin Mohamed
    date: 2nd March 2022
    file with all classes for GUI application
"""
import sys

import exc
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from pdf import merge_pdf, extract_page, separate_pages


def show_error_message(parent, title, message):
    bx = QMessageBox.critical(parent, title, message)


def show_message(parent, title, message):
    bx = QMessageBox.information(parent, title, message)


class FileInputField(QWidget):
    """
    Class that represents A File Input Field.
    It consists of a label, a text field and a browse button.
    """

    def __init__(self, header, parent=None):
        super(QWidget, self).__init__(parent)
        self.setFixedSize(500, 30)

        self.label = QLabel(header, self)
        self.label.setFixedHeight(25)

        self.text_field = QLineEdit(self)
        self.text_field.setFixedSize(
            self.width() - self.label.width() - 25, 25)
        self.text_field.move(self.label.width(), 0)
        self.text_field.textChanged.connect(lambda x: self.text_area_edited(x))

        self.browse = QPushButton("...", self)
        self.browse.setFixedSize(25, 25)
        self.browse.clicked.connect(self.browse_clicked)
        self.browse.move(self.label.width() + self.text_field.width(), 0)

        self.path = ""

    def browse_clicked(self):
        """
        Action function
        :return:
        """
        self.path = self.show_file_dialog()
        self.text_field.setText(self.path)

    def show_file_dialog(self):
        """
        Shows a file dialog
        :return: selected file's path
        """
        d = QFileDialog
        files, _ = d.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                     "", "PDF (*.pdf)")
        if files:
            return files

    def text_area_edited(self, x):
        self.path = x


class TextInput(QWidget):
    """
    Class that represents A Text Input Field.
    It consists of a label and a text field.
    """

    def __init__(self, header, parent=None):
        super(QWidget, self).__init__(parent)
        self.setFixedSize(500, 30)

        self.label = QLabel(header, self)
        self.label.setFixedHeight(25)

        self.text_field = QLineEdit(self)
        self.text_field.setFixedSize(
            self.width() - self.label.width(), 25)
        self.text_field.move(self.label.width(), 0)

    def get_text(self):
        return self.text_field.text()


class IntegerInput(QWidget):
    """
    Class that represents a Numbers Input Field.
    It consists of a label and a text field that accepts numbers only.
    """

    def __init__(self, header, parent=None):
        super(QWidget, self).__init__(parent)
        self.setFixedSize(500, 30)

        self.label = QLabel(header, self)
        self.label.setFixedHeight(25)

        self.text_field = QLineEdit(self)
        self.text_field.setValidator(QtGui.QIntValidator())
        self.text_field.setFixedSize(
            self.width() - self.label.width(), 25)
        self.text_field.move(self.label.width(), 0)

    def get_number(self):
        return int(self.text_field.text())


class FieldsArea(QWidget):
    """
    Container for fields.
    """

    def __init__(self):
        super(QWidget, self).__init__()
        sys.excepthook = self.exception_raised
        self.setFixedWidth(550)

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

    def clear_layout(self):
        """
        Removes all widgets in layout.
        :return:
        """
        for i in reversed(range(self.v_layout.count())):
            self.v_layout.itemAt(i).widget().setParent(None)

    def merge_fields(self):
        """
        shows fields for merging pdfs
        :return:
        """
        self.clear_layout()

        pdf1_path = FileInputField("PDF 1's path", self)
        self.v_layout.addWidget(pdf1_path)

        pdf2_path = FileInputField("PDF 2's path", self)
        self.v_layout.addWidget(pdf2_path)

        output_name = TextInput("Output Name")
        self.v_layout.addWidget(output_name)

        merge = QPushButton("Merge")
        merge.clicked.connect(
            lambda: self.merge_clicked(pdf1_path.path, pdf2_path.path,
                                       output_name.get_text()))
        self.v_layout.addWidget(merge)

    def merge_clicked(self, p1, p2, name):
        merge_pdf(p1,
                  p2,
                  name)
        show_message(self, "Complete", "Merging is complete.\nYou can find "
                                       "the output under \"outputs\" folder.")
        self.clear_layout()

    def extract_fields(self):
        """
        shows fields needed for extracting a page from pdf
        :return:
        """
        self.clear_layout()

        pdf_path = FileInputField("PDF path", self)
        self.v_layout.addWidget(pdf_path)

        page_number = IntegerInput("Page Number")
        self.v_layout.addWidget(page_number)

        extract = QPushButton("Extract")
        extract.clicked.connect(lambda:
                                self.extract_clicked(pdf_path.path,
                                                     page_number.get_number()))
        self.v_layout.addWidget(extract)

    def extract_clicked(self, p1, num):
        extract_page(p1, num)
        show_message(self, "Complete", "Extracting is complete.\nYou can find "
                                       "the output under \"outputs\" folder.")
        self.clear_layout()

    def separate_fields(self):
        """
        shows fields needed for separating all pages in a pdf
        :return:
        """
        self.clear_layout()

        pdf_path = FileInputField("PDF path", self)
        self.v_layout.addWidget(pdf_path)

        separate = QPushButton("Separate")
        separate.clicked.connect(lambda: self.separate_clicked(pdf_path.path))
        self.v_layout.addWidget(separate)

    def separate_clicked(self, p):
        separate_pages(p)
        show_message(self, "Complete", "Separating is complete.\nYou can find "
                                       "the output under \"outputs\" folder.")
        self.clear_layout()

    def exception_raised(self, exc_type, exc_val, exc_tb):
        if exc_type == exc.NotPath:
            show_error_message(self, "Critical Error",
                               "There is an invalid path")
        elif exc_type == exc.NotPDF:
            show_error_message(self, "Critical Error",
                               "A path doesn't lead to a PDF File")
        elif exc_type == ValueError:
            show_error_message(self, "Critical Error",
                               "Please enter a number")
        elif exc_type == IndexError:
            show_error_message(self, "Critical Error", "This page doesn't "
                                                       "exist.")
        else:
            show_error_message(self, "Critical Error",
                               exc_type)


class ButtonsBox(QWidget):
    """
    Container for buttons
    """

    def __init__(self):
        super(QWidget, self).__init__()

        self.v_layout = QVBoxLayout()
        self.setLayout(self.v_layout)

        self.merge = QPushButton("Merge 2 PDF files")
        self.merge.setFixedHeight(50)

        self.extract = QPushButton("Extract a page")
        self.extract.setFixedHeight(50)

        self.separate = QPushButton("Separate all pages")
        self.separate.setFixedHeight(50)

        self.exit = QPushButton("Exit")
        self.exit.clicked.connect(exit)
        self.exit.setFixedHeight(50)

        self.v_layout.addWidget(self.merge)
        self.v_layout.addWidget(self.extract)
        self.v_layout.addWidget(self.separate)
        self.v_layout.addWidget(self.exit)


class App(QWidget):
    """
    Main App Widget
    """

    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowTitle("PDF Merging and Separating Application")
        self.setWindowFlags(
            QtCore.Qt.WindowType.WindowCloseButtonHint |
            QtCore.Qt.WindowType.WindowMinimizeButtonHint |
            QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)

        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(10, 10, 5, 5)
        self.setLayout(self.h_layout)

        self.buttons = ButtonsBox()
        self.h_layout.addWidget(self.buttons)

        self.fields = FieldsArea()
        self.h_layout.addWidget(self.fields)

        self.buttons.merge.clicked.connect(self.fields.merge_fields)
        self.buttons.extract.clicked.connect(self.fields.extract_fields)
        self.buttons.separate.clicked.connect(self.fields.separate_fields)


# to run gui application
if __name__ == "__main__":
    root = QApplication([])
    app = App()
    app.show()

    exit(root.exec_())
