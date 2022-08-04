''' Once nester module is in PyPI, once we modify it to contain different changes, we need to ensure it doesn't affect previous versions
1. we need to make that if user wants to use its new functionality they need to specify explicitly
2. output should be the same unless user calls it explicity
In our case, we want our new version to indent if there is nested lists for the updated version but this should be explicit '''

#a second arg called "level" is used to insert tab-stops when a nested list is encountered
def loop_list(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            loop_list(each_item, level+1) #keep track of how many level we have; loop through all and add number of tabs accordingly
        else:
            for tab_stop in range(level): #use the value of level to control how many tab_stops are used
                print("\t", end='') #display a tab character for each level of indentation
            print(each_item)



names = ["Kara", "Sara", ["Linda", "Kyle"], [["Josephina"]]]
loop_list(names)