from random import randint


DESCRIPTION = 'What number is missing in the progression?'
MIN_INITIAL_TERM = 1
MAX_INITIAL_TERM = 10
MIN_CONSTANT_DIFF = 1
MAX_CONSTANT_DIFF = 10
FINAL_TERM = 100
LEN_PROGR = 10
INDEX_MIN = 0
INDEX_MAX = LEN_PROGR - 1


def generate_progression():
    # Расчитываем арифметическую последовательность
    initial_term = randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    constant_diff = randint(MIN_CONSTANT_DIFF, MAX_CONSTANT_DIFF)
    progression = [initial_term + constant_diff * i for i in range(LEN_PROGR)]
    return progression


def hide_element(progression):
    # Скрываем один элемент прогрессии, состоящей из 10 членов(LEN_PROGR)
    random_index = randint(INDEX_MIN, INDEX_MAX)
    hidden_number = progression[random_index]
    progression[random_index] = '..'
    return progression, hidden_number


def get_question_and_answer():
    progression = generate_progression()
    progression, hidden_number = hide_element(progression)
    # Вычисляем правильный ответ
    new_task = ' '.join(map(str, progression))
    correct_answer = str(hidden_number)
    return new_task, correct_answer
