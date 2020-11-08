import enum

class DisplayPeriod(enum.Enum):
    def __init__(self):
        self.DAY = 1
        self.WEEK = 2
        self.MONTH = 3
        self.YEAR = 4
        super().__init__(self)
