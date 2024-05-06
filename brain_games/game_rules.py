import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rules(game):
    name = greet()
    print(game.question)
    counter = 0
    rounds = 3
    while counter < rounds:
        new_task, correct_answer = game.get_question()
        print(f'Question: {new_task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct')
            counter += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.'
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return
    if counter == rounds:
        print(f'Congratulations, {name}!')
