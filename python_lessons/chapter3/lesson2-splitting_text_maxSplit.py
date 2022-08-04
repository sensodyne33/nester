''' we want to split role and the lines; to do that we use split function
role and lines are separated by : which is our indicator for how to split the text'''


data = open('python_lessons\chapter3\sketch.txt')

for each_line in data:
    (role, line_spoken) = each_line.split(':', 1) #store the split after the colon in role and line_spoken respectively; only split 1 colon even if multiple colons in one line
    # help(each_line.split)  see what BIF split has to help us with multiple colons read in but not enough vars to store the multiple split
    print(role, end='') #print name of role
    print(' said: ', end='') #add a the "role said...."
    print(line_spoken, end= '') #print the role's line as usual
data.close() 


