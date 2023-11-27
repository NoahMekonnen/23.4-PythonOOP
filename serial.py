"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        self.seq = start

    def generate(self):
        """returns the next number based on the start value and number
        of generate calls made thus far"""
        self.seq += 1
        return self.seq - 1

    def reset(self):
        """resets the seq value to the start value"""
        self.seq = self.start








