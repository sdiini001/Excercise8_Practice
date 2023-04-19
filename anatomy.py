# import the sys module to give access to command line arguments
import sys
# find out how many arguments have been passed in
# and assign it to our own variable
# argv is an attribute of sys
# arg = argument count
argument_count = len(sys.argv)
# length of list of arguments passed through a parameter/vector
# if there is more than 1 argument passed in
# print "Too many args"
# otherwise print "Hello World"
if argument_count > 1:
    print("Too many args")
else:
    where = "World"
    print("Hello", where)
# print "Goodbye from " {}
# get me 0th argument in the vector
print("Goodbye from " + sys.argv[0])