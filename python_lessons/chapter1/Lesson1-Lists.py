#Recursion is good for nested lists
#List is a collection of data; arrays on steroids
#isinstance() BIF checks whether an identifier refers to a data object of some specified type
#BIF - built-in-function


def loop_list(the_list):
    for each_item in the_list:
        #if each item is an instance of a list, call function loop_list
        if isinstance(each_item, list):
            loop_list(each_item)
        #else if each item is not a list, simply print each item
        else:
            print(each_item)


names = ["Kara", "Sara", ["Linda", "Kyle"], ["Josephina"]]
loop_list(names)