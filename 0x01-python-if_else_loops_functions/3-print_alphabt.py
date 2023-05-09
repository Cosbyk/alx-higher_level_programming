#!/usr/bin/python3
for letter in range(97, 121+2):
    if chr(letter) not in ["q", "e"]:
        print("{}".format(chr(letter)), end="")
