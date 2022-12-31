from PyQt5 import QtWidgets
import Window
import sys

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Window.Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
