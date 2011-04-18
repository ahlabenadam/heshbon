#!/usr/bin/python


import random


class MinMax:
    mmin=None
    mmax=None
    def __init__(self, mmin = -10, mmax = 10):
        MinMax.mmin = mmin
        MinMax.mmax = mmax
    
    def random(self):
        return random.randrange(self.mmin, self.mmax)
        
    def prinT(self):
        print "Minium {min}, maximum {max}".format(min=MinMax.mmin, max=MinMax.mmax)
# TODO
# Parse imported arguments
       

m1 = MinMax()
def func(R):
	print  R.random()


question="Enter the number: "
line=""
while line != "quit":
	x, y = m1.random(), m1.random()
	correct= x + y
	if y < 0:
		oper="-"
	else:
		oper = "+"

	y = abs(y)

	line=""

	while  True:
		query = "{0} {x} {oper} {y} = ".format(question, x=x, y=y, oper=oper)	
		line = raw_input(query)
		if line == str(correct) or line == "quit" :
			break

