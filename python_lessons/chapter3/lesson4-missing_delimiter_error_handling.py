''' lines that don't have colons will cause a problem since split func expects every line to contain 1 colon
so we have to find all lines that do not contain a colon and then do something about it'''


''' another way to fix this is to handle the errors after by simply calling an event handler to see what went wrong first
try and except protect code from runtime errors
except: pass simply report the error without us needing to write some error code
basically if any error appears during the try block code, we simply pass that code and only print everything that works
This eliminates the need for extra logic!'''


data = open('python_lessons\chapter3\sketch.txt')

for each_line in data:
    #use try and catch to skip lines that doesn't have colons
    try:
        (role, line_spoken) = each_line.split(':', 1) 
        print(role, end='') 
        print(' said: ', end='') 
        print(line_spoken, end= '')
    except:
        pass 
data.close() 


