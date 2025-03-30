from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
                             QMessageBox, QRadioButton, QGroupBox)

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.resize(400, 250)
question_label = QLabel('Какой правильный ответ?')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_line = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout (layout_ans2)
layout_ans1.addLayout (layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

btn_OK = QPushButton('OK')

layout_line.addWidget(btn_OK)

layout_line = QVBoxLayout()
layout_line.addWidget(question_label, alignment=Qt.AlignCenter)
layout_line.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layout_line.addStretch(1)
layout_line.addWidget(btn_OK, alignment=Qt.AlignCenter)
layout_line.addStretch(1)



question = QLabel('Самый сложный вопрос в мире')

BOX = QGroupBox('Результат теста')

Lab = QLabel('Привально/Неправильно')

Labe = QLabel('Правельный ответ')

ver = QVBoxLayout()
ver.addWidget(Lab, alignment= (Qt.AlignLeft|Qt.AlignTop))
ver.addWidget(Labe, alignment= Qt.AlignCenter)

BOX.setLayout(ver)

Ceck = QPushButton()
Ceck.setText('Следующий вопрос')

lay = QVBoxLayout()

lay.addWidget(question, alignment = Qt.AlignCenter)
lay.addWidget(BOX, alignment = Qt.AlignCenter)
lay.addWidget(Ceck, alignment = Qt.AlignCenter)

l = QHBoxLayout()
l.addLayout(layout_line)
l.addLayout(lay)

main_win.setLayout(l)
main_win.show()
app.exec_()
