from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,
                             QRadioButton, QGroupBox)

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 300)


question_label = QLabel('Какой правильный ответ?')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

btn_OK = QPushButton('Ответить')

layout_question = QVBoxLayout()
layout_question.addWidget(question_label, alignment=Qt.AlignCenter)
layout_question.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layout_question.addStretch(1)
layout_question.addWidget(btn_OK, alignment=Qt.AlignCenter)
layout_question.addStretch(1)


result_label = QLabel('Правильно/Неправильно')
correct_answer_label = QLabel('Правильный ответ')

result_box = QGroupBox('Результат теста')

layout_result = QVBoxLayout()
layout_result.addWidget(result_label, alignment=Qt.AlignLeft | Qt.AlignTop)
layout_result.addWidget(correct_answer_label, alignment=Qt.AlignCenter)

result_box.setLayout(layout_result)

btn_next = QPushButton('Следующий вопрос')

layout_result_screen = QVBoxLayout()
layout_result_screen.addWidget(result_box, alignment=Qt.AlignCenter)
layout_result_screen.addWidget(btn_next, alignment=Qt.AlignCenter)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_question)
main_layout.addLayout(layout_result_screen) 


result_box.hide()
btn_next.hide()

def check_answer():
    RadioGroupBox.hide()
    btn_OK.hide()
    result_box.show()
    btn_next.show()

btn_OK.clicked.connect(check_answer)

def next_question():
    RadioGroupBox.show()
    btn_OK.show()
    result_box.hide()
    btn_next.hide()

btn_next.clicked.connect(next_question)

main_win.setLayout(main_layout)
main_win.show()
app.exec_()
