import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        command = input()
        words = command.split()
        if command == "exit":
            break
        if words[0] == "echo":
            message = " ".join(words[1:])
            print(message)

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
