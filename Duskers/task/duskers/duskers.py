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

COMMAND = "Your command:\n"
NAME = "Enter your name:\n"

INVALID_INPUT = "Invalid input\n"


def _get_input(prompt, lowercase=True):
    command = input(prompt)
    if lowercase:
        command = command.lower()
    print()
    return command


def play():
    name = _get_input(NAME, False)

    print(f"Greetings, commander {name}!")
    print("Are you ready to begin?", "    [Yes] [No]", sep="\n", end="\n\n")
    while True:
        command = _get_input(COMMAND)

        if command == "yes":
            print("Great, now let's go code some more ;)")
            return
        elif command == "no":
            print("How about now.")
        else:
            print(INVALID_INPUT)


def menu():
    print("[Play]", "[Exit]", sep="\n", end="\n\n")

    while True:
        command = _get_input(COMMAND)

        if command == "play":
            return play()
        elif command == "exit":
            print("Thanks for playing, bye!")
            return
        else:
            print(INVALID_INPUT)


def main():
    print(TITLE)
    menu()


if __name__ == "__main__":
    main()
