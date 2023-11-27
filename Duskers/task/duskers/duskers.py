TITLE = """\
+===========================================================================================+
  ######*   ##*  ##*  ######*   ##*   ##*  #######*  ##*  ##*  #######*  ######*   #######*
  ##*  ##*  ##*  ##*  ##*  ##*  ##*   ##*  ##*       ##* ##*   ##*       ##*  ##*  ##*
  ######*    #####*   ##*  ##*  ##*   ##*  #######*  #####*    #####*    ######*   #######*
  ##*         ##*     ##*  ##*  ##*   ##*       ##*  ##* ##*   ##*       ##*  ##*       ##*
  ##*         ##*     ######*    ######*   #######*  ##*  ##*  #######*  ##*  ##*  #######*
                                (Survival ASCII Strategy Game)
+===========================================================================================+\
"""

HUB = """\
__________(LOG)__________________________________________________(LOG)__________
+==============================================================================+
         $()$()$      |      $()$()$     |      $()$()$
        $$.....$$     |     $$.....$$    |     $$.....$$
         $$$$$$$      |      $$$$$$$     |      $$$$$$$
        $$$...$$$     |     $$$...$$$    |     $$$...$$$
        $~$$$$$~$     |     $~$$$$$~$    |     $~$$$$$~$
+==============================================================================+
|                  [Ex]plore                          [Up]grade                |
|                  [Save]                             [M]enu                   |
+==============================================================================+\
"""

MENU = """\
                          |==========================|
                          |            MENU          |
                          |                          |
                          | [Back] to game           |
                          | Return to [Main] Menu    |
                          | [Save] and exit          |
                          | [Exit] game              |
                          |==========================|\
"""

COMMAND = "Your command:\n"
NAME = "Enter your name:\n"

INVALID_INPUT = "Invalid input\n"
COMING_SOON = "Coming SOON! Thanks for playing!"


def _get_input(prompt, lowercase=True):
    command = input(prompt)
    if lowercase:
        command = command.lower()
    print()
    return command


def play():
    name = _get_input(NAME, False)

    print(f"Greetings, commander {name}!")
    print(
        "Are you ready to begin?",
        "    [Yes] [No] Return to Main [Menu]",
        sep="\n",
        end="\n\n",
    )
    while True:
        command = _get_input(COMMAND)

        if command == "yes":
            while True:
                print(HUB, end="\n\n")
                command = _get_input(COMMAND)

                if command == "ex":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "save":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "up":
                    print(COMING_SOON, end="\n\n")
                    return True
                elif command == "m":
                    print(MENU, sep="\n\n")

                    command = _get_input(COMMAND)

                    if command == "back":
                        pass
                    elif command == "main":
                        return False
                    elif command == "save":
                        print(COMING_SOON, end="\n\n")
                        return True
                    elif command == "exit":
                        print(COMING_SOON, end="\n\n")
                        return True

        elif command == "no":
            print("How about now.")
        elif command == "menu":
            return False
        else:
            print(INVALID_INPUT)


def main_menu():
    while True:
        print(TITLE)
        print("[Play]", "[High] Scores", "[Help]", "[Exit]", sep="\n", end="\n\n")

        while True:
            command = _get_input(COMMAND)

            if command == "play":
                exit_game = play()
                if exit_game:
                    return
                else:
                    break
            elif command == "high":
                print("No scores to display.", "    [Back]", end="\n\n")

                command = _get_input(COMMAND)

                while command != "back":
                    print(INVALID_INPUT)
                    command = _get_input(COMMAND)

                break

            elif command == "help":
                print(COMING_SOON, end="\n\n")
                return
            elif command == "exit":
                print("Thanks for playing, bye!")
                return
            else:
                print(INVALID_INPUT)


def main():
    main_menu()


if __name__ == "__main__":
    main()
