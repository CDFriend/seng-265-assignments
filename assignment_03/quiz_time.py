import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

quiz_files = sys.argv[1:] #target files

# get question count
log_list1 = quiz_library.load_quiz_log(sys.argv[1])
num_questions = quiz_library.compute_question_count(log_list1)

sumDeltaT = [0] * num_questions #sum of delta t values for all questions across all quizzes

for quizFile in quiz_files:
	deltaT = [0] * num_questions #total screen time over current quiz
	tInit = 0 #initial time for current stopwatch
	
	# get index of first display element, set iterator
	iPrev = 0
	log_list = quiz_library.load_quiz_log(quizFile)
	log_list_iter = iter(log_list)
	while not isinstance(log_list_iter.next(), quiz_library.Display): 
		iPrev += 1 #previous element index
	
	# start first stopwatch (previous element = first Display element)
	swOnIndex = log_list[iPrev].index #active stopwatch index
	tInit = log_list[iPrev].time

	# iterate through log_list[i:] (quiz start-end)
	for ele in log_list_iter:
		if isinstance(ele, quiz_library.Display):
			# stop old stopwatch
			deltaT[swOnIndex] += ele.time - tInit
			
			# start new stopwatch
			swOnIndex = ele.index
			tInit = ele.time

	# last element
	last_ele = log_list[len(log_list) - 1]
	
	# Case: last element is an Answer
	if isinstance(last_ele, quiz_library.Answer):
		lDispIndex = len(log_list) - 2
		# get index of last display element
		while not isinstance(log_list[lDispIndex], quiz_library.Display):
			lDispIndex -= 1
		# add screen time to last answer (approximation, no data on quiz close time)
		deltaT[swOnIndex] += last_ele.time - log_list[lDispIndex].time
	
	# If no answer is provided, assume additional screen time is 0.

	# add question times to sumDeltaT
	for i in range(len(deltaT)):
		sumDeltaT[i] += deltaT[i]

# calculate average screen times
avgTimes = map(lambda x: float(x) / len(quiz_files), sumDeltaT)
		
# print avgTimes as CSV
strOut = ''
for n in avgTimes:
	strOut = strOut + str(n) + ','
print strOut[:-1] #remove last comma from output
