import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        # Создание осей выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_therd = QHBoxLayout()
        self.hbox_four = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_therd)
        self.vbox.addLayout(self.hbox_four)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)
        # Создание кнопок и привязка к осям выравнивания
        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_0 = QPushButton("0", self)
        self.hbox_therd.addWidget(self.b_0)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_multi = QPushButton("*", self)
        self.hbox_second.addWidget(self.b_multi)

        self.b_divi = QPushButton("%", self)
        self.hbox_second.addWidget(self.b_divi)

        self.b_comm = QPushButton(".", self)
        self.hbox_therd.addWidget(self.b_comm)

        # Создаем события, которые будут отвечать за результат нажатия по кнопкам
        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multi.clicked.connect(lambda: self._operation("*"))
        self.b_divi.clicked.connect(lambda: self._operation("%"))
        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_comm.clicked.connect(lambda: self._button("."))

    # Создаем метод класса для обработки кнопок, отвечающих за ввод цифр в линию ввода текста
    def _button(self, param):
        line = self.input.text()

        self.input.setText(line + param)

    # Создаем метод класса для обработки нажатия на кнопку математической операции
    def _operation(self, op):
        self.num_1 = float(self.input.text())

        self.op = op
        self.input.setText("")

    # Создаем метод класса для обработки нажатия на кнопку результата
    def _result(self):
        self.num_2 = float(self.input.text())
        if self.op == "+":
            self.input.setText(str(self.num_1 + self.num_2))
        if self.op == "-":
            self.input.setText(str(self.num_1 - self.num_2))
        if self.op == "*":
            self.input.setText(str(self.num_1 * self.num_2))
        if self.op == "%" and self.num_2 != 0:
            self.input.setText(str(self.num_1 / self.num_2))
        if self.op == "%" and self.num_2 == 0:
            self.input.setText("На ноль делить нельзя")


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())
