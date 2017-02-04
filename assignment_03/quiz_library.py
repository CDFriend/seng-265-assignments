import libxml2
import sys

'''
purpose
	store the information from an answer element
'''
class Answer:
	def __init__(self, index, path, result, answer, time):
		self.index = index
		self.path = path
		self.result = result
		self.answer = answer
		self.time = time

'''
purpose
	Store the information from a display element.
'''
class Display:
	def __init__(self, index, path, time):
		self.index = index
		self.path = path
		self.time = time

'''
purpose
	Extract the information from log_file and return it as a list
	of answer and display objects.
preconditions
	log_file is the name of a legal, readable quiz log XML file
'''
def load_quiz_log(log_file):
	# load xml file
	parse_tree = libxml2.parseFile(log_file)
	context = parse_tree.xpathNewContext(); #new context
	root = parse_tree.getRootElement();

	# extract elements
	quiz_elements = []
	ele = root.children
	while ele is not None:
		child = ele.children
		index, path, result, answer, time = None, None, None, None, None

		# answer element
		if ele.name == "answer":
			while child is not None:
				if child.name == "index": index = int(child.content)
				if child.name == "path": path = child.content
				if child.name == "result" and child.content.isdigit():
					result = int(child.content)
				if child.name == "answer" and child.content is not '': 
					answer = child.content
				if child.name == "time" and child.content.isdigit():
					time = int(child.content)
				child = child.next
			ans = Answer(index, path, result, answer, time)
			quiz_elements.append(ans)
		
		# display element
		if ele.name == "display":
			while child is not None:
				if child.name == "index": index = int(child.content)
				if child.name == "path": path = child.content
				if child.name == "time" and child.content.isdigit():
					time = int(child.content)
				child = child.next
			disp = Display(index, path, time)
			quiz_elements.append(disp)

		ele = ele.next
	return quiz_elements

'''
purpose
	Return the number of distinct questions in log_list.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_question_count(log_list):
	questions = [] #question indexes displayed and answered (unique)
	for ele in log_list:
		if ele.index not in questions:
			questions.append(ele.index)
		if isinstance(ele, Display):
			# break the loop at the first display element - all question
			# indexes will be encountered before this	
			break 
	return len(questions)

'''
purpose
	Extract the list of marks.
	For each index value, use the result from the last non-empty answer,
	or 0 if there are no non-empty results.
preconditions
	log_list was returned by load_quiz_log
'''
def compute_mark_list(log_list):
	marks_list = []
	log_iter = iter(log_list)
	# initialize n null elements in the marks list
	while not isinstance(next(log_iter), Display):
		marks_list.append(0)
	# remaining display and answer elements
	for ele in log_iter:
		if isinstance(ele, Answer):
			marks_list[ele.index] = ele.result
	return marks_list
