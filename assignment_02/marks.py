import libxml2
import sys
import marks_library

# ***** load the assignments file

# parse the XML file in argv[1] and load it into memory
parse_tree = libxml2.parseFile(sys.argv[1])

# create a context for tree traversal
context = parse_tree.xpathNewContext()

# get the root of the tree
root = parse_tree.getRootElement()

# iterate over children of root, storing result in assignment dictionary
assignment = root.children
assignments = { }
while assignment is not None:
	if assignment.name == "assignment":
		child = assignment.children
		L = marks_library.extract_assignment(child)
		assignments[L[0]] = [ L[1], L[2] ]
	assignment = assignment.next

# ***** load the students file

# parse the XML file in argv[2] and load it into memory
parse_tree = libxml2.parseFile(sys.argv[2])

# create a context for tree traversal
context = parse_tree.xpathNewContext()

root = parse_tree.getRootElement()
student = root.children
student_list = [ ]
while student is not None:
	if student.name == "student":
		child = student.children
		L = marks_library.extract_student(child)
		student_list.append(L)
	student = student.next

# ***** generate the output

for s in student_list:
	mark = marks_library.compute_mark(s, assignments)
	print s[0] + ',' + s[1] + ',' + s[2] + ',' + str(mark)
