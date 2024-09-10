from PyQt5.QtWidgets import QWidget, QApplication
from layout_quizz import *

app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("MemoryCard")
window.setLayout(main_line_quizz)
window.show()

app.exec()





















