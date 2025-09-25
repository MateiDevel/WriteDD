from PyQt6.QtWidgets import QWidget, QApplication
from src.ui import createUI
import sys

app = QApplication(sys.argv)

APP_WIDTH, APP_HEIGHT = 500, 600

window = QWidget()
window.setWindowTitle("WriteDD")
window.setFixedSize(APP_WIDTH, APP_HEIGHT)

createUI(window, APP_WIDTH, APP_HEIGHT)
window.show()

sys.exit(app.exec())