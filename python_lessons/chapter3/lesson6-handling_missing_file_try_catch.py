''' if the file is deleted, it will cause an IO error
To prevent this we will we can also use another try-except handler'''

try:
    data = open('python_lessons\chapter3\sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1) 
            print(role, end='') 
            print(' said: ', end='') 
            print(line_spoken, end= '')
        except ValueError: #be more specific with what type of error it takes in
            pass 
    data.close()
except IOError:
    print("The file is missing") 


