format = "%r %r %r"

print format % (1, 2, 3)
print format % ("one", "two", "three")
print format % (True, False, True)
print format % (format,format,format)
print format % (
	"I had this thing.",
	"That you could type up right.",
	"Added three args"
	)