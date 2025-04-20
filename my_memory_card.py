#создай приложение для запоминания информации
from PyQt5.QtCore import Qt #Создание пустого окна
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QButtonGroup
from random import randint
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Кто выиграл лигу чемпионов в 2015 году', 'Барселона', 'Реал Мадрид', 'Бавария', 'Ювентус'))
question_list.append(Question('Кто из этих игроков не когда не выигрывал чемпионат мира', 'Роналду', 'Иньеста', 'Буффон', 'Мюллер'))
question_list.append(Question('Кто оскорбил сестру Зидана в финале чемпионата мира ', 'Матераци', 'Буффон', 'Ван перси', 'Маттеус'))
question_list.append(Question('Кто выиграл чемпионат мира в 2022 году ', 'Аргентина', 'Бразилия', 'Фрвнция', 'Нидерланды'))
question_list.append(Question('Кто выиграл золотой мяч в 2023 году', 'Месси', 'Холланд', 'Мбаппе', 'Родри'))
question_list.append(Question('Какой самый титулованый клуб Россий', 'Спартак', 'Зенит', 'Цска', 'Краснодар'))
# q = question('Кто из этих футболистов никогда не играл в РПЛ?', 'Роберто Карлос', 'Тьяго Сильва', 'Паредес', 'Икарди')
app = QApplication([]) #Конструктор создающий обьект типа приложения
main_win = QWidget() #Конструктор создающий объект типа окно
main_win.setWindowTitle('Memory Card') #Установить заголовок окна
main_win.move(900, 70) #Сдвиг экрана
main_win.resize(400, 200) #Размер экрана
RadioGroupBox = QGroupBox('Варианты ответов') #Группировка кнопок
rbtn_1 = QRadioButton('Месси')
rbtn_2 = QRadioButton('Неймар')
rbtn_3 = QRadioButton('Роналду')
rbtn_4 = QRadioButton('Левандовский') #Создать кнопку с переключателем

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
#2 окно
AnsGroupBox = QGroupBox('Результат теста')

result = QLabel('Правильно \ неправильно')
itog = QLabel('Тут будет верный ответ')

# RadioGroupBox.hide() #Временно спрятали варианты ответа
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog, Qt.AlignCenter | Qt.AlignVCenter)
AnsGroupBox.setLayout(layout_res)

glav = QVBoxLayout() #Главный комплектовщик где все находится
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

text = QLabel('Кто выиграл золотой мяч в 2023 году?')
line1.addWidget(text) #На линию 1 добавили вопрос
glav.addLayout(line1) #В главный комплектовщик добавили линию 1

main_win.setLayout(glav) #Показали главный комплектовщик в окне
line2.addWidget(RadioGroupBox) #На линию 2 добавили группу ответов
AnsGroupBox.hide()
line2.addWidget(AnsGroupBox)
glav.addLayout(line2) #В главный комплектовщик добавили линию 2
button = QPushButton('Ответить')
line3.addWidget(button)
glav.addLayout(line3)

def show_result(): #Панель ответов
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question(): #Панель с вопросом и вариантами ответов
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers) #Метод для перемешивания списка из кнопок
    answers [0].setText(q.right_answer)
    answers [1].setText(q.wrong1)
    answers [2].setText(q.wrong2)
    answers [3].setText(q.wrong3)
    text.setText(q.question) #Вопрос
    itog.setText(q.right_answer)
    show_question() #Функция с панелью

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers [1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0 #Обнуляем счетчик
    q = question_list[main_win.cur_question] #Взяли вопрос
    ask(q)
def click_ok():
    if button.text() == 'Ответить' :
        check_answer()
    else:
        next_question()

main_win.cur_question = -1 #Создали номер вопроса









next_question()
button.clicked.connect(click_ok)


# text = QLabel('Нажми чтобы узнать победителя') #Надпись
# winner = QLabel('?')
# button = QPushButton('Сгенерировать')

# line = QVBoxLayout() #коробочка для хранения виджетов
# line.addWidget(text, alignment = Qt.AlignCenter ) #Текст в коробочку добавили
# line.addWidget(winner, alignment = Qt.AlignCenter ) #Текст в коробочку добавили
# line.addWidget(button, alignment = Qt.AlignCenter) #Кнопку в коробочку добавили
# main_win.setLayout(line)
# def show_ winner():
#     number = randint(0, 99)
#     winner.setText(str(number)) #Метод изменяющий текст надписи
#     text.setText('Победитель:')

# button.clicked.connect(show_winner)




main_win.show() #Сделать окно видимым
app.exec_() #Оставлять приложение открытым пока не будет нажата кнопка выхода

#привязка элементов к вертикальной лини

#обработка событий

#запуск приложения