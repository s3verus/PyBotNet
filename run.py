#!/usr/bin/python3

from os import system


def logo():
    print(
        "\n                00000000000000000000        \n"
        "                ********************     4  \n"
        "         **    ****( . )****( . )***     8  \n"
        "         ***************************     8  \n"
        "           ***  00000000000000000000     8  \n"
        "         ***    000  0000000000  000     8  \n"
        "         *      000              000   00807\n"
        "                00000000000000000000000000  \n"
        "                00000000000000000000     0  \n"
        "                00000000000000000000        \n"
        "                00000          00000        \n"
        "                00000          00000        \n"
        "                                            \n"
        "                 created by:  S3verus       \n")


if __name__ == "__main__":
    logo()
    input("please enter for obfuscate your BotNet...")
    command = "pyarmor obfuscate PyBots.py"
    system(command)
    input("please copy your icon.icon to /dist directory and enter for create executable file...")
    command = "cd dist"
    system(command)
    # i will change it soon
    output = input("what is your target OS? (1.windows/2.linux)\n")
    if output == "1" or output == "windows" or output == "1.windows":
        command = "pyinstaller --noconsole --clean -i icon.icon -F PyBots.py"
        system(command)
        print("\n your executable file is in /dist/ directory \n")
    elif output == "2" or output == "linux" or output == "2.linux":
        command = "pyinstaller --noconsole --clean -i icon.icon -F PyBots.py"
        system(command)
        print("\n your executable file is in /dist/ directory \n")
    else:
        print("please enter a valid number!!!")
