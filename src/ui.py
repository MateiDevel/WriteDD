from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

font = QFont("DejaVu Sans", 30)

def createUI(window, APP_WIDTH, APP_HEIGHT):
    title = QLabel("WriteDD", window)
    title.setFont(font)
    title.move((APP_WIDTH - title.height()) // 2 - 65, 0)
    
    title.show