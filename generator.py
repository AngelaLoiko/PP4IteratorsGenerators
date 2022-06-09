nested_list = [[],3,2,
	['a', 'b', 'c'], [],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],[1, [3,[1,2],[]],7],89, []
]

# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None]
# ]

# nested_list = [
# 	['a', [1,3,'asd'],'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None]
# ]

def gener_listfromlists(outerlist):
    for item in outerlist:
        if isinstance(item, list):
            for inner_item in gener_listfromlists(item):
                yield inner_item
        else:
            yield item


if __name__ == '__main__':

    for item in gener_listfromlists(nested_list):
        print(item)