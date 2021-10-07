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
    "PiZero": "/piZero",
    "Back": "/pi4A",
    "Side B": "/pi4B",
}
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Push Buttons
        self.boxes = QPushButton('Boxes6')
        self.boxes.clicked.connect(lambda: self.on_button_clicked('boxes6'))

        self.minions4 = QPushButton('Minions4')
        self.minions4.clicked.connect(lambda: self.on_button_clicked('minions4'))
        self.minions6 = QPushButton('Minions6')
        self.minions6.clicked.connect(lambda: self.on_button_clicked('minions6'))
        self.dimo = QPushButton('3Dimo6')
        self.dimo.clicked.connect(lambda: self.on_button_clicked('3dimo6'))
        self.hya = QPushButton('Hya6')
        self.hya.clicked.connect(lambda: self.on_button_clicked('hya6'))
        self.parkway = QPushButton('Parkday4')
        self.parkway.clicked.connect(lambda: self.on_button_clicked('parkway4'))
        self.science = QPushButton('Science4')
        self.science.clicked.connect(lambda: self.on_button_clicked('science4'))
        self.ziscuit = QPushButton('Ziscuit4')
        self.ziscuit.clicked.connect(lambda: self.on_button_clicked('ziscuit4'))
        self.brett6 = QPushButton('Brett6')
        self.brett6.clicked.connect(lambda: self.on_button_clicked('brett6'))
        self.brett4 = QPushButton('Brett4')
        self.brett4.clicked.connect(lambda: self.on_button_clicked('brett4'))
        self.jess6 = QPushButton('Jess6')
        self.jess6.clicked.connect(lambda: self.on_button_clicked('jess6'))
        self.jess4 = QPushButton('Jess4')
        self.jess4.clicked.connect(lambda: self.on_button_clicked('jess4'))
        self.stephanie6 = QPushButton('Stephanie6')
        self.stephanie6.clicked.connect(lambda: self.on_button_clicked('stephanie6'))
        self.stephanie4 = QPushButton('Stephanie4')
        self.stephanie4.clicked.connect(lambda: self.on_button_clicked('stephanie4'))
        self.techstars = QPushButton('Techstars6')
        self.techstars.clicked.connect(lambda: self.on_button_clicked('techstars6'))


        self.richard = QPushButton('Richard')
        self.richard.clicked.connect(lambda: self.on_button_clicked('richard6'))
        self.cow = QPushButton('Cow')
        self.cow.clicked.connect(lambda: self.on_button_clicked('COW_4'))
        self.caribou = QPushButton('Caribou')
        self.caribou.clicked.connect(lambda: self.on_button_clicked('caribouSkippy2'))
        self.potBelly = QPushButton('Pot Belly')
        self.potBelly.clicked.connect(lambda: self.on_button_clicked('potbellySkippy'))
        self.ricos = QPushButton('Ricos')
        self.ricos.clicked.connect(lambda: self.on_button_clicked('ricos'))
        self.freshii = QPushButton('Freshii')     
        self.freshii.clicked.connect(lambda: self.on_button_clicked('freshie'))

        self.redBull0 = QPushButton('Red Bull 4-0')
        self.redBull0.clicked.connect(lambda: self.on_button_clicked('redbull0'))
        self.redBull1 = QPushButton('Red Bull 4-1')
        self.redBull1.clicked.connect(lambda: self.on_button_clicked('redbull4-4'))
        self.redBull5 = QPushButton('Red Bull 4-2')
        self.redBull5.clicked.connect(lambda: self.on_button_clicked('redbull4-2'))
        self.redBull2 = QPushButton('Red Bull 6-1')
        self.redBull2.clicked.connect(lambda: self.on_button_clicked('redbull6-1'))
        self.redBull3 = QPushButton('Red Bull 6-2')
        self.redBull3.clicked.connect(lambda: self.on_button_clicked('redbull6-2'))
        self.redBull = QPushButton('Red Bull 6-3')
        self.redBull.clicked.connect(lambda: self.on_button_clicked('redbull6-3'))
        self.redBull6 = QPushButton('Red Bull 6-4')
        self.redBull6.clicked.connect(lambda: self.on_button_clicked('redbull6-4'))
        self.redBull7 = QPushButton('Red Bull 6-5')
        self.redBull7.clicked.connect(lambda: self.on_button_clicked('redbull6-5'))
        self.chips4 = QPushButton('Chips 4-1')
        self.chips4.clicked.connect(lambda: self.on_button_clicked('chips4-1'))
        self.cookies6 = QPushButton('Cookies 6-1')
        self.cookies6.clicked.connect(lambda: self.on_button_clicked('cookies6-1'))
        self.techstars1 = QPushButton('Techstars 4-1')
        self.techstars1.clicked.connect(lambda: self.on_button_clicked('techstars4-1'))
        self.techstars2 = QPushButton('Techstars 4-2')
        self.techstars2.clicked.connect(lambda: self.on_button_clicked('techstars4-2'))
        self.brett1 = QPushButton('Brett 6-1')
        self.brett1.clicked.connect(lambda: self.on_button_clicked('brett6-1'))
        # Radio Button
        
        self.pi4A = QRadioButton("Back")
        self.piZero = QRadioButton("Side A")
        self.pi4B = QRadioButton("Side B")
        self.radioBtns = [self.piZero, self.pi4A, self.pi4B]

        #main_layout.addWidget(self.piZero)
        main_layout.addWidget(self.pi4A)
        main_layout.addWidget(self.pi4B) 

        main_layout.addWidget(self.boxes6)
        main_layout.addWidget(self.minions4)
        main_layout.addWidget(self.minions6)
        main_layout.addWidget(self.dimo)
        main_layout.addWidget(self.hya)
        main_layout.addWidget(self.parkway)
        main_layout.addWidget(self.science)
        main_layout.addWidget(self.ziscuit)
        main_layout.addWidget(self.brett6)
        main_layout.addWidget(self.brett4)
        main_layout.addWidget(self.jess6)
        main_layout.addWidget(self.jess4)
        main_layout.addWidget(self.stephanie6)
        main_layout.addWidget(self.stephanie4)
        main_layout.addWidget(self.techstars)

        main_layout.addWidget(self.richard)
        main_layout.addWidget(self.cow)
        main_layout.addWidget(self.caribou) 
        main_layout.addWidget(self.potBelly)
        main_layout.addWidget(self.ricos)
        main_layout.addWidget(self.freshii)
        main_layout.addWidget(self.redBull0)
        main_layout.addWidget(self.redBull1)
        main_layout.addWidget(self.redBull5)
        main_layout.addWidget(self.redBull2)
        main_layout.addWidget(self.redBull3)
        main_layout.addWidget(self.redBull)
        main_layout.addWidget(self.redBull6)
        main_layout.addWidget(self.redBull7)
        main_layout.addWidget(self.chips4)
        main_layout.addWidget(self.cookies6)
        main_layout.addWidget(self.techstars1)
        main_layout.addWidget(self.techstars2)
        main_layout.addWidget(self.brett1)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)  

    def on_button_clicked(self, adName):
        json_payload = json.dumps({'feed-id': 'none',
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