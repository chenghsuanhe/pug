from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import serial
import sys
import ui


class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for n in range(10):
            getattr(self, f'pushButton_{n}').clicked.connect(
                lambda checked, x=n: self.onNumberClick(x))

        for c in ["exit", "clear", "back"]:
            getattr(self, f'pushButton_{c}').clicked.connect(
                lambda checked, x=c: self.onButtonClick(x))

    def onNumberClick(self, num: int):
        print(f"Clicked {num}")

    def onButtonClick(self, cmd: str):
        print(f"Clicked {cmd}")


app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()

try:
    fpga = serial.Serial("/dev/ttyUSB0", timeout=1)
except serial.serialutil.SerialException as error:
    print("連接至 FPGA 時發生錯誤:", error)
    sys.exit(1)

sys.exit(app.exec())
