nested_list = [
	['a', 'b', 'c', [1,75, [23, True]]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
class IteratorListsToList:
    def __init__(self, some_list):
        # self.new_list = sum(some_list)
        self.new_list = some_list
        pass
    
    def __iter__(self):
        self.lenlist = len(self.new_list)
        self.key = 0
        return self
    
    def __next__(self):
        if self.key == self.lenlist:
            raise StopIteration
        else:
            self.key += 1
            return self.new_list[self.key]
            
        


print(sum(nested_list, []))
