# modules can be considered as small code libraries that are based on related features like math module
# math module contains functions and constant values for use in mathematical equations
# built-in modules in python, but should be imported to use it
from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rps7 import rock_paper_scissors


print(pi)

# for item in dir(rdm):
#     print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

rock_paper_scissors()
