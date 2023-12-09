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
    def __init__(self):
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
            print(HUB, end="\n\n")
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
        print(COMING_SOON, end="\n\n")
        self.state = GameState.quitting

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


def main():
    Game().start_game()


if __name__ == "__main__":
    main()
