import re
import operator


def count_per_user(file):
	per_user = {}

	with open(file, encoding = 'UTF-8') as errfile :
		
		pattern = r"ticky: ERROR +([\w\s']*)+\(([\w.]*)\)"
		for line in errfile.readlines() :
			var = re.search(pattern, line)
			#print(var)
			if var != None :
				#print(var[2])
				if var[2] not in per_user :
					per_user[var[2]] = 0
				per_user[var[2]] += 1
		#print(per_user)
		
	with open(file) as errfile :

		search_pattern = r"ticky: INFO +[\w\s']*\[#\d{4}\]\s+\(([\w.]*)\)"
		for line in errfile.readlines() :
			temp = re.search(search_pattern, line)
			#print(temp)
			if temp != None :
				#print(temp[1])
				if temp[1] not in per_user:
					per_user[temp[1]] = 0
				per_user[temp[1]] += 1
	print('\n')
	print(sorted(per_user.items(), key = operator.itemgetter(0)))

def count_error(file) :
	error = {}

	with open(file) as errfile :
		pattern = r"ticky: ERROR +([\w\s']*)"
		for line in errfile.readlines() :
			var = re.search(pattern, line)
			#print(var)
			if var != None :
				#print(var[1])
				if var[1] not in error :
					error[var[1]] = 0
				error[var[1]] += 1
	#print(error)
	tuples = sorted(error.items(), key=operator.itemgetter(1), reverse = True)
	print(tuples)


count_error('logfiles.txt')
count_per_user('logfiles.txt')

!/usr/bin/env python3


