class Color:
    def __init__(self, text='', *attributes, to_normal_end=True):
        """
            attributes
        0 - normal
        1 - thumbnail
        4 - underline
        5 - flashing
        7 - inverted colors
        8 - invisible

            text color
        30 - black
        31 - red
        32 - green
        33 - yellow
        34 - blue
        35 - purple
        36 - light-blue
        37 - white

            background color
        40 - black
        41 - red
        42 - green
        43 - yellow
        44 - blue
        45 - purple
        46 - light-blue
        47 - white
        """
        if not all(map(lambda x: type(x) is int, attributes)):
            raise TypeError("attribute takes only 'int' arguments")
        elif not all(map(lambda x: x in [0, 1, 4, 5, 7, 8]+list(range(30, 38))+list(range(40, 48)), attributes)):
            raise ValueError("the values ​​of 'attribute' are not in the values ​​of the table")
        self.atr = '\x1b['+';'.join(sorted(map(str, attributes)))+'m'
        self.attributes = attributes
        self.text = text
        self.end = to_normal_end

    def __str__(self):
        return self.atr+str(self.text)+('\x1b[0m' if self.end else '')

    def no_end(self):
        return self.atr+str(self.text)

    def __add__(self, other):
        if type(other) is Color:
            return Color(self.no_end() + other.no_end + self.atr, *self.attributes, to_normal_end=self.end)
        return str(self) + other

    def __radd__(self, other):
        if type(other) is Color:
            return Color(other.no_end + self.no_end(), *self.attributes, to_normal_end=self.end)
        return other + str(self)
