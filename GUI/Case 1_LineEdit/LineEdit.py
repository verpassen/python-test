import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5 import uic
class MyForm(QDialog):
	def __init__(self):
		super().__init__()
		uic.loadUi('demoLineEdit.ui',self)
		self.initGUI()
		self.show()

	def initGUI(self):
		Name = self.lineEditName
		button = self.ButtonClickMe
		button.clicked.connect(lambda: self.dispmsg())

	def dispmsg(self):
		self.label_response.setText("Hello {} !".format(self.lineEditName.text()))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = MyForm()
	w.show()
	sys.exit(app.exec_())

#---
'''
- 練習用qt designer 畫出GUI layout 
- load the ui file 
- connect functino to the button widget 


'''