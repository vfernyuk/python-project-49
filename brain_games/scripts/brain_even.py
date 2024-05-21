#!/usr/bin/env python3

from brain_games.engine_game import run_game
from brain_games.games import brain_even


def main():
    run_game(brain_even)


if __name__ == '__main__':
    main()
