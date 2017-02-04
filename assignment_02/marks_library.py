import libxml2
import sys

'''
purpose
	return the course mark for student s
preconditions
	student is a list of the form:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
	assignments is a dictionary of the form:
		{mark_id:[points, percentage], ... }
'''
def compute_mark(student, assignments):
	courseMark = 0
	for mark in student[3]:
		assignment = assignments[mark[0]] #get assignment from ID
		courseMark += (float(mark[1]) / assignment[0]) * assignment[1]	
	return courseMark
	
'''
purpose
	extract the information from a and return it as a list:
		[mark_id, points, percentage]
preconditions
	s is an assignment element from a legal students XML file
'''
def extract_assignment(a):
	assignment = [None, None, None] 
	while a is not None:
		if a.name == 'mark_id':
			assignment[0] = a.content
		if a.name == 'points':
			assignment[1] = int(a.content)
		if a.name == 'percentage':
			assignment[2] = float(a.content)
		a = a.next
	return assignment

'''
purpose
	extract the information from s and return it as a list:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [mark_id,score], ... ]
preconditions
	s is a student element from a legal students XML file
'''
def extract_student(s):
	student = [None, None, None, None]
	while s is not None: #iterate through students
		if s.name == 'last_name': student[0] = s.content
		if s.name == 'first_name': student[1] = s.content
		if s.name == 'student_id': student[2] = s.content
		if s.name == 'marks': #marks subtree
			marks = []
			m = s.children
			while m is not None:
				mark = [None, None]
				mAttr = m.children #mark attribute
				while mAttr is not None:
					if mAttr.name == 'mark_id': mark[0] = mAttr.content
					if mAttr.name == 'score': mark[1] = int(mAttr.content)
					mAttr = mAttr.next
				if None not in mark: marks.append(mark)
				m = m.next
			student[3] = marks
		s = s.next
	return student
