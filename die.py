from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    @staticmethod
    def x_labels(start, end):
        label_list = []
        for label in range(start, end + 1):
            label_list.append("\'" + label + "\'")

        return label_list
