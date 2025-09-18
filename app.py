import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QLabel, QLineEdit, QPushButton, QWidget, QGridLayout, QShortcut
from PyQt5.QtGui import QFont, QPalette, QColor, QDoubleValidator, QKeySequence, QIcon
from PyQt5.QtCore import Qt, QTimer
from PolynomialDerivative import PolynomialDerivative

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polynomial Derivative Calculator")
        self.resize(500, 550)
        self.center()
        self.setWindowIcon(QIcon('logo.jpg'))
        
        self.pal = QPalette()
        
        self.header = QLabel("Polynomial Derivative Calculator", self)
        
        self.item_box = QLabel("d", self)
        
        self.collin_label = QLabel(":", self)
        
        self.equation_box = QLineEdit(self)
        
        self.sentence_box = QLabel("Enter Degree of Equation", self)
        
        self.btn1 = QPushButton("1", self)
        self.btn2 = QPushButton("2", self)
        self.btn3 = QPushButton("3", self)
        self.btn4 = QPushButton("4", self)
        self.btn5 = QPushButton("5", self)
        self.btn6 = QPushButton("6", self)
        self.btn7 = QPushButton("7", self)
        self.btn8 = QPushButton("8", self)
        self.btn9 = QPushButton("9", self)
        self.btndel = QPushButton("AC", self)
        self.btn0 = QPushButton("0", self)
        self.btnminus = QPushButton("-", self)
        self.btneq = QPushButton("=", self)
        
        self._equation = []
        self._current_index_flag = None
        
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
        
        self.sentence_box.setGeometry(125, 170, 250, 30)
        self.sentence_box.setFont(QFont("Segoe UI", 10))
        self.sentence_box.setStyleSheet("border: 2px inset #555;"
                "border-radius: 6px;"
                "padding: 4px;"
                "background: #1c1c1c;"
                "color: #dcd3c9;")
        self.sentence_box.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)


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
        grid.addWidget(self.btnminus, 3, 0)
        grid.addWidget(self.btn0, 3, 1)
        grid.addWidget(self.btneq, 3, 2)
        grid.addWidget(self.btndel, 4, 1)
        
        button_container = QWidget(self)
        button_container.setGeometry(50, 200, 400, 350)
        button_container.setLayout(grid)
        
        self.btn0.clicked.connect(self.write_0)
        self.btn1.clicked.connect(self.write_1)
        self.btn2.clicked.connect(self.write_2)
        self.btn3.clicked.connect(self.write_3)
        self.btn4.clicked.connect(self.write_4)
        self.btn5.clicked.connect(self.write_5)
        self.btn6.clicked.connect(self.write_6)
        self.btn7.clicked.connect(self.write_7)
        self.btn8.clicked.connect(self.write_8)
        self.btn9.clicked.connect(self.write_9)
        self.btnminus.clicked.connect(self.write_minus)
        self.btndel.clicked.connect(self.clear_text)
        self.btneq.clicked.connect(self.equals_btn)
        
        self.btn0.setFocusPolicy(Qt.NoFocus)
        self.btn1.setFocusPolicy(Qt.NoFocus)
        self.btn2.setFocusPolicy(Qt.NoFocus)
        self.btn3.setFocusPolicy(Qt.NoFocus)
        self.btn4.setFocusPolicy(Qt.NoFocus)
        self.btn5.setFocusPolicy(Qt.NoFocus)
        self.btn6.setFocusPolicy(Qt.NoFocus)
        self.btn7.setFocusPolicy(Qt.NoFocus)
        self.btn8.setFocusPolicy(Qt.NoFocus)
        self.btn9.setFocusPolicy(Qt.NoFocus)
        self.btnminus.setFocusPolicy(Qt.NoFocus)
        self.btndel.setFocusPolicy(Qt.NoFocus)
        self.btneq.setFocusPolicy(Qt.NoFocus)
        
        QShortcut(QKeySequence("Return"), self, self.equals_btn)
        QShortcut(QKeySequence("Enter"), self, self.equals_btn)
        QShortcut(QKeySequence("Backspace"), self, self.clear_text)
        
        
    def write_0(self):
        self.equation_box.setText(self.equation_box.text() + "0")        
        
    def write_1(self):
        self.equation_box.setText(self.equation_box.text() + "1")
        
    def write_2(self):
        self.equation_box.setText(self.equation_box.text() + "2")
        
    def write_3(self):
        self.equation_box.setText(self.equation_box.text() + "3")
        
    def write_4(self):
        self.equation_box.setText(self.equation_box.text() + "4")
        
    def write_5(self):
        self.equation_box.setText(self.equation_box.text() + "5")
        
    def write_6(self):
        self.equation_box.setText(self.equation_box.text() + "6")
        
    def write_7(self):
        self.equation_box.setText(self.equation_box.text() + "7")
        
    def write_8(self):
        self.equation_box.setText(self.equation_box.text() + "8")
        
    def write_9(self):
        self.equation_box.setText(self.equation_box.text() + "9")
        
    def write_minus(self):
        if self.equation_box.text() == "":
            self.equation_box.setText("-")
        
    def clear_text(self):
        self.equation_box.clear()
        
    def equals_btn(self):
        if self.item_box.text() == 'd':
            if "-" in self.equation_box.text():
                self.equation_box.setText("Degree must be positive integer")
                QTimer.singleShot(2000, self.equation_box.clear)
                return
            
            if self.equation_box.text() == "":
                self.equation_box.setText("Enter Degree of Equation")
                QTimer.singleShot(2000, self.equation_box.clear)
                return
            
            self._equation.append(self.equation_box.text())
            self._current_index_flag = int(self._equation[0])
            self.item_box.setText('x' + f'{PolynomialDerivative.superscripter(self._current_index_flag)}')
            self.sentence_box.setText("Enter Coefficient")
            self.equation_box.clear()
            return
            
        elif self.item_box.text() == 'a':
            self._equation = []
            self._current_index_flag = None
            self.equation_box.clear()
            self.item_box.setText("d")
            self.sentence_box.setText("Enter Degree of Equation")
            return
            
        else:
            if self._current_index_flag != 0:
                if self.equation_box.text() == "":
                    self.equation_box.setText("Enter Coefficient")
                    QTimer.singleShot(2000, self.equation_box.clear)
                    return
                    
                self._equation.append(self.equation_box.text())
                self._current_index_flag -= 1
                self.item_box.setText('x' + f'{PolynomialDerivative.superscripter(self._current_index_flag)}')
                self.equation_box.clear()
                return
            
            if self._current_index_flag == 0:
                if self.equation_box.text() == "":
                    self.equation_box.setText("Enter Coefficient")
                    QTimer.singleShot(3000, self.equation_box.clear)
                    return
                
                self._equation.append(self.equation_box.text())
                
                pd = PolynomialDerivative(int(self._equation.pop(0)))
                self._equation.reverse()
                pd.equation_list_input(self._equation)
                
                self.item_box.setText('a')
                self.sentence_box.setText("Your Answer")
                self.equation_box.setText(pd.answer)
                return
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
        

if __name__ == "__main__":
    main()