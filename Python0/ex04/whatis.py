from sys import argv
from sys import exit
try:
    assert (len(argv) <= 2)
except AssertionError:
    print("AssertionError: more than one argument is provided")
    exit(1)
if len(argv) == 1:
    exit(0)
try:
    number = int(argv[1])
except Exception:
    print("AssertionError: argument is not an integer")
    exit(1)
if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
