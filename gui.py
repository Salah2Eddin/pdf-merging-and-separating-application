"""
    author: Salah Eddin Mohamed
    date: 2nd March 2022
    file with all classes for GUI application
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from pdf import merge_pdf, extract_page, separate_pages


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

        self.text = self.text_field.text


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

        self.text = self.text_field.text


class FieldsArea(QWidget):
    """
    Container for fields.
    """

    def __init__(self):
        super(QWidget, self).__init__()
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
        merge.clicked.connect(lambda: merge_pdf(pdf1_path.path,
                                                pdf2_path.path,
                                                output_name.text))
        self.v_layout.addWidget(merge)

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
        extract.clicked.connect(lambda: extract_page(pdf_path.path,
                                                     page_number.text))
        self.v_layout.addWidget(extract)

    def separate_fields(self):
        """
        shows fields needed for separating all pages in a pdf
        :return:
        """
        self.clear_layout()

        pdf_path = FileInputField("PDF path", self)
        self.v_layout.addWidget(pdf_path)

        separate = QPushButton("Separate")
        separate.clicked.connect(lambda: separate_pages(pdf_path.path))
        self.v_layout.addWidget(separate)


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
