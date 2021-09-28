import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QLineEdit, QPushButton, QVBoxLayout)
import mqttPublish
import json
from awscrt import io, mqtt, auth, http
import configparser

topics = configparser.ConfigParser()
topics.read('topics.ini')

io.init_logging(getattr(io.LogLevel, io.LogLevel.NoLogs.name), 'stderr')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        self.caribou = QPushButton('Caribou')
        self.caribou.clicked.connect(lambda: self.on_button_clicked('caribou'))
        self.redBull = QPushButton('Red Bull')
        self.redBull.clicked.connect(lambda: self.on_button_clicked('red bull'))
        self.ricos = QPushButton('Ricos')
        self.ricos.clicked.connect(lambda: self.on_button_clicked('ricos'))
        self.freshii = QPushButton('Freshii')     
        self.freshii.clicked.connect(lambda: self.on_button_clicked('freshie'))

        main_layout.addWidget(self.caribou) 
        main_layout.addWidget(self.redBull)
        main_layout.addWidget(self.ricos)
        main_layout.addWidget(self.freshii)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)  

    def on_button_clicked(self, adName):
        json_payload = json.dumps({'feed-id': adName,
                                    'display': True,
                                    'display-ad': adName,
                                    'ad-img': adName + ".jpg"
                                    })
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
        mqtt_client = mqttPublish.connect_client(client_bootstrap)
        mqttPublish.publish_msg(mqtt_client, json_payload)
        mqttPublish.disconnect(mqtt_client)
        print(adName)    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow() 
    w.show()
    sys.exit(app.exec_())    