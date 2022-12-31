from PyQt5 import QtCore, QtWidgets
import traceback
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 505)
        self.Metric = QtWidgets.QRadioButton(Dialog)
        self.Metric.setGeometry(QtCore.QRect(200, 40, 95, 31))
        self.Metric.setObjectName("Metric")
        self.SelectGroup = QtWidgets.QButtonGroup(Dialog)
        self.SelectGroup.setObjectName("SelectGroup")
        self.SelectGroup.addButton(self.Metric, 1)
        self.Imperial = QtWidgets.QRadioButton(Dialog)
        self.Imperial.setGeometry(QtCore.QRect(340, 40, 95, 31))
        self.Imperial.setObjectName("Imperial")
        self.SelectGroup.addButton(self.Imperial, 2)
        self.SelectLabel = QtWidgets.QLabel(Dialog)
        self.SelectLabel.setEnabled(True)
        self.SelectLabel.setGeometry(QtCore.QRect(0, 40, 161, 31))
        self.SelectLabel.setTextFormat(QtCore.Qt.AutoText)
        self.SelectLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SelectLabel.setObjectName("SelectLabel")
        self.WeightLabel = QtWidgets.QLabel(Dialog)
        self.WeightLabel.setEnabled(True)
        self.WeightLabel.setGeometry(QtCore.QRect(0, 110, 161, 31))
        self.WeightLabel.setTextFormat(QtCore.Qt.AutoText)
        self.WeightLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.WeightLabel.setObjectName("WeightLabel")
        self.WeightInput = QtWidgets.QTextEdit(Dialog)
        self.WeightInput.setGeometry(QtCore.QRect(223, 110, 191, 31))
        self.WeightInput.setObjectName("WeightInput")
        self.HeightInput = QtWidgets.QTextEdit(Dialog)
        self.HeightInput.setGeometry(QtCore.QRect(223, 190, 191, 31))
        self.HeightInput.setObjectName("HeightInput")
        self.HeightLabel = QtWidgets.QLabel(Dialog)
        self.HeightLabel.setEnabled(True)
        self.HeightLabel.setGeometry(QtCore.QRect(0, 190, 161, 31))
        self.HeightLabel.setTextFormat(QtCore.Qt.AutoText)
        self.HeightLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.HeightLabel.setObjectName("HeightLabel")
        self.CalcButton = QtWidgets.QPushButton(Dialog)
        self.CalcButton.setGeometry(QtCore.QRect(160, 420, 151, 51))
        self.CalcButton.setObjectName("CalcButton")
        self.CalcButton.clicked.connect(self.check)
        self.HeightLabel_2 = QtWidgets.QLabel(Dialog)
        self.HeightLabel_2.setEnabled(True)
        self.HeightLabel_2.setGeometry(QtCore.QRect(0, 290, 161, 31))
        self.HeightLabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.HeightLabel_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.HeightLabel_2.setObjectName("HeightLabel_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(200, 290, 256, 41))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BMI CALCULATOR"))
        self.Metric.setText(_translate("Dialog", "Metric"))
        self.Imperial.setText(_translate("Dialog", "Imperial"))
        self.SelectLabel.setText(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Select mode:</span></p></body></html>"))
        self.WeightLabel.setText(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Weight:</span></p></body></html>"))
        self.HeightLabel.setText(_translate("Dialog",
                                            "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Height</span></p></body></html>"))
        self.CalcButton.setText(_translate("Dialog", "Calculate"))
        self.HeightLabel_2.setText(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">BMI:</span></p></body></html>"))

    def check(self):
        weight = self.WeightInput.toPlainText()
        height = self.HeightInput.toPlainText()
        try:
            if weight == "" or height == "": raise Exception
            weight = float(weight)
            height = float(height)
            if weight < 0 or height < 0: raise Exception
            return self.calc(weight, height)
        except Exception:
            self.errorText()

    def calc(self, weight, height):
        BMI = 0
        if self.SelectGroup.checkedId() == 1:
            BMI = weight / ((height / 100) ** 2)
        elif self.SelectGroup.checkedId() == 2:
            BMI = (weight / 2.2046) / (((height * 30.48) / 100) ** 2)
        else:
            self.errorText()
        str = "{}: ".format(BMI)

        if BMI < 18.5:
            str = str + "Underweight"
        elif BMI <= 24.9:
            str = str + "Healthy Weight"
        elif BMI <= 29.9:
            str = str + "Overweight"
        else:
            str = str + "Obese"

        self.textBrowser.setText(str)

    def errorText(self):
        self.textBrowser.setText("Incorrect Inputs. Please Try again")


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
