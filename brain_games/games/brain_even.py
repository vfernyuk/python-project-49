from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return random_number, result
