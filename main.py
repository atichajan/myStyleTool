try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool'

class myStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('My Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5f2c82, stop:1 #49a09d);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/smile.png")
		scale_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(128,128),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scale_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.imageLabel.setPixmap(self.imagePixmap)
		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('create')
		self.cancelButton = QtWidgets.QPushButton('cancel')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #D95138;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family: Papyrus;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 red, stop:1 blue);;
				}
				QPushButton:pressed {
					background-color: navy;
				}
			'''
		)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = myStyleToolDialog(parent=ptr)
	ui.show()