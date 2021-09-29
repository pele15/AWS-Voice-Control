import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout, QRadioButton)
import mqttPublish
import json
from awscrt import io, mqtt, auth, http
import configparser

topics = configparser.ConfigParser()
topics.read('topics.ini')

io.init_logging(getattr(io.LogLevel, io.LogLevel.NoLogs.name), 'stderr')

DEVICE_TO_LOCATION_DICT = {
    "Back": "/piZero",
    "Side A": "/pi4A",
    "Side B": "/pi4B",
}
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Push Buttons
        self.caribou = QPushButton('Caribou')
        self.caribou.clicked.connect(lambda: self.on_button_clicked('caribouSkippy2'))
        self.redBull = QPushButton('Pot Belly')
        self.redBull.clicked.connect(lambda: self.on_button_clicked('potbellySkippy'))
        self.ricos = QPushButton('Ricos')
        self.ricos.clicked.connect(lambda: self.on_button_clicked('ricos'))
        self.freshii = QPushButton('Freshii')     
        self.freshii.clicked.connect(lambda: self.on_button_clicked('freshie'))

        # Radio Button
        
        self.piZero = QRadioButton("Back")
        self.pi4A = QRadioButton("Side A")
        self.pi4B = QRadioButton("Side B")
        self.radioBtns = [self.piZero, self.pi4A, self.pi4B]

        main_layout.addWidget(self.piZero)
        main_layout.addWidget(self.pi4A)
        main_layout.addWidget(self.pi4B) 


        main_layout.addWidget(self.caribou) 
        main_layout.addWidget(self.redBull)
        main_layout.addWidget(self.ricos)
        main_layout.addWidget(self.freshii)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)  

    def on_button_clicked(self, adName):
        json_payload = json.dumps({'feed-id': 'coffee',
                                    'display': True,
                                    'display-ad': adName,
                                    'ad-img': adName + ".jpg"
                                    })
        location = self.getToggleState()
        topic = DEVICE_TO_LOCATION_DICT[location.text()]
        print(adName)
        mqtt_client = mqttPublish.connect_client()
        connection = mqtt_client.connect()
        connection.result() # waits until connection is established
        print("connection established!")
        publish = mqttPublish.publish_msg(mqtt_client, json_payload, topic)
        print(publish)
        mqttPublish.disconnect(mqtt_client)
        
        
    
    def getToggleState(self):
        for widget in self.radioBtns:
            if (widget.isChecked()):
                return widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow() 
    w.show()
    sys.exit(app.exec_())    