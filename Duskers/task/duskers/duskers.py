import datetime
import json
import os.path
import random
from argparse import ArgumentParser
from bisect import insort
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
        self.upgrades = []

        self.config = config
        self.location_names = config.locations.replace("_", " ").split(",")
        # Discard any "" locations
        self.location_names = [location for location in self.location_names if location]

        self.gamestate = GameState.initializing
        self.next_gamestate = None

        self.player_name = None
        # They are called DRONES! Not robots... Have it your way Hyperskill... for now.
        self.robots = 3
        self.titanium = 0

        self.savefile = "save_file.json"
        self.init_savefile()
        self.score_file = "high_scores.json"
        self.init_scores_file()

    def init_savefile(self):
        if not os.path.isfile(self.savefile):
            with open(self.savefile, "w") as f:
                json.dump({"1": {}, "2": {}, "3": {}}, f, indent=2)

    def read_savefile(self):
        with open(self.savefile, "r") as f:
            savestate = json.load(f)
        return savestate

    def init_scores_file(self):
        if not os.path.isfile(self.score_file):
            with open(self.score_file, "w") as f:
                json.dump([], f, indent=2)

    def read_scores_file(self):
        with open(self.score_file, "r") as f:
            high_scores = json.load(f)
        return high_scores

    @staticmethod
    def _get_input(prompt, lowercase=True):
        command = input(prompt)
        if lowercase:
            command = command.lower()
        print()
        return command

    def set_state(self, gamestate, next_gamestate=None):
        self.gamestate = gamestate
        self.next_gamestate = next_gamestate

    def start_game(self):
        self.set_state(GameState.main_menu)
        self.controller()

    def controller(self):
        while self.gamestate != GameState.quitting:
            if self.gamestate == GameState.main_menu:
                self.main_menu()

            elif self.gamestate == GameState.loading:
                self.load()

            elif self.gamestate == GameState.pre_play:
                self.pre_play()
            elif self.gamestate == GameState.explore:
                self.explore()
            elif self.gamestate == GameState.save:
                self.save_menu()
            elif self.gamestate == GameState.upgrade:
                self.upgrade()
            elif self.gamestate == GameState.game_menu:
                self.game_menu()
            elif self.gamestate == GameState.play:
                self.play()

            elif self.gamestate == GameState.high_scores:
                self.high_scores()
            elif self.gamestate == GameState.help:
                self.help()
        self.quit()

    @staticmethod
    def quit():
        print("Thanks for playing, bye!")

    def main_menu(self):
        print(TITLE)
        print(
            "[New] Game",
            "[Load] Game",
            "[High] Scores",
            "[Help]",
            "[Exit]",
            sep="\n",
            end="\n\n",
        )

        while True:
            command = self._get_input(COMMAND)

            if command == "new":
                self.set_state(GameState.pre_play)
            elif command == "load":
                self.set_state(GameState.loading)
            elif command == "high":
                self.set_state(GameState.high_scores)
            elif command == "help":
                self.set_state(GameState.help)
            elif command == "exit":
                self.set_state(GameState.quitting)
            else:
                print(INVALID_INPUT, end="\n\n")
                continue

            break

    def load(self):
        savestate = self.read_savefile()

        print("Select save slot:")
        self.print_slots(savestate)
        print("[Back]", end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command in savestate:
                chosen_slot = savestate[command]

                self.player_name = chosen_slot["player_name"]
                self.titanium = chosen_slot["titanium"]
                self.robots = chosen_slot["robots"]
                self.upgrades = chosen_slot["upgrades"]

                print(LOADED, sep="\n\n")
                print(GREETING.format(self.player_name), end="\n\n")

                self.set_state(GameState.play)
                break
            elif command == "back":
                self.set_state(GameState.main_menu)
                break
            else:
                print(INVALID_INPUT)

    def pre_play(self):
        self.player_name = self._get_input(NAME, False)

        print(GREETING.format(self.player_name))
        print(
            "Are you ready to begin?",
            "    [Yes] [No] Return to Main [Menu]",
            sep="\n",
            end="\n\n",
        )

        while True:
            command = self._get_input(COMMAND)

            if command == "yes":
                self.set_state(GameState.play)
                break
            elif command == "menu":
                self.set_state(GameState.main_menu)
                break
            elif command == "no":
                print("How about now.")
            else:
                print(INVALID_INPUT, end="\n\n")

    def play(self):
        self._print_hub(5, "|")
        print()

        while True:
            command = self._get_input(COMMAND)

            if command == "ex":
                self.set_state(GameState.explore)
                break
            elif command == "save":
                self.set_state(GameState.save, GameState.play)
                break
            elif command == "up":
                self.set_state(GameState.upgrade)
                break
            elif command == "m":
                self.set_state(GameState.game_menu)
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    def _print_hub(self, padding, separator):
        padding = padding * " "
        drones = []
        for line in DRONE.split("\n"):
            # Extra empty column before the first drone
            new_line = [" "]
            for i in range(self.robots):
                new_line.append(
                    padding
                    + line
                    # No characters after the last drone
                    + (padding + separator if i < self.robots - 1 else "")
                )
            drones.append("".join(new_line))
        drones = "\n".join(drones)
        print(HUB.format(drones, self.titanium))

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
                        output = [f"[{location_id}] {location_data['name']}"]
                        if "1" in self.upgrades:
                            output.append(f"Titanium:{location_data['titanium']}")
                        if "2" in self.upgrades:
                            output.append(
                                f"Encounter_rate:{location_data['encounter_rate']:.0%}"
                            )
                        output = " ".join(output)
                        print(output)
                    print()

                    print("[S] to continue searching")
                    print("[Back] to cancel exploration", end="\n\n")

                except StopIteration:
                    print("Nothing more in sight.\n       [Back]", end="\n\n")

            elif command == "back":
                break

            elif command.isdigit() and int(command) in locations:
                command = int(command)
                location = locations[command]

                is_encounter = random.random() < location["encounter_rate"]

                print(f"Deploying robots...")
                if is_encounter and self.robots <= 1:
                    print("Enemy encounter!!!")
                    print("Mission aborted, the last robot lost...")
                    print(GAME_OVER)
                    self.save_score()
                    self.set_state(GameState.main_menu)
                    return
                else:
                    if is_encounter:
                        print("Enemy encounter")
                    print(f"{location['name']} explored successfully, ", end="")
                    print("1 robot lost." if is_encounter else "with no damage taken.")
                    print(
                        f"Acquired {location['titanium']} lumps of titanium.",
                        end="\n\n",
                    )

                    self.titanium += location["titanium"]
                    if is_encounter:
                        self.robots -= 1
                    # Here I'd ask the player to acknowledge, where it not for
                    # the specification
                    break

            else:
                print(INVALID_INPUT, end="\n\n")

            command = self._get_input(COMMAND)

        self.set_state(GameState.play)

    def save_score(self):
        high_scores = self.read_scores_file()

        # Note the minus in the lambda. It should ensure that high scores are sorted
        # in reverse (descending) order.
        insort(high_scores, [self.titanium, self.player_name], key=lambda x: -x[0])
        while len(high_scores) > 10:
            high_scores.pop()

        with open(self.score_file, "w") as f:
            json.dump(high_scores, f)

    def _get_locations(self, min_number, max_number):
        number_of_locations = random.randint(min_number, max_number)
        location_numbers = range(1, number_of_locations + 1)

        locations = {}
        for i in location_numbers:
            locations[i] = {
                "name": random.choice(self.location_names),
                "titanium": random.randint(10, 100),
                "encounter_rate": random.random(),
            }

            yield locations

    def save_menu(self):
        savestate = self.read_savefile()

        print("Select save slot:")
        self.print_slots(savestate)
        print("[Back] to game", end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command in savestate:
                savestate[command] = {
                    "player_name": self.player_name,
                    "titanium": self.titanium,
                    "robots": self.robots,
                    "upgrades": self.upgrades,
                    "last_save": str(datetime.datetime.now()),
                }
                self.save(savestate)

                print(SAVED, end="\n\n")

                # If next_gamestate is not set, fallback to play
                self.set_state(self.next_gamestate or GameState.play)
                break
            elif command == "back":
                self.set_state(GameState.play)
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    @staticmethod
    def print_slots(savestate):
        for slot, data in savestate.items():
            if data:
                print(
                    f"[{slot}] "
                    f"{data['player_name']} "
                    f"Titanium:{data['titanium']} "
                    f"Robots:{data['robots']} "
                    f"Last_save:{data['last_save']}"
                )
            else:
                print(f"[{slot}] empty")

    def save(self, savestate):
        with open(self.savefile, "w") as f:
            json.dump(savestate, f, indent=2)

    def upgrade(self):
        print(UPGRADE_MENU)

        while True:
            command = self._get_input(COMMAND)

            if command == "back":
                self.set_state(GameState.play)
                break
            elif command in UPGRADES:
                upgrade = UPGRADES[command]
                if self.titanium < upgrade["price"]:
                    print("Not enough titanium!")
                elif upgrade["name"] in self.upgrades:
                    print(f"You already own {upgrade['name']}!")
                else:
                    self.upgrades.append(command)
                    self.titanium -= upgrade["price"]
                    print(f"Purchase successful. {upgrade['description']}")
                    break
            elif command in ITEMS:
                # Luckily a new robot is the only item in the shop
                new_robot = ITEMS[command]
                if self.titanium < new_robot["price"]:
                    print("Not enough titanium!")
                elif self.robots >= 4:
                    print("Robot bay at max capacity!")
                else:
                    self.robots += 1
                    self.titanium -= new_robot["price"]
                    print(f"Purchase successful. {new_robot['description']}")
                    break
            else:
                print(INVALID_INPUT)
        self.gamestate = GameState.play

    def game_menu(self):
        print(MENU, end="\n\n")

        while True:
            command = self._get_input(COMMAND)

            if command == "back":
                self.set_state(GameState.play)
                break
            elif command == "main":
                self.set_state(GameState.main_menu)
                break
            elif command == "save":
                self.set_state(GameState.save, GameState.quitting)
                break
            elif command == "exit":
                self.set_state(GameState.quitting)
                break
            else:
                print(INVALID_INPUT, end="\n\n")

    def high_scores(self):
        print("No scores to display.", "    [Back]", end="\n\n")

        command = self._get_input(COMMAND)

        while True:
            if command == "back":
                self.set_state(GameState.main_menu)
                break
            else:
                print(INVALID_INPUT, end="\n\n")
                command = self._get_input(COMMAND)

    def help(self):
        print(COMING_SOON, end="\n\n")
        self.set_state(GameState.play)


def get_config():
    parser = ArgumentParser()
    parser.add_argument("seed", nargs="?", type=str, default=None)
    # No animations implemented as of commit ad068a38
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
