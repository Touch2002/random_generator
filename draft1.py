import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "C:/Users/userr/AppData/Local/Programs/Python/Python312/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

class AdderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Налаштування головного вікна
        self.setWindowTitle('Генерування чисел')
        self.setGeometry(100, 100, 400, 300)

        # Створення макету
        layout = QVBoxLayout()

        # Створення та налаштування віджетів
        self.label1 = QLabel('Введіть x0:', self)
        layout.addWidget(self.label1)
        self.entry1 = QLineEdit(self)
        layout.addWidget(self.entry1)

        self.label2 = QLabel('Введіть a:', self)
        layout.addWidget(self.label2)
        self.entry2 = QLineEdit(self)
        layout.addWidget(self.entry2)

        self.label3 = QLabel('Введіть c:', self)
        layout.addWidget(self.label3)
        self.entry3 = QLineEdit(self)
        layout.addWidget(self.entry3)

        self.label4 = QLabel('Введіть m:', self)
        layout.addWidget(self.label4)
        self.entry4 = QLineEdit(self)
        layout.addWidget(self.entry4)

        self.label5 = QLabel('Введіть назву файлу (без розширення):', self)
        layout.addWidget(self.label5)
        self.entry5 = QLineEdit(self)
        layout.addWidget(self.entry5)

        self.addButton = QPushButton('Згенерувати', self)
        self.addButton.clicked.connect(self.add_numbers)
        layout.addWidget(self.addButton)

        self.resultLabel = QLabel('Термінал на мінімалках:', self)
        layout.addWidget(self.resultLabel)

        # Додавання текстової області для повідомлень
        self.messageArea = QTextEdit(self)
        self.messageArea.setReadOnly(True)  # Робимо текстову область тільки для читання
        layout.addWidget(self.messageArea)

        self.messageArea.append(f'Привіт я програма')

        # Встановлення макету
        self.setLayout(layout)

    def add_numbers(self):
        try:
            num1 = float(self.entry1.text())
            num2 = float(self.entry2.text())
            result = num1 + num2
            self.resultLabel.setText(f'Результат: {result}')
            self.messageArea.append(f'Додано числа {num1} і {num2}. Результат: {result}')
        except ValueError:
            QMessageBox.critical(self, 'Помилка', 'Будь ласка, введіть коректні числа.')
            self.messageArea.append('Помилка: Некоректні вхідні дані.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdderApp()
    ex.show()
    sys.exit(app.exec_())
