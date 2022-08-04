''' This module provides one function called loop_list which prints lists that may or may
not be include nested lists'''

def loop_list(the_list):
    for each_item in the_list:
        #if each item is an instance of a list, call function loop_list
        if isinstance(each_item, list):
            loop_list(each_item)
        #else if each item is not a list, simply print each item
        else:
            print(each_item)
