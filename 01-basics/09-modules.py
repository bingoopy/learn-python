"""
Modules basic:
    - import
    - from ... import ...
    - module alias
    - __name__
"""

# module is a .py file

import math

from datetime import datetime, date

import random as rand

from datetime import datetime as dt

# __name__
# each module has __name__ varibale

# Check is main program
if __name__ == "__main__":
    print("This is main program.. not imported by others")
