from random import randint
from math import gcd

question = 'Find the greatest common divisor of given numbers.'


def get_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    new_task = f'{first_number} {second_number}'
    correct_answer = gcd(first_number,second_number)
    return new_task, correct_answer
