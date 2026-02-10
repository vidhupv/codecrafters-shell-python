import sys


def main():
    # TODO: Uncomment the code below to pass the first stage

    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin = ["exit", "echo", "type"]
        words = command.split()
        if command == "exit":
            break
        elif words[0] == "echo":
            message = " ".join(words[1:])
            print(message)
        elif words[0] == "type":
            if words[1] in builtin:
                print(f"{words[1]} is a shell builtin")
            else:
                print(f"{words[1]}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
