from PyQt6.QtWidgets import QFileDialog, QFileIconProvider
from PyQt6.QtCore import QFileInfo
from pathlib import Path

def isoBtn_clicked(pathBox):
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select ISO file",
        "",
        "Images (*.iso *.img)"
    )

    ext = Path(file_path).suffix.lower()
    if ext == ".iso" or ext == ".img":
        pathBox.setText(file_path)
        print("[WRITEDD] Image detected")
    else:
        pathBox.setText('')
        pathBox.setPlaceholderText("Not an ISO file")
        print("[WRITEDD] Not an ISO file")