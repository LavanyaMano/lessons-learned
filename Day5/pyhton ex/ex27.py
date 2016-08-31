def find_needle(haystack):
    # your code here
    for i in haystack:
        if i == "needle":
            print "Found the needle at position",haystack.index(i)


         

def stringy(size):
    # Good Luck!
    str=""
    for i in range (1,size):
        if i%2==0:
            str+="0"
        else:
            str+="1"
    print str


def summation(num):
    pass # Code here
    a=0
    for i in range(1,num+1):
        a=a+i
    print a



print "this is a bell \f formfeed \f again \r carriage \r where?"

print "this is a rewritten here \r with this"

print "with vertical tab \v lets see \v aaa"

