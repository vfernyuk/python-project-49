from random import randint


description = 'What number is missing in the progression?'


def make_progression():
    # Расчитываем арифметическую последовательность
    start_progression = randint(1, 10)
    step_progression = randint(1, 10)
    progression = list(range(start_progression, 100, step_progression))[:10]
    # Скрываем один элемент прогрессии
    random_index = randint(0, 9)
    hidden_number = progression[random_index]
    progression[random_index] = '..'
    # Вычисляем правильный ответ
    new_task = ' '.join(map(str, progression))
    correct_answer = str(hidden_number)
    return new_task, correct_answer
