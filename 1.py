import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class NoteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Note olish ilovasi')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.input_widget = QLineEdit()
        self.input_widget.setPlaceholderText("Note kiriting")

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Saqlangan eslatmalar bu yerda ko'rsatiladi")
        self.text_area.setReadOnly(True)

        self.save_button = QPushButton("Saqlash")
        self.save_button.clicked.connect(self.save_note)

        layout.addWidget(QLabel("Input widget-ga note kiriting:"))
        layout.addWidget(self.input_widget)
        layout.addWidget(self.save_button)
        layout.addWidget(QLabel("Saqlangan note'lar:"))
        layout.addWidget(self.text_area)

        self.setLayout(layout)

    def save_note(self):

        note = self.input_widget.text()

        if note:
            current_text = self.text_area.toPlainText()
            updated_text = current_text + note + "\n"
            self.text_area.setText(updated_text)

            self.input_widget.clear()

def main():
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
