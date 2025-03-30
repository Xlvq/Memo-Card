import json
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel
)


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

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

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

questions_list = [
    Question('Государственный язык Бразилии?', 'Португальский', 'Бразильский', 'Испанский', 'Английский'),
    Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'),
    Question('Национальная валюта Японии?', 'Иена', 'Юань', 'Рупия', 'Вон'),
    Question('Сколько дней в високосном году?', '366', '365', '364', '360'),
    Question('Как называется столица Канады?', 'Оттава', 'Торонто', 'Ванкувер', 'Монреаль'),
]

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

# ----------------------------------------------------------
# Функции:
# ----------------------------------------------------------

def show_result():
    """Показать панель ответа"""
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    """Показать панель с вопросом"""
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)  # снять ограничения выбора
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # вернуть ограничения


def ask(q: Question):
    """Выводит вопрос на экран"""
    lb_Question.setText(q.question)  # Исправлено
    lb_Correct.setText(q.right_answer)  # Исправлено

    random.shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    show_question()


def check_answer():
    """Проверка ответа пользователя"""
    selected = None
    for btn in answers:
        if btn.isChecked():
            selected = btn.text()

    if selected == lb_Correct.text():
        lb_Result.setText("Правильно!")
    else:
        lb_Result.setText("Неправильно!")

    show_result()


def next_question():
    """Выбирает следующий случайный вопрос"""
    current_question = random.choice(questions_list)
    ask(current_question)


btn_OK.clicked.connect(lambda: check_answer() if btn_OK.text() == "Ответить" else next_question())

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

next_question()  # Первый вопрос
window.show()
app.exec()
