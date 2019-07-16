class ChangedStock:
    def __init__(self, val1, val2, val3, val4, val5):
        self.date = val1
        self.code = val2
        self.name = val3
        self.oldUnit = val4
        self.newUnit = val5
    
    def __str__ (self):
        return self.date + ',' + self.code + ',' + self.name + ',' + self.oldUnit + ',' +self.newUnit
