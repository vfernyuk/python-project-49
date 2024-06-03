from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    min_number = 1
    max_number = 100
    random_number = randint(min_number, max_number)
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return random_number, result
