import sys 
import requests 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                            QVBoxLayout, QDesktopWidget)
from PyQt5.QtCore import Qt 

class WeatherApp(QWidget): 
    def __init__(self): 
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70°F", self)
        self.emoji_label = QLabel("")

        self.initUI()

    def initUI(self): 
        pass

    def center_window(self): 
        qr = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp) 
        self.move(qr.topLeft())

    def showEvent(self, event): 
        self.center_window()
        super().showEvent(event)

def main(): 
    app = QApplication(sys.argv)
    weather_app = WeatherApp() 
    weather_app.show() 
    sys.exit(app.exec_())

if __name__ == "__main__": 
    main()