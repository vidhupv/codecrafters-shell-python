import os
import subprocess
import sys
from posixpath import isfile


def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin = ["exit", "echo", "type"]
        words = command.split()
        shell_command = words[0]
        command_strip = command[5:].strip()
        path_string = os.getenv("PATH")

        if shell_command in builtin:
            if command == "exit":
                break
            elif shell_command == "echo":
                message = " ".join(words[1:])
                print(message)
            elif shell_command == "type":
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
            if path_string:
                paths = path_string.split(os.pathsep)
                for path in paths:
                    if os.path.isfile and os.access(
                        path + f"/{shell_command}", os.X_OK
                    ):
                        full_path = os.path.join(path, shell_command)
                        result = subprocess.run([shell_command, command_strip])
                else:
                    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
