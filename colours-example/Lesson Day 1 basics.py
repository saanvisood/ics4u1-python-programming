#####File Pointers / File Data Types
####filepointer = open("helloWorld.txt", "r")
####print(filepointer)
####print(type(filepointer))
####
####filepointer.close()
####
####
#####Read and print every line
####file_in = open("helloWorld.txt", "r")
####
####for line in file_in:
####    print(line)
####
####file_in.close()
####
####
####
#####Read and print a selection of lines
####file_in = open("helloWorld.txt", "r")
####
#####skip first three lines
####for i in range(0, 3):
####    file_in.readline()  #read and ignore the line
####
#####read and print the next five lines
####for i in range(0, 5):
####    line = file_in.readline()
####    print(line)
####
####file_in.close()
####
####
#####Using the with block to open and close
####with open("helloWorld.txt", "r") as file_in:
####
####    for line in file_in:
####        print(line[0:5])
####        
####
#####no need to call file_in.close()
##
##
##
##
###Count how many times "hello world" appears in file
##with open("helloWorld.txt") as file_in:
##
##    counter = 0
##
##    for line in file_in:
##        counter += line.count("hello world")
##
##print(f'hello world appears {counter} times in the file')
