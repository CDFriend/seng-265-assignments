import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.
	For each log file
		write to standard output the course mark for the log file,
		in CSV format
preconditions
	Each command-line argument is the name of a legal, readable quiz log file.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

target_files = sys.argv[1:] #target file names

# sum quiz marks and print to stdout
for quizFile in target_files:
	quiz_log = quiz_library.load_quiz_log(quizFile)
	mark_list = quiz_library.compute_mark_list(quiz_log)
	quiz_total = reduce(lambda x, y: x + y, mark_list)
	print  quizFile + "," + str(quiz_total)
