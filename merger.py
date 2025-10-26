import sys, os, tempfile
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QListWidget, QFileDialog, QLabel, QHBoxLayout, QListWidgetItem, QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyPDF2 import PdfMerger
from pdf2image import convert_from_path

class PDFMergerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.pdf_files = []
        self.setWindowTitle("Premium PDF Merger")
        self.setGeometry(200, 200, 600, 450)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("📚 Premium PDF Merger")
        title.setStyleSheet("font-size:20px;font-weight:bold;text-align:center;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.list_widget = QListWidget()
        self.list_widget.setIconSize(QSize(80, 100))
        layout.addWidget(self.list_widget)

        btn_row = QHBoxLayout()
        upload_btn = QPushButton("Add PDFs")
        upload_btn.clicked.connect(self.add_pdfs)
        btn_row.addWidget(upload_btn)

        remove_btn = QPushButton("Remove Selected")
        remove_btn.clicked.connect(self.remove_selected)
        btn_row.addWidget(remove_btn)

        layout.addLayout(btn_row)

        merge_btn = QPushButton("Merge PDFs")
        merge_btn.setStyleSheet("background-color:#0078ff;color:white;font-weight:bold;")
        merge_btn.clicked.connect(self.merge_pdfs)

        layout.addWidget(merge_btn)

        self.setLayout(layout)

    def add_pdfs(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select PDF Files", "", "PDF Files (*.pdf)")
        if files:
            for file in files:
                self.pdf_files.append(file)

                # Create thumbnail
                thumbnail = None
                try:
                    first_page = convert_from_path(file, 100, first_page=1, last_page=1)[0]
                    thumb = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
                    first_page.save(thumb.name, "PNG")
                    thumbnail = QIcon(thumb.name)
                except:
                    thumbnail = QIcon()

                item = QListWidgetItem(thumbnail, os.path.basename(file))
                self.list_widget.addItem(item)

    def remove_selected(self):
        row = self.list_widget.currentRow()
        if row >= 0:
            self.list_widget.takeItem(row)
            del self.pdf_files[row]

    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            QMessageBox.warning(self, "Error", "Add at least two PDF files.")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "merged.pdf", "PDF Files (*.pdf)")
        if not save_path:
            return

        merger = PdfMerger()
        try:
            for pdf in self.pdf_files:
                merger.append(pdf)
            merger.write(save_path)
            QMessageBox.information(self, "Success", "Merged successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            merger.close()


if __name__ == "__main__":
    from PyQt5.QtCore import Qt
    app = QApplication(sys.argv)
    window = PDFMergerUI()
    window.show()
    sys.exit(app.exec_())
