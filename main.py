# -*- encoding: utf-8 -*-
# Thoughtful’s robotic automation factory
### Rules

# Sort the packages using the following criteria:
#
# - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
# - A package is **heavy** when its mass is greater or equal to 20 kg.
#
# You must dispatch the packages in the following stacks:
#
# - **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
# - **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
# - **REJECTED**: packages that are **both** heavy and bulky are rejected.

# Implementing sort() function as sort(width, height, length, mass):


def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length

    # if heavy
    heavy = mass >= 20

    # if bulky
    bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150

    # Check the package stack
    if heavy or bulky:
        return 'Special Package'
    elif heavy and bulky:
        return 'Rejected Package'
    else:
        return 'Standard Package'

