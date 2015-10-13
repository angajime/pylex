#!/usr/bin/python

import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) != 2:
	print 'Hand over a file as a first argument.'
	sys.exit(2)

with open(sys.argv[1]) as f:
    content = f.readlines()

isRegex = True
regex_list = []
test_list = []

for line in content:
	line = line[:-1]
	if line == '%%':
		isRegex = False
	if isRegex:
		regex_list.append(line)
	else:
		test_list.append(line)
test_list.pop(0)


for regex in regex_list:
	for test in test_list:
		pattern = re.compile(regex)
		if pattern.match(test):
			print "{:<20} {:<10} {color} {:>5} {clear}".format(regex, test, '[PASS]', color=bcolors.OKGREEN, clear=bcolors.ENDC)
		else:
			print "{:<20} {:<10} {color} {:>5} {clear}".format(regex, test, '[FAIL]', color=bcolors.FAIL, clear=bcolors.ENDC)






