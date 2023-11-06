class SearchableArray:
    def __init__(self):
        self.numbers = []
    
    def insert(self, number):
        self.numbers.append(number)

    def search(self, number):
        for i in range(len(self.numbers)):
            if self.numbers[i] == number:
                return i + 1
        return -1

