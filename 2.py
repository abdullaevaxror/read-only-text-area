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

        self.input_ism = QLineEdit()
        self.input_ism.setPlaceholderText("Ismingizni kiriting: ")
        
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Elektron pochtangizni kiriting: ")

        self.input_trjhol = QLineEdit()
        self.input_trjhol.setPlaceholderText("Tarjimai holingizni kiriting: ")

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Saqlangan eslatmalar bu yerda ko'rsatiladi")
        self.text_area.setReadOnly(True)

        self.save_button = QPushButton("Saqlash")
        self.save_button.clicked.connect(self.save_note)

        layout.addWidget(QLabel("Ism:"))
        layout.addWidget(self.input_ism)
        layout.addWidget(QLabel("Elektron pochta:"))
        layout.addWidget(self.input_email)
        layout.addWidget(QLabel("Tarjimai hol:"))
        layout.addWidget(self.input_trjhol)
        layout.addWidget(self.save_button)
        layout.addWidget(QLabel("Saqlangan note'lar:"))
        layout.addWidget(self.text_area)

        self.setLayout(layout)

    def save_note(self):
        ism = self.input_ism.text()
        email = self.input_email.text()
        tarjimai_hol = self.input_trjhol.text()
        if ism and email and tarjimai_hol:

            new_note = f"Ism: {ism}\nEmail: {email}\ntarjimai hol: {tarjimai_hol}\n"

            current_text = self.text_area.toPlainText()
            updated_text = current_text + new_note + "\n"
            self.text_area.setText(updated_text)

            self.input_ism.clear()
            self.input_email.clear()
            self.input_trjhol.clear()

def main():
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
