MyStuff_dic = {'apple': "I am APPLES!"}
print(MyStuff_dic['apple'])

import ex40_mystuff_module as mystuff_module
mystuff_module.apple()

class MyStuff_class(object):

    def __init__(self):
        self.tangerine = "And Now a thousand year between"

    def apple(self):
        print("I am classy apples!")

thing = MyStuff_class()
thing.apple()
print(thing.tangerine)
