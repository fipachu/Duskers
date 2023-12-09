import random
from argparse import ArgumentParser
from enum import StrEnum, auto

from constants import *


class GameState(StrEnum):
    initializing = auto()
    quitting = auto()

    main_menu = auto()

    pre_play = auto()
    play = auto()
    explore = auto()
    save = auto()
    upgrade = auto()
    game_menu = auto()

    high_scores = auto()
    help = auto()


class Game:
    def __init__(self, config):
        self.config = config
        self.locations = config.locations.replace("_", " ").split(",")
        # Discard any "" locations
        self.locations = [location for location in self.locations if location]

        self.state = GameState.initializing

    @staticmethod
    def _get_input(prompt, lowercase=True):
        command = input(prompt)
        if lowercase:
            command = command.lower()
        print()
        return command

    def set_state(self, new_state):
        self.state = new_state

    def start_game(self):
        self.state = GameState.main_menu
        self.loop()

    def loop(self):
        while self.state != GameState.quitting:
            if self.state == GameState.main_menu:
                self.main_menu()

            elif self.state == GameState.pre_play:
                self.pre_play()
            elif self.state == GameState.explore:
                self.explore()
            elif self.state == GameState.save:
                self.save()
            elif self.state == GameState.upgrade:
                self.upgrade()
            elif self.state == GameState.game_menu:
                self._submenu()
            elif self.state == GameState.play:
                self.play()

            elif self.state == GameState.high_scores:
                self.high_scores()
            elif self.state == GameState.help:
                self.help()
        self.quit()

    @staticmethod
    def quit():
        print("Thanks for playing, bye!")

    def main_menu(self):
        print(TITLE)
        print("[Play]", "[High] Scores", "[Help]", "[Exit]", sep="\n", end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "play":
                self.state = GameState.pre_play
            elif command == "high":
                self.state = GameState.high_scores
            elif command == "help":
                self.state = GameState.help
            elif command == "exit":
                self.state = GameState.quitting
            else:
                print(INVALID_INPUT, end="\n\n")
                continue

            break

    def pre_play(self):
        name = self._get_input(NAME, False)

        print(f"Greetings, commander {name}!")
        print(
            "Are you ready to begin?",
            "    [Yes] [No] Return to Main [Menu]",
            sep="\n",
            end="\n\n",
        )

        while True:
            command = self._get_input(COMMAND)

            if command == "yes":
                self.state = GameState.play
                break
            elif command == "menu":
                self.state = GameState.main_menu
                break
            elif command == "no":
                print("How about now.")
            else:
                print(INVALID_INPUT, end="\n\n")

    def play(self):
        print(HUB, end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "ex":
                self.state = GameState.explore
                break
            elif command == "save":
                self.state = GameState.save
                break
            elif command == "up":
                self.state = GameState.upgrade
                break
            elif command == "m":
                self.state = GameState.game_menu
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    def explore(self):
        number_of_locations = random.randint(1, 9)

        locations = {}
        for i in range(1, number_of_locations + 1):
            locations[i] = random.choice(self.locations)

            print("Searching")
            for location_id, location in locations.items():
                print(f"[{location_id}] {location}")
            print()

            print("[S] to continue searching", end="\n\n")

            while True:
                command = self._get_input(COMMAND)
                if command == "s":
                    break
                else:
                    print(INVALID_INPUT, end="\n\n")

        # print("Nothing more in sight.\n"
        #       "       [Back]")
        self.state = GameState.play

    def save(self):
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting

    def upgrade(self):
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting

    def _submenu(self):
        print(MENU, end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "back":
                self.state = GameState.play
                break
            elif command == "main":
                self.state = GameState.main_menu
                break
            elif command == "save":
                print(COMING_SOON, end="\n\n")
                self.state = GameState.quitting
                break
            elif command == "exit":
                print(COMING_SOON, end="\n\n")
                self.state = GameState.quitting
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    def high_scores(self):
        print("No scores to display.", "    [Back]", end="\n\n")

        command = self._get_input(COMMAND)

        while True:
            if command == "back":
                self.state = GameState.main_menu
                break
            else:
                print(INVALID_INPUT, end="\n\n")
                command = self._get_input(COMMAND)

    def help(self):
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting


def get_config():
    parser = ArgumentParser()
    parser.add_argument("seed", nargs="?", type=str, default="0")
    parser.add_argument("min_animation_duration", nargs="?", type=int, default=0)
    parser.add_argument("max_animation_duration", nargs="?", type=int, default=0)
    parser.add_argument("locations", nargs="?", default=LOCATIONS)

    args = parser.parse_args()
    return args


def main():
    config = get_config()
    random.seed(config.seed)

    Game(config).start_game()


if __name__ == "__main__":
    main()
