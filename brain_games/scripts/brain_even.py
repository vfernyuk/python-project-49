#!/usr/bin/env python3

from brain_games.game_rules import rules
from brain_games.games.brain_even import get_question
from brain_games.games.brain_even import question


def main():
    rules(question, get_question)


if __name__ == '__main__':
    main()
