from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtGui import QFont
from src.isoChooser import isoBtn_clicked
from src.searchDrives import searchDrives
from src.writeIso import write

font = QFont("DejaVu Sans", 30)

def createUI(window, APP_WIDTH, APP_HEIGHT):
    
    title = QLabel("WriteDD", window)
    title.setFont(font)
    title.move((APP_WIDTH - title.height()) // 2 - 65, 0)

    usbSelect = QComboBox(window)
    usbSelect.move(title.x() - 60 , 100)
    usbSelect.resize(370, usbSelect.height())

    pathBox = QLineEdit(window)
    pathBox.move(title.x()- 60, usbSelect.y() + 50)
    pathBox.resize(370, pathBox.height())

    selectBtn = QPushButton("Select ISO", window)
    selectBtn.move(10, pathBox.y())
    selectBtn.clicked.connect(lambda : isoBtn_clicked(pathBox))


    writeBtn = QPushButton("Write", window)
    writeBtn.move(10, pathBox.y() + 30)
    writeBtn.clicked.connect(lambda : write(usbSelect, window))

    def printOption():
        print(usbSelect.currentText())

    usbSelect.currentIndexChanged.connect(printOption)
    searchDrives(usbSelect)