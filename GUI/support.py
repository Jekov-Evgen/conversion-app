from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from GUI.style import CONST_MAIN_WINDOW

def pop_window_support(title : str, text : str):
    window = QMessageBox()
    window.setWindowTitle(title)
    window.setText(text)
    window.exec()

class SupportWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перевод аудио в текст")
        self.setFixedSize(500, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        central_widget = QWidget()
        control_UI = QVBoxLayout()
        
        greet = QLabel(text="Укажите путь куда сохранить пожалуйста")
        save = QPushButton(text="Выбрать путь")
        save.clicked.connect(self.audio_selection)
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(save)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def audio_selection(self):
        try:
            path = QFileDialog.getExistingDirectory(self)
        except:
            pop_window_support("Ошибка", "Ошибка открытия окна")