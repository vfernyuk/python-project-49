from random import randint


question = 'What number is missing in the progression?'


def get_question():
    first_number_progression = randint(1, 10)
    step_progression = randint(1, 10)
    progression = list(range(first_number_progression, 100, step_progression))
    lenght_progression = 10
    limited_progression = progression[:lenght_progression]
    random_index = randint(0, 9)
    hidden_number = progression[random_index]
    progression[random_index] = '..'
    new_task = ' '.join(map(str, progression)
    correct_answer = str(hidden_number)
    return new_task, correct_answer
 