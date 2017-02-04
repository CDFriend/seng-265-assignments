# test extract_assignments

import libxml2
import marks_library

# ***** load the assignments file

parse_tree = libxml2.parseFile('assignments.xml')
context = parse_tree.xpathNewContext()

root = parse_tree.getRootElement()
assignment = root.children

assignments = { }
while assignment is not None:
	if assignment.type == "element":
		child = assignment.children
		L = marks_library.extract_assignment(child)
		assignments[L[0]] = [ L[1], L[2] ]
	assignment = assignment.next

for a in assignments.keys():
	print a, assignments[a]
