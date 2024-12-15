from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from calculator import *
from modewindow import *
import math

class Logic2(QMainWindow, Ui_ModeWindow):

    def __init__(self):
        """Function calls and instance variables"""
        super().__init__()
        self.area:int = 0
        self.base:int = 0
        self.height:int = 0
        self.setupUi(self)
        self.label_1.hide()
        self.text2.hide()
        self.circle_radio.toggled.connect(self.circle)
        self.square_radio.toggled.connect(self.square)
        self.rectange_radio.toggled.connect(self.rectangle)

        self.comput_button.clicked.connect(self.submit)


    def circle(self) -> None:
        """If circle button is checked then set up interface"""
        if self.circle_radio.isChecked():
            self.label_2.setVisible(False)
            self.label_1.setVisible(True)
            self.label_1.setText('Radius')
            self.text2.setVisible(False)


    def square(self) -> None:
        """If square button is checked then set up interface"""
        if self.square_radio.isChecked():
            self.label_2.setVisible(False)
            self.label_1.setText('Side')
            self.text2.setVisible(False)


    def rectangle(self) -> None:
        """If rectangle button is checked then set up interface"""
        if self.rectange_radio.isChecked():
            self.label_2.setVisible(True)
            self.label_1.setText('Base')
            self.label_2.setText('Height')
            self.text2.setVisible(True)

    def triangle(self) -> None:
        """If triangle button is checked then set up interface"""
        if self.triangle_radio.isChecked():
            self.label_2.setVisible(True)
            self.label_1.setText('Base')
            self.label_2.setText('Height')
            self.text2.setVisible(True)

    def submit(self) -> None:
        """If compute button is clicked then display area calculation, if an error occurs then display error"""
        if self.circle_radio.isChecked():
            try:
                self.area = self.text1.text()
                self.area = float(self.area)
                if self.area > 0:
                    self.area = self.area * math.pi
                    self.result_label.setText(f'Area = {self.area}')
                else:
                    raise TypeError
            except TypeError:
                self.result_label.setText('Values must be positive')
            except ValueError:
                self.result_label.setText('Enter numeric values')


        elif self.square_radio.isChecked():
            try:
                self.area = self.text1.text()
                self.area = float(self.area)
                if self.area > 0:
                    self.area = self.area ** 2
                    self.result_label.setText(f'Area = {self.area}')
                else:
                    raise TypeError
            except TypeError:
                self.result_label.setText('Values must be positive')
            except ValueError:
                self.result_label.setText('Enter numeric values')


        elif self.rectange_radio.isChecked():
            try:
                self.base = self.text1.text()
                self.height = self.text2.text()
                self.base = float(self.base)
                self.height = float(self.height)
                if self.base <= 0:
                    raise TypeError
                if self.height <= 0:
                    raise TypeError
                else:
                    self.area = self.base * self.height
                    self.result_label.setText(f'Area = {self.area}')
            except TypeError:
                self.result_label.setText('Values must be positive')
            except ValueError:
                self.result_label.setText('Enter numeric values')


        elif self.triangle_radio.isChecked():
            try:
                self.base = self.text1.text()
                self.height = self.text2.text()
                self.base = float(self.base)
                self.height = float(self.height)
                if self.base <= 0:
                    raise TypeError
                if self.height <= 0:
                    raise TypeError
                else:
                    self.area = 0.5 * self.base * self.height
                    self.result_label.setText(f'Area = {self.area}')
            except TypeError:
                self.result_label.setText('Values must be positive')
            except ValueError:
                self.result_label.setText('Enter numeric values')


