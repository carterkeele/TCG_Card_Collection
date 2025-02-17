import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import card_scan

class TCG_Card_Collection(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TCG Card Collection')

        self.image_label = QLabel('No image selected', self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.upload_button = QPushButton('Upload Image', self)
        self.upload_button.clicked.connect(self.upload_image)

        self.search_button = QPushButton('Search Card', self)
        self.search_button.clicked.connect(self.search_card)
        self.search_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.upload_button)
        layout.addWidget(self.search_button)
        self.setLayout(layout)

    def upload_image(self):
        # Open a file dialog to select an image
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.xpm *.jpg)', options=options)
        if file_name:
        # Display the selected image
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))
            self.search_button.setEnabled(True)

    def search_card(self):
        # Placeholder function to perform the card search
        # You can integrate your existing card search logic here
        print('Searching for the card...')
        card_scan.main()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TCG_Card_Collection()
    ex.show()
    sys.exit(app.exec_())

