from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QMainWindow, QVBoxLayout, QWidget, QFileDialog, QMessageBox
from GUI.support import SupportWindow
from GUI.style import CONST_MAIN_WINDOW

def pop_window(title : str, text : str):
    window = QMessageBox()
    window.setWindowTitle(title)
    window.setText(text)
    window.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Перевод аудио в текст")
        self.setFixedSize(300, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.start = None
        
        central_widget = QWidget()
        control_UI = QVBoxLayout()
        
        greet = QLabel(text="Укажите путь к файлу пожалуйста")
        run = QPushButton(text="Выбрать путь")
        run.clicked.connect(self.audio_selection)
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(run)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def audio_selection(self):
        try:
            file_filter = "Audio Files (*.mp3 *.wav *.m4a)"
            path = QFileDialog.getOpenFileName(self, "Выберите аудио","", file_filter)
        except:
            pop_window("Ошибка", "Ошибка открытия окна")
            
        print(path)
        
        #конвертация в нужный формат
        #сохранение в перменную
        self.start = SupportWindow()
        