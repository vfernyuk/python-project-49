from random import randint
from random import choice
from operator import add
from operator import sub
from operator import mul

question = 'What is the result of the expression?'


def operation(symbol):
    if symbol == '+':
        return add
    elif symbol == '-':
        return sub
    elif symbol == '*':
        return mul


def get_question():
    first_number = randint(1, 50)
    second_number = randint(1,50)
    symbol = choice('+-*')
    correct_answer = str(operation(symbol)(first_number,second_number))
    if first_number >= second_number:
        result = f'{first_number} {symbol} {second_number}'
    else:
        result = f'{second_number} {symbol} {first_number}' 
    return correct_answer, result
