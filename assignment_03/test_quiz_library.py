import libxml2
import sys
import quiz_library

print '-------------------- test load_quiz_log'

log_list = quiz_library.load_quiz_log(sys.argv[1])

for x in log_list:
	if isinstance(x, quiz_library.Answer):
		print 'Answer:', x.index, x.path, x.result, x.answer, x.time
	else:
		print 'Display:', x.index, x.path, x.time

print '-------------------- test compute_question_count'

question_count = quiz_library.compute_question_count(log_list)
print question_count

print '-------------------- test compute_mark_list'

mark_list = quiz_library.compute_mark_list(log_list)
print mark_list
