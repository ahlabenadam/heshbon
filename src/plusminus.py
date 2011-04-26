#!/usr/bin/python


import minmax
import random


#class MinMax:
#    mmin=None
#    mmax=None
#    def __init__(self, mmin = -10, mmax = 10):
#        MinMax.mmin = mmin
#        MinMax.mmax = mmax
#    
#    def random(self):
#        return random.randrange(self.mmin, self.mmax)
#        
#    def prinT(self):
#        print "Minium {min}, maximum {max}".format(min=MinMax.mmin, max=MinMax.mmax)
        
# TODO
# Parse imported arguments
       

m1 = minmax.minmax()

math_action = ('+', '-', '*', '/')

question="Enter the number: "
line=""

while line != "quit":
	x = m1.random()
	y = m1.random()

	action=math_action[random.randrange(0,4)]
	if action == '+':
		correct = x + y
		oper = "+"
	elif action == '*':
		correct = x * y
		oper = "*"
	elif action == '-':
		correct = x - y
		oper = "-"
	else:
		correct = x 
		x = correct * y
		oper = ":"

	line=""

	while  True:
		query = "{0} {x} {oper} {y} = ".format(question, x=x, y=y, oper=oper)	
		line = raw_input(query)
		if line == str(correct) or line == "quit" :
			break

