#!/usr/bin/python
# Spit.py
# This tool generates human looking typing (including
#   mistakes. It is based on Andrew Morris' talk on
#   threat intelligence where he was able to deduce
#   that an attacker was a bot or not based on if they
#   used backspaces.
#
# Example usage with a Parimiko SSH client:
# 1) create a SSH client (shell.py) that opens a chan and reads from stdin
# while True:
#       d = sys.stdin.read(1)
#       chan.send(d)
# 2) ./spit.py commandinput | ./shell.py
#  NOTE:
#  This was written on the plane from SFO to PHL for
#  no other reason than curing boredom.


import sys
import random
import time

BS = "BS"  # \x08 is backspace but this is used for testing

def main(lines=None):
    if not lines:
      try:
        f = open(sys.argv[1])
        lines = f.readlines()
      except:
        print("File not found. Choose a file with commands in it separated by newlines")
        sys.exit()

    for line in lines:
        spit(line)


def spit(line):
    """Main function that randomly
    chooses how to muck up the typing
    and send it to stdout"""
    rlen = random.randint(1,3)
    #for chunk in chunklineing(line, rlen):
    #print(chunk)
    human = random.randint(0,6)
    if human == 1:
        line = add_balls(line)
    elif human == 2:
        line = add_backspace(line)
    elif human == 3:
        line = add_confusion(line)
    elif human == 4:
        line = add_smack(line)
    elif human == 5:
        line = add_cr(line)
    elif human == 6:
        line = add_typo(line)
    elif human == 7:
        line = add_fat(line)

    for l in line:
            typing(l)
    sys.stdout.write("\r\n")

def typing(line):
    if " " in line:
       mult = random.randint(1,4)
    else:
       mult = random.randint(1,50)
    time.sleep(random.random()/mult)
    sys.stdout.write(line)

def add_typo(line):
    """Add a deliberate typo by switching the
    last two chars of a random word"""
    words = line.split()
    newline = []
    randword = random.randint(0,len(words))
    for word in words:
        if words.index(word) == randword:
            word = word.replace(word[-2:],word[-1]+word[-2]+BS*2)
        newline.append(word+" ")
    return "".join(newline)

def add_fat(line):
    """Takes a line and replaces a character of
    one random word with a fat fingered alternative"""
    words = line.split()
    sofat = {"a":"as",
            "b": "bn",
            "c": "cv",
            "d": "sd",
            "e": "ed",
            "f": "fg",
            "g": "gf",
            "h": "hj",
            "i": "ik",
            "j": "jk",
            "k": "kl",
            "l": "l;",
            "m": "mn",
            "n": "nm",
            "o": "ol",
            "p": "p;",
            "q": "1q",
            "r": "rf",
            "s": "sa",
            "t": "tf",
            "u": "yu",
            "v": "cv",
            "w": "wq",
            "x": "xz",
            "y": "yu",
            "z": "zx"
    }
    newline = []
    randword = random.randint(0,len(words))
    for word in words:
        if words.index(word) == randword:
            randle = random.randint(0, len(word))
            for l in word:
                if word.index(l) == randle:
                    word = word.replace(l,sofat[l])
        newline.append(word+" ")
    return "".join(newline)

def add_cr(line):
    """Add frustrated carriage returns to a line"""
    return line + "\n\n\n\n\n\n\n\n\n"

def add_smack(line):
    """Add frustrated keyboard smacking to a line"""
    return line + "fjda;lsjfk;asdljfl;ksadlj;kfsdajlkf;sadjfl;k"

def add_balls(line):
    """Add the word 'balls' to a line"""
    return line + "BALLS"

def add_confusion(line):
    """Sleep while the person typinging
    is thinking about what they should type"""
    time.sleep(4)
    return(line)

def add_backspace(line):
    """Add backspaces that fix typos to a line"""
    #BS = "\x08"
    BS = "BS" # debug
    clear = BS*(len(line))
    return line + clear + line + clear

def chunklineing(lineing, length):
    """IDK what this is anymore. I think the guy next to me on the plane wrote it. """
    return (lineing[0+i:length+i] for i in range(0, len(lineing), length))

if __name__ == "__main__":
    demo = [
                "Hi Andrew. Hope you enjoy this yack shave\nSincerely, Dr. James Russle",
                "chmod +x ./something.py",
                "ls",
                "cat /tmp/balls"
                "why the fuck isnt this working!!!",
                "cat /etc/passwd",
                ]
    if len(sys.argv) == 1:
        main(demo)
    else:
        main()
