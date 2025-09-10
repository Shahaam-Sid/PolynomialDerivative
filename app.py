import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import QFont, QPalette, QColor, QDoubleValidator
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
        
        self.collin_label = QLabel(":", self)
        
        self.equation_box = QLineEdit(self)
        
        self.btn1 = QPushButton("1", self)
        self.btn2 = QPushButton("2", self)
        self.btn3 = QPushButton("3", self)
        self.btn4 = QPushButton("4", self)
        self.btn5 = QPushButton("5", self)
        self.btn6 = QPushButton("6", self)
        self.btn7 = QPushButton("7", self)
        self.btn8 = QPushButton("8", self)
        self.btn9 = QPushButton("9", self)
        self.btndel = QPushButton("CE", self)
        self.btn0 = QPushButton("0", self)
        self.btneq = QPushButton("=", self)
        
        
        
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
        self.header.setContentsMargins(0, 0, 0, 5)
        
        self.item_box.setGeometry(50, 90, 60, 50)
        self.item_box.setFont(QFont("Segoe UI", 20))
        self.item_box.setStyleSheet("background-color: white;"
                                    "border-radius: 20px;")
        self.item_box.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.item_box.setContentsMargins(0, 0, 0, 7)
        
        self.collin_label.setGeometry(120, 85, 60, 50)
        self.collin_label.setFont(QFont("Segoe UI", 15))
        self.collin_label.setStyleSheet("color: #ffdf00;"
                                        "font-weight: bold")
        
        self.equation_box.setGeometry(140, 85, 315, 60)
        self.equation_box.setFont(QFont("Segoe UI", 15))
        self.equation_box.setStyleSheet("background-color: white;"
                                    "border-radius: 20px;"
                                    "selection-color: white;"
                                    "selection-background-color: #ffdf00;")
        self.equation_box.setTextMargins(10, 0, 0, 0)
        
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)
        validator.setBottom(-99999)
        validator.setTop(99999)
                    
        self.equation_box.setValidator(validator)
        
        self.btneq.setObjectName("equalButton")
        self.btndel.setObjectName("deleteButton")
        
        
        self.setStyleSheet("""
    QPushButton {
        background-color: #2a313d;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #3e4756;
    }
    QPushButton:pressed {
        background-color: #1c2027;
    }QPushButton#equalButton {
        background-color: #ffdf00;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }QPushButton:hover#equalButton {
        background-color: #c79500;
    }
    QPushButton:pressed#equalButton {
        background-color: #5c4500;
    }QPushButton#deleteButton {
        background-color: #d10404;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }QPushButton:hover#deleteButton {
        background-color: #960202;
    }
    QPushButton:pressed#deleteButton {
        background-color: #4a0101;
    }
""")
        
        grid = QGridLayout()
        grid.addWidget(self.btn1, 0, 0)
        grid.addWidget(self.btn2, 0, 1)
        grid.addWidget(self.btn3, 0, 2)
        grid.addWidget(self.btn4, 1, 0)
        grid.addWidget(self.btn5, 1, 1)
        grid.addWidget(self.btn6, 1, 2)
        grid.addWidget(self.btn7, 2, 0)
        grid.addWidget(self.btn8, 2, 1)
        grid.addWidget(self.btn9, 2, 2)       
        grid.addWidget(self.btndel, 3, 0)
        grid.addWidget(self.btn0, 3, 1)
        grid.addWidget(self.btneq, 3, 2)
        
        button_container = QWidget(self)
        button_container.setGeometry(50, 180, 400, 350)
        button_container.setLayout(grid)
        
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())   
        

if __name__ == "__main__":
    main()