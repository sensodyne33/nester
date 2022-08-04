''' We make indentation false by default in case old users don't want it '''


def loop_list(the_list, level=0, indent=False):
    for each_item in the_list:
        if isinstance(each_item, list):
            loop_list(each_item, level+1, indent) 
        else:
            if indent==True: #only add tabs to level if user specifically sets indent to true; else we simply print the list
                for tab_stop in range(level): 
                    print("\t", end='') 
            print(each_item)



names = ["Kara", "Sara", ["Linda", "Kyle"], [["Josephina"]]]
loop_list(names, indent=True)