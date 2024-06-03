from random import randint
from random import choice
from operator import add
from operator import sub
from operator import mul

description = 'What is the result of the expression?'


def operation(symbol):
    if symbol == '+':
        return add
    elif symbol == '-':
        return sub
    elif symbol == '*':
        return mul


def get_question_and_answer():
    min_number = 1
    max_number = 50
    first_number = randint(min_number, max_number)
    second_number = randint(min_number, max_number)
    symbol = choice('+-*')
    if first_number >= second_number:
        new_task = f'{first_number} {symbol} {second_number}'
    else:
        new_task = f'{second_number} {symbol} {first_number}'
    correct_answer = str(abs(operation(symbol)(first_number, second_number)))
    return new_task, correct_answer
