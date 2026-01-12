import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
BOOL = True + False
print(BOOL)
all_cards = {
    'Ace of hearts': 11, '2 of hearts': 2, '3 of hearts': 3, '4 of hearts': 4, '5 of hearts': 5, '6 of hearts': 6, '7 of hearts': 7, '8 of hearts': 8, '9 of hearts': 9, '10 of hearts': 10, 'Jack of hearts': 10, 'Queen of hearts': 10, 'King of hearts': 10, 'Ace of spades': 11, '2 of spades': 2, '3 of spades': 3, '4 of spades': 4, '5 of spades': 5, '6 of spades': 6, '7 of spades': 7, '8 of spades': 8, '9 of spades': 9, '10 of spades': 10, 'Jack of spades': 10, 'Queen of spades': 10, 'King of spades': 10, 'Ace of diamonds': 11, '2 of diamonds': 2, '3 of diamonds': 3, '4 of diamonds': 4, '5 of diamonds': 5, '6 of diamonds': 6, '7 of diamonds': 7, '8 of diamonds': 8, '9 of diamonds': 9, '10 of diamonds': 10, 'Jack of diamonds': 10, 'Queen of diamonds': 10, 'King of diamonds': 10, 'Ace of clubs': 11, '2 of clubs': 2, '3 of clubs': 3, '4 of clubs': 4, '5 of clubs': 5, '6 of clubs': 6, '7 of clubs': 7, '8 of clubs': 8, '9 of clubs': 9, '10 of clubs': 10, 'Jack of clubs': 10, 'Queen of clubs': 10, 'King of clubs': 10 
}
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.buttonhit = QPushButton("Hit")
        self.buttonhit.setCheckable(True)
        self.buttonhit.clicked.connect(self.hit)
        self.buttonstand = QPushButton("Stand")
        self.buttonstand.setCheckable(True)
        self.buttonstand.clicked.connect(self.stand)
        self.playercard1 = QLabel("2")
        self.playercard1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.playercard2 = QLabel("Ace")
        self.playercard2.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.buttonhit)
        layout.addWidget(self.buttonstand)
        layout.addWidget(self.playercard1)
        layout.addWidget(self.playercard2)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    def hit(self):
        print("hit")
    def stand(self):
        print("stand")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()














