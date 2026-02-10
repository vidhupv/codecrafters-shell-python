import os
import sys


def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin = ["exit", "echo", "type"]
        words = command.split()
        command_strip = command[5:].strip()
        path_string = os.getenv("PATH")
        if command == "exit":
            break
        elif words[0] == "echo":
            message = " ".join(words[1:])
            print(message)
        elif words[0] == "type":
            if words[1] in builtin:
                print(f"{words[1]} is a shell builtin")
            elif path_string:
                paths = path_string.split(os.pathsep)
                found = False
                for path in paths:
                    if os.access(path + f"/{command_strip}", os.X_OK):
                        print(f"{command_strip} is {path}/{command_strip}")
                        found = True
                        break

                if not found:
                    print(f"{command_strip}: not found")
            else:
                print(f"{words[1]}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
