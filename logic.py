from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from calculator import *
import math
from logic2 import *

class Logic(QMainWindow, Ui_Calculator):

    def __init__(self) -> None:
        """Function calls"""
        super().__init__()
        self.setupUi(self)
        self.result:int = 0
        self.list1:list = []
        self.screen.setText('0')
        self.button_0.clicked.connect(lambda: self.button())
        self.button_1.clicked.connect(lambda: self.button())
        self.button_2.clicked.connect(lambda: self.button())
        self.button_3.clicked.connect(lambda: self.button())
        self.button_4.clicked.connect(lambda: self.button())
        self.button_5.clicked.connect(lambda: self.button())
        self.button_6.clicked.connect(lambda: self.button())
        self.button_7.clicked.connect(lambda: self.button())
        self.button_8.clicked.connect(lambda: self.button())
        self.button_9.clicked.connect(lambda: self.button())
        self.sign_button.clicked.connect(lambda: self.button())
        self.clear_button.clicked.connect(lambda: self.button())
        self.button_decimal.clicked.connect(lambda: self.button())
        self.delete_button.clicked.connect(lambda: self.button())

        self.multiply_button.clicked.connect(lambda: self.operator())
        self.subtract_button.clicked.connect(lambda: self.operator())
        self.add_button.clicked.connect(lambda: self.operator())
        self.divide_button.clicked.connect(lambda: self.operator())

        self.equal_button.clicked.connect(lambda: self.equal())

        self.mode_button.clicked.connect(lambda: self.second_window())

    def operator(self) -> None:
        """If multiply, divide, add, or subtract button is clicked append to list"""
        operator = self.sender()
        if operator == self.multiply_button:
            self.list1.append('*')
        if operator == self.divide_button:
            self.list1.append('/')
        if operator == self.add_button:
            self.list1.append('+')
        if operator == self.subtract_button:
            self.list1.append('-')
        self.result = ''.join(self.list1)
        self.screen.setText(self.result)

    def equal(self) -> None:
        """If equal button is pressed display calculation result, if an error occurs then display error in the screen"""
        equal = self.sender()
        if equal == self.equal_button:
            try:
                self.result = str(self.result)
                answer = eval(self.result)
                if answer == math.floor(answer):
                    answer = int(answer)
                print(answer)
                self.screen.setText(str(answer))
                self.list1.clear()
                self.list1.append(str(answer))
            except SyntaxError:
                self.screen.setText('Syntax Error')
            except ZeroDivisionError:
                self.screen.setText('Undefined')


    def button(self) -> None:
        """If a number button is pressed then append to list.
        If the clear button is pressed then clear the screen.
        If the delete button is pressed then delete last item from the list.
        Convert the list into a string"""
        button = self.sender()
        if button == self.button_0:
            self.list1.append('0')
        if button == self.button_1:
            self.list1.append('1')
        if button == self.button_2:
            self.list1.append('2')
        if button == self.button_3:
            self.list1.append('3')
        if button == self.button_4:
            self.list1.append('4')
        if button == self.button_5:
            self.list1.append('5')
        if button == self.button_6:
            self.list1.append('6')
        if button == self.button_7:
            self.list1.append('7')
        if button == self.button_8:
            self.list1.append('8')
        if button == self.button_9:
            self.list1.append('9')
        if button == self.button_decimal:
            self.list1.append('.')
        if button == self.sign_button:
            if self.list1[0] != '-':
                self.list1.insert(0, '-')
            elif self.list1[0] == '-':
                self.list1.pop(0)
        if button == self.clear_button:
            self.list1.clear()
        if button == self.delete_button:
            if len(self.list1) == 0:
                self.screen.setText('0')
                self.list1.append('0')
            else:
                self.list1.pop()
                if len(self.list1) == 0:
                    self.screen.setText('0')

        self.result = ''.join(self.list1)
        if len(self.list1) == 0:
            self.screen.setText('0')
        else:
            self.screen.setText(self.result)

    def second_window(self) -> None:
        """Open up mode window when mode button is clicked"""
        self.secondwindow = Logic2()
        self.secondwindow.setGeometry(100, 200, 451, 401)
        self.secondwindow.show()


















