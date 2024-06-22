from random import randint


DESCRIPTION = 'What number is missing in the progression?'
MIN_INITIAL_TERM = 1
MAX_INITIAL_TERM = 10
MIN_CONSTANT_DIFF = 1
MAX_CONSTANT_DIFF = 10
LEN_PROGR = 10
INDEX_MIN = 0
INDEX_MAX = LEN_PROGR - 1


def generate_progression(initial_term, constant_diff, LEN_PROGR):
    progression = [initial_term + constant_diff * i for i in range(LEN_PROGR)]
    return progression


def progression_hidden(progression, hidden_element_index):
    progression[hidden_element_index] = '..'
    new_task = ' '.join(map(str, progression))
    return new_task


def get_question_and_answer():
    initial_term = randint(MIN_INITIAL_TERM, MAX_INITIAL_TERM)
    constant_diff = randint(MIN_CONSTANT_DIFF, MAX_CONSTANT_DIFF)
    hidden_element_index = randint(INDEX_MIN, INDEX_MAX)
    progression = generate_progression(initial_term, constant_diff, LEN_PROGR)
    correct_answer = str(progression[hidden_element_index])  # Сохраняем пропущенное число
    new_task = progression_hidden(progression, hidden_element_index)
    return new_task, correct_answer