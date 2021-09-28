from PyQt5.QtWidgets import *

app = QApplication([])
caribou = QPushButton('Caribou')
redBull = QPushButton('Red Bull')
ricos = QPushButton('Ricos')
freshii = QPushButton('Freshii')

ads = [caribou, redBull, ricos, freshii]

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

def on_clicked_ad(ad):
    pass

# button.clicked.connect(on_button_clicked)
# button.show()
for ad in ads:
    ad.clicked.connect(lambda: on_clicked_ad('caribou'))
    ad.show()

# caribou_ad.clicked.connect(lambda: on_clicked_ad('caribou'))
app.exec_()