from sys import argv

script,filename = argv

txt = open (filename)

print "this is file %r:" % filename
print txt.read()

print "Type the filename again:"
filename2 = raw_input (">  ")

txt_again = open(filename2)

print txt_again.read()