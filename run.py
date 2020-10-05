#!/usr/bin/python3

from os import system
from time import sleep


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
    command = "pyarmor obfuscate PyBots.py"
    system(command)
    command = "cd dist"
    system(command)
    command = "pyinstaller --noconsole -i icon.svg -F PyBots.py"
    system(command)
    print("\n your executable file is on /dist/ directory \n")
