import subprocess
from PyQt6.QtWidgets import QMessageBox
from src.isoChooser import file_path

def write(usbSelect, window):

    ask = QMessageBox.question(
            window,
            "WARNING",
            "WARNING! All data will be wiped on the selected device!\n Do you want to continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

    if ask == QMessageBox.StandardButton.Yes:
        print("BOOM!")
    else:
        print("good")
    