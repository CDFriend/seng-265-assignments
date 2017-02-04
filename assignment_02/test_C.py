# test extract_students

import libxml2
import marks_library

parse_tree = libxml2.parseFile('students.xml')
context = parse_tree.xpathNewContext()

root = parse_tree.getRootElement()
student = root.children
students = [ ]
while student is not None:
	if student.name == "student":
		child = student.children
		L = marks_library.extract_student(child)
		students.append(L)
	student = student.next

for a in students:
	print a
