import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout, QLabel,QLineEdit
from datetime import datetime

class AgeCalculator( QWidget ):
    def __init__( self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid  = QGridLayout()
        name_label = QLabel("Name:")
        name_line_edit = QLineEdit()

        dbirth_label = QLabel("Date of Birth (YYYY-MM-DD):")
        self.dbirth_line_edit = QLineEdit()

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(name_line_edit, 0, 1)
        grid.addWidget(dbirth_label, 1, 0)
        grid.addWidget(self.dbirth_line_edit, 1, 1)

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)
    
    def calculate_age(self):
        current_date = datetime.now().year
        date_of_birth = self.dbirth_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date().year
        age = current_date - int(year_of_birth)
        self.output_label.setText(f"Your age is: {age} years")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())