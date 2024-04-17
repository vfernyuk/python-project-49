#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.brain_even import get_question_and_answer
from brain_games.games.brain_even import question


def main():
    question()
    get_question_and_answer()


if __name__ == '__main__':
    main()

