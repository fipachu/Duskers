import random
from argparse import ArgumentParser
from enum import StrEnum, auto

from constants import *


class GameState(StrEnum):
    initializing = auto()
    quitting = auto()

    main_menu = auto()

    loading = auto()

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
        self.location_names = config.locations.replace("_", " ").split(",")
        # Discard any "" locations
        self.location_names = [location for location in self.location_names if location]

        self.state = GameState.initializing

        self.titanium = 0

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

            elif self.state == GameState.loading:
                self.loading()

            elif self.state == GameState.pre_play:
                self.pre_play()
            elif self.state == GameState.explore:
                self.explore()
            elif self.state == GameState.save:
                self.save()
            elif self.state == GameState.upgrade:
                self.upgrade()
            elif self.state == GameState.game_menu:
                self.game_menu()
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
        print("[New] Game", "[Load] Game", "[High] Scores", "[Help]", "[Exit]", sep="\n", end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "new":
                self.state = GameState.pre_play
            elif command == "load":
                self.state = GameState.loading
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

    def loading(self):
        raise NotImplemented

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
        print(HUB.format(self.titanium), end="\n\n")

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
        locations_generator = self._get_locations(1, 9)

        locations = {}
        command = "s"  # First search runs automatically
        while True:
            if command == "s":
                print("Searching")

                try:
                    locations = next(locations_generator)

                    for location_id, location_data in locations.items():
                        print(f"[{location_id}] {location_data['name']}")
                    print()

                    print("[S] to continue searching")
                    print("[Back] to cancel exploration", end="\n\n")

                except StopIteration:
                    print("Nothing more in sight.\n       [Back]", end="\n\n")

            elif command == "back":
                break

            elif command.isdigit() and int(command) in locations:
                command = int(command)

                chosen_location = locations[command]["name"]
                titanium_found = locations[command]["titanium"]
                print(
                    f"Deploying robots\n"
                    f"{chosen_location} explored successfully, with no damage taken.\n"
                    f"Acquired {titanium_found} lumps of titanium."
                )
                self.titanium += titanium_found
                # Here I'd ask the player to acknowledge, where it not for the specification
                break

            else:
                print(INVALID_INPUT, end="\n\n")

            command = self._get_input(COMMAND)

        self.state = GameState.play

    def _get_locations(self, min_number, max_number):
        number_of_locations = random.randint(min_number, max_number)
        location_numbers = range(1, number_of_locations + 1)

        locations = {}
        for i in location_numbers:
            locations[i] = {
                "name": random.choice(self.location_names),
                "titanium": random.randint(10, 100),
            }

            yield locations

    def save(self):
        print("Select save slot:")
        print("[1] empty", "[2] empty", "[3] empty", "[Back]", sep="\n", end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "1":
                raise NotImplemented
            elif command == "2":
                raise NotImplemented
            elif command == "3":
                raise NotImplemented
            elif command == "back":
                self.state = GameState.play
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    def upgrade(self):
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting

    def game_menu(self):
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
    parser.add_argument("seed", nargs="?", type=str, default=None)
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
