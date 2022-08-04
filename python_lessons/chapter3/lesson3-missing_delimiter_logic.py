''' lines that don't have colons will cause a problem since split func expects every line to contain 1 colon
so we have to find all lines that do not contain a colon and then do something about it'''


''' one way to fix this is to only print lines with colon; so here we fixing it by adding extra logic to prevent errors''''


data = open('python_lessons\chapter3\sketch.txt')

for each_line in data:
    if each_line.find(':') != -1: #number of colon in a line is not null, print the line
        (role, line_spoken) = each_line.split(':', 1) 
        print(role, end='') 
        print(' said: ', end='') 
        print(line_spoken, end= '') 
data.close() 


