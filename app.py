import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from PolynomialDerivative import PolynomialDerivative

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polynomial Derivative Calculator")
        self.resize(500, 550)
        self.center()
        
        self.pal = QPalette()
        
        self.header = QLabel("Polynomial Derivative Calculator", self)
        
        self.item_box = QLabel("x²", self)
        
        self.initUI()

    def center(self):
        frame_size = self.frameGeometry()
        centre_point = QDesktopWidget().availableGeometry().center()
        frame_size.moveCenter(centre_point)
        self.move(frame_size.topLeft())
        
    def initUI(self):
        self.pal.setColor(QPalette.Window, QColor("black"))
        self.setPalette(self.pal)
        self.setAutoFillBackground(True)
        
        self.header.setGeometry(25, 10, 450, 50)
        self.header.setFont(QFont("Segoe UI", 20))
        self.header.setStyleSheet("color: white;"
                                  "font-weight: bold;"
                                  "background-color: #2a313d;"
                                  "border-radius: 20px")
        self.header.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        
        self.item_box.setGeometry(50, 90, 60, 50)
        self.item_box.setFont(QFont("Segoe UI", 20))
        self.item_box.setStyleSheet("background-color: white;"
                                    "border-radius: 20px;")
        self.item_box.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.item_box.setContentsMargins(0, 0, 0, 7)
            
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())   
        

if __name__ == "__main__":
    main()