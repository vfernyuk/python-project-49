from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100

def get_question_and_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    new_task = f'{first_number} {second_number}'
    correct_answer = str(gcd(first_number, second_number))
    return new_task, correct_answer
