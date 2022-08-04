''' if the file is deleted, it will cause an IO error
To prevent this we will use os module to determine whether a file exist'''

import os

if os.path.exists('python_lessons\chapter3\sketch.txt'):
    data = open('python_lessons\chapter3\sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1) 
            print(role, end='') 
            print(' said: ', end='') 
            print(line_spoken, end= '')
        except:
            pass 
    data.close()
else:
    print("The file is missing") 


