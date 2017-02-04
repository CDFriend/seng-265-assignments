# test extract_students

import marks_library

students = [
	['l0', 'f0', 'id0', [['a0',60],['a1',10],['a2', 5]] ],
	['l1', 'f1', 'id1', [['a0',100],['a1',20],['a2', 10]] ]
]

assignments = {
	'a1': [20, 25.0],
	'a0': [100, 50.0],
	'a2': [10, 25.0]
}

for s in students:
	m = marks_library.compute_mark(s, assignments)
	print s[0], m
