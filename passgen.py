import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtCore

class DialogMain(QDialog):
    def __init__(self):
        super().__init__()

        # Main Window

        self.setWindowTitle("Password Generator")
        self.setFixedHeight(300)
        self.setFixedWidth(760)
        self.setStyleSheet("background-color: '#fcfcfc';")
        self.AllComponents()

    def AllComponents(self):

        # Frames

        self.FirstFrame = QFrame(self)
        self.FirstFrame.setGeometry(20, 20, 720, 90)
        self.FirstFrame.setFrameShape(QFrame.StyledPanel)
        self.FirstFrame.setFrameShadow(QFrame.Raised)
        self.FirstFrame.setObjectName("FirstFrame")
        self.FirstFrame.setStyleSheet("background-color: '#eadef7';" +
                                      "border: none;")

        self.SecondFrame = QFrame(self)
        self.SecondFrame.setGeometry(20, 130, 720, 150)
        self.SecondFrame.setFrameShape(QFrame.StyledPanel)
        self.SecondFrame.setFrameShadow(QFrame.Raised)
        self.SecondFrame.setObjectName("SecondFrame")
        self.SecondFrame.setStyleSheet("background-color: '#eadef7';" +
                                       "border: none;")

        self.GreenLine = QFrame(self)
        self.GreenLine.setGeometry(20, 101, 720, 10)
        self.GreenLine.setFrameShape(QFrame.StyledPanel)
        self.GreenLine.setFrameShadow(QFrame.Raised)
        self.GreenLine.setObjectName("GreenLine")
        self.GreenLine.setStyleSheet("QFrame {"
            "background-color: green;" +
            "border: none;"
            "}")

        # LineEdit

        self.LineEditPasswd = QLineEdit("Password", self)
        self.LineEditPasswd.setGeometry(50, 40, 520, 40)
        self.LineEditPasswd.setReadOnly(True)
        self.LineEditPasswd.setCursor(QtCore.Qt.IBeamCursor)
        self.LineEditPasswd.setObjectName("LineEditPasswd")
        self.LineEditPasswd.setStyleSheet(" QLineEdit {"
            "background: '#eadef7';" +
            "color: black;" +
            "border: none;" +
            "font-size: 30px;" +
            "font-family: monospace;" +
            "}")

        # Labels

        self.LabelPasswdLen = QLabel("Password Lenght", self)
        self.LabelPasswdLen.setGeometry(40, 180, 130, 20)
        self.LabelPasswdLen.setObjectName("LabelPasswdLen")
        self.LabelPasswdLen.setStyleSheet("QLabel {"
            "color: rgb(0, 0, 0);" +
            "background-color: transparent;" +
            "font-size: 15px;" +
            "}")

        self.LabelCustomize = QLabel("Customize your password", self)
        self.LabelCustomize.setGeometry(40, 130, 350, 40)
        self.LabelCustomize.setObjectName("LabelCustomize")
        self.LabelCustomize.setStyleSheet("QLabel {"
            "color: black;" +
            "background-color: transparent;" +
            "font-size: 20px;" +
            "}")

        # Buttons

        self.btnGenerate = QPushButton(self)
        self.btnGenerate.setGeometry(660, 30, 64, 64)
        self.btnGenerate.setObjectName("btnGenerate")
        self.btnGenerate.setToolTip('<p style="color:black;">Refresh</p>')
        self.btnGenerate.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnGenerate.clicked.connect(self.main_check)
        self.btnGenerate.setStyleSheet("QPushButton {"
            "background-image: url(refresh.png);" +
            "border-radius: 30px;" +
            "background-color: none;" +
            "border: none;"
            "}"

            "QPushButton:hover {"
            "background-color: '#b7b7b7';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#a4a4a4';"
            "}")

        self.btnCopy = QPushButton(self)
        self.btnCopy.setGeometry(590, 30, 64, 64)
        self.btnCopy.setObjectName("btnCopy")
        self.btnCopy.setToolTip('<p style="color: black;">Copy</p>')
        self.btnCopy.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnCopy.clicked.connect(self.button_copy)
        self.btnCopy.setStyleSheet("QPushButton {"
            "background-image: url(copy.png);" +
            "border-radius: 5px;" +
            "background-color: none;" +
            "border: none;" +
            "}"

            "QPushButton:hover {"
            "background-color: '#b7b7b7';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#a4a4a4';" +
            "}")

        # RadioButtons

        self.RadioBtnEasySay = QRadioButton("Easy to say", self)
        self.RadioBtnEasySay.setGeometry(350, 180, 110, 22)
        self.RadioBtnEasySay.setObjectName("RadioBtnEasySay")
        self.RadioBtnEasySay.toggled.connect(self.radio_buttons_check)
        self.RadioBtnEasySay.setStyleSheet("color: black;" +
                                           "background-color: transparent;")

        self.RadioBtnEasyRead = QRadioButton("Easy to read", self)
        self.RadioBtnEasyRead.setGeometry(350, 210, 110, 22)
        self.RadioBtnEasyRead.setObjectName("RadioBtnEasyRead")
        self.RadioBtnEasyRead.toggled.connect(self.radio_buttons_check)
        self.RadioBtnEasyRead.setStyleSheet("color: black;" +
                                            "background-color: transparent;")

        self.RadioBtnAllChar = QRadioButton("All Characters", self)
        self.RadioBtnAllChar.setGeometry(350, 240, 110, 22)
        self.RadioBtnAllChar.setObjectName("RadioBtnAllChar")
        self.RadioBtnAllChar.setChecked(True)
        self.RadioBtnAllChar.toggled.connect(self.radio_buttons_check)
        self.RadioBtnAllChar.setStyleSheet("color: black;" +
                                           "background-color: transparent;")

        # CheckBoxes

        self.checkBoxUppercase = QCheckBox("Uppercase", self)
        self.checkBoxUppercase.setGeometry(550, 180, 88, 22)
        self.checkBoxUppercase.setObjectName("checkBoxUppercase")
        self.checkBoxUppercase.setChecked(True)
        self.checkBoxUppercase.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxLowcase = QCheckBox("Lowercase", self)
        self.checkBoxLowcase.setGeometry(550, 200, 88, 22)
        self.checkBoxLowcase.setObjectName("checkBoxLowcase")
        self.checkBoxLowcase.setChecked(True)
        self.checkBoxLowcase.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxNum = QCheckBox("Numbers", self)
        self.checkBoxNum.setGeometry(550, 220, 88, 22)
        self.checkBoxNum.setObjectName("checkBoxNum")
        self.checkBoxNum.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxSym = QCheckBox("Symbols", self)
        self.checkBoxSym.setGeometry(550, 240, 88, 22)
        self.checkBoxSym.setObjectName("checkBoxSym")
        self.checkBoxSym.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        # Slider

        self.SliderValue = QSlider(self,
                              value=10,
                              maximum=50,
                              minimum=1)
        self.SliderValue.setGeometry(100, 225, 160, 20)
        self.SliderValue.setOrientation(QtCore.Qt.Horizontal)
        self.SliderValue.setToolTip(str(self.SliderValue.value()))
        self.SliderValue.setObjectName("SliderValue")
        self.SliderValue.valueChanged.connect(self.slider_value_act)
        self.SliderValue.setStyleSheet("color: black;" +
                                       "background-color: '#eadef7';")

        # Spinbox

        self.spinBoxValue = QSpinBox(self,
                                value=10,
                                maximum=50,
                                minimum=1,
                                singleStep=1)
        self.spinBoxValue.setGeometry(40, 220, 52, 32)
        self.spinBoxValue.setObjectName("spinBoxValue")
        self.spinBoxValue.valueChanged.connect(self.spinbox_value_act)
        self.spinBoxValue.setStyleSheet("QSpinBox {"
            "color: black;" +
            "font-family: Arial Black;" +
            "font-size: 15px;" +
            "background-color: transparent;"
            "}")

        # Line

        self.DecorLine = QFrame(self)
        self.DecorLine.setGeometry(40, 170, 681, 1)
        self.DecorLine.setFrameShape(QFrame.HLine)
        self.DecorLine.setFrameShadow(QFrame.Sunken)
        self.DecorLine.setObjectName("DecorLine")
        self.DecorLine.setStyleSheet("background-color: grey;")

        #Functions

    def slider_value_act(self):
        current = self.SliderValue.value()
        self.spinBoxValue.setValue(current)
        self.main_check()
        ####### By Sur3n0s #######
        # https://github.com/Sur3n0s/PasswordGenerator

    def spinbox_value_act(self):
        current = self.spinBoxValue.value()
        self.SliderValue.setValue(current)
        self.main_check()

    def main_check(self):

        # Lists

        list_uppcase = ('QWERTYUIOPASDFGHJKLZXCVBNM')
        list_lowcase = ('qwertyuiopasdfghjklzxcvbnm')
        list_numbers = ('1234567890')
        list_symbols = ('!@#$%^&*()_=+-<>?/\|~')
        list_main = ''

        # Operations

        if self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True:
            for x in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase)
                self.LineEditPasswd.setText(list_main)

        else:
            self.LineEditPasswd.setText('Please, choose valid option')

    def radio_buttons_check(self):
        if self.RadioBtnEasyRead.isChecked():
            self.checkBoxSym.setEnabled(False)
            self.checkBoxNum.setEnabled(False)
            self.checkBoxSym.setChecked(False)
            self.checkBoxNum.setChecked(False)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

        elif self.RadioBtnEasySay.isChecked():
            self.checkBoxSym.setEnabled(False)
            self.checkBoxNum.setEnabled(False)
            self.checkBoxSym.setChecked(False)
            self.checkBoxNum.setChecked(False)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

        else:
            self.checkBoxSym.setEnabled(True)
            self.checkBoxNum.setEnabled(True)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: black;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: black;" +
                "background-color: transparent;"
                "}")

    def button_copy(self):
        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.LineEditPasswd.text(), mode=copy.Clipboard)

######## aliens ########
# https://github.com/Sur3n0s/PasswordGenerator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogMain = DialogMain()
    dialogMain.show()
    sys.exit(app.exec_())

