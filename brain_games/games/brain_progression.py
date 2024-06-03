from random import randint


description = 'What number is missing in the progression?'


def generate_progression():
    # Расчитываем арифметическую последовательность
    min_initial_term = 1
    max_initial_term = 10
    initial_term = randint(min_initial_term, max_initial_term)
    min_constant_diff = 1
    max_constant_diff = 10
    constant_diff = randint(min_constant_diff, max_constant_diff)
    final_term = 100
    # Длина рассчитываемой прогрессии будет равна 10 элементам
    return list(range(initial_term, final_term, constant_diff))[:10]


def hide_element(progression):
    # Скрываем один элемент прогрессии
    random_index = randint(0, 9)
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
