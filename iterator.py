# nested_list = [[],3,2,
# 	['a', 'b', 'c'], [],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None],[1, [3,[1,2],[]],7],89, []
# ]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

# nested_list = [
# 	['a', [1,3,'asd'],'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None]
# ]

# nested_list = [ 1, [ 2, [ 3, [ 4, None ] ] ] ]

class IterListsToList:
    def __init__(self, outerlist):
        self.outerlist = outerlist
        self.item = []
        self.len_outerlist = len(outerlist)
        self.len_item = 0
        self.is_item = False
        self.ind_outerlist = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.is_item and self.ind_item == self.len_item:
            self.is_item = False
            self.ind_item = 0
            self.ind_outerlist += 1

# пропустить пустые внутренние листы
        if self.ind_outerlist != self.len_outerlist:
            if  not self.is_item and isinstance(self.outerlist[self.ind_outerlist], list)\
                and not len(self.outerlist[self.ind_outerlist]): 
                     self.is_item = False
                     self.ind_outerlist += 1

        if self.ind_outerlist == self.len_outerlist:
            raise StopIteration

        if  self.is_item:
            result = self.outerlist[self.ind_outerlist][self.ind_item]
            self.ind_item += 1
        else:
             if isinstance(self.outerlist[self.ind_outerlist], list): 
                 self.is_item = True
                 self.item = self.outerlist[self.ind_outerlist]
                 self.len_item = len(self.item)
                 self.ind_item = 0
                 result = self.outerlist[self.ind_outerlist][self.ind_item]
                 self.ind_item += 1
             else:
                 result = self.outerlist[self.ind_outerlist]
                 self.ind_outerlist += 1
            
        return result
            
if __name__ == '__main__':

    print(nested_list)
    for item in IterListsToList(nested_list):
        print(item)

    flat_list = [item for item in IterListsToList(nested_list)]
    print(flat_list)


# print(sum(nested_list, []))