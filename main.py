import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from insp import inspect
from generator import generate
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
        self.x0 = QLineEdit(self)
        layout.addWidget(self.x0)

        self.label2 = QLabel('Введіть a:', self)
        layout.addWidget(self.label2)
        self.a = QLineEdit(self)
        layout.addWidget(self.a)

        self.label3 = QLabel('Введіть c:', self)
        layout.addWidget(self.label3)
        self.c = QLineEdit(self)
        layout.addWidget(self.c)

        self.label4 = QLabel('Введіть m:', self)
        layout.addWidget(self.label4)
        self.m = QLineEdit(self)
        layout.addWidget(self.m)

        self.label5 = QLabel('Введіть назву файлу (без розширення):', self)
        layout.addWidget(self.label5)
        self.name_file = QLineEdit(self)
        layout.addWidget(self.name_file)

        self.addButton = QPushButton('Згенерувати', self)
        self.addButton.clicked.connect(self.generate_user)
        layout.addWidget(self.addButton)

        self.addButton = QPushButton('Згенерувати послідовності з мого варіанту', self)
        self.addButton.clicked.connect(self.calculate_from_lab)
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

    def generate_user(self):
        """Провидить генерацію для чисел користувача"""
        try:
            a = int(self.a.text())
            c = int(self.c.text())
            m = int(self.m.text())
            x0 = int(self.x0.text())
            file_name = self.name_file.text()

            if file_name == '':
                QMessageBox.critical(self, 'Помилка', 'Будь ласка, введіть ім`я файлу')
            self.messageArea.append(f'Початкові параметри a, c, m {a, c, m}')
            acm = inspect(a, c, m)
            self.messageArea.append(f'Так виглядають а, с, m після перевірки {acm}')
            generate(x0, acm, file_name)
        except ValueError:
            QMessageBox.critical(self, 'Помилка', 'Будь ласка, введіть коректні числа.')
            self.messageArea.append('Помилка: Некоректні вхідні дані.')


    def calculate_from_lab(self):
        """Проводить генерацію для чисел з лабораторної"""
        x0 = 0
        a, c, m = [289, 169], [1079, 857], [131072, 1048576]
        file_name = ["GPCH1", "GPCH2"]
        for i in range(2):
            self.messageArea.append(f'ПОЧИНАЮ ГЕНЕРАЦІЮ ДЛЯ ПОСЛІДОВНОСТІ {file_name[i]}')
            self.messageArea.append(f'Початкові параметри a, c, m {a[i], c[i], m[i]}')
            acm = inspect(a[i], c[i], m[i])
            self.messageArea.append(f'Так виглядають а, с, m після перевірки {acm}')
            generate(x0, acm, file_name[i])
        self.messageArea.append(f"Генерацію завершено, в папці з програмою з`явилися текстові файли з послідовностями")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdderApp()
    ex.show()
    sys.exit(app.exec_())