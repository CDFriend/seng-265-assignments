import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.
preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

# check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

quiz_logs = sys.argv[1:] # target file names

# create list for each question index
log1 = quiz_library.load_quiz_log(sys.argv[1]) #log for question 1
mark_passes = quiz_library.compute_mark_list(log1) #total passes for each question index

# Case: more than one log file
if len(sys.argv) > 2:
	for quiz in sys.argv[2:]:
		quiz_log = quiz_library.load_quiz_log(quiz)
		quiz_marks = quiz_library.compute_mark_list(quiz_log)
		new_passes = []
		passes_iter = iter(quiz_marks)
		for mark in mark_passes:
			new_passes.append(mark + passes_iter.next()) #add quiz results to passes element-wise
		mark_passes = new_passes #replace mark_passes with sum

# calculate pass ratios for each question		
pass_ratios = map(lambda x: float(x) / len(quiz_logs), mark_passes)

# print CSV
strOut = ""
for n in pass_ratios:
	strOut = strOut + str(n) + ','
print strOut[:-1] #remove last comma from output
