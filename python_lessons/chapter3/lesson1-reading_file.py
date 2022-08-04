''' we will read directly from sketch.txt line by line by using its relative path
end='' appends space instead of newline'''


data = open('python_lessons\chapter3\sketch.txt') #assign file to var called data
# print(data.readline(), end='') #use readline to grav a line from the file and then use print to print it to console
# print(data.readline(), end='') #reads in another line
# data.seek(0) #rewind back to the beinning of file


#use for loop to read the whole file
for each_line in data:
    print(each_line, end='')
data.close() #close file when done reading



