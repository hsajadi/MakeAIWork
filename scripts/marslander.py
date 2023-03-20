#!/usr/bin/env python

class Marslander:

    def __init__(self, valDict):
        self.length = valDict['length']
        self.width = valDict['width']
        self.weight = valDict['weight']

    def __str__(self):
        return f"{self.length} x {self.width}"


def main():
    pass


if __name__ == main():
    main()

marslander = Marslander({"length": 6, "width": 1.56, "weight": 360})
print(marslander)
