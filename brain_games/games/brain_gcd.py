from random import randint
from math import gcd

description = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    min_number = 1
    max_number = 100
    first_number = randint(min_number, max_number)
    second_number = randint(min_number, max_number)
    new_task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return new_task, correct_answer
