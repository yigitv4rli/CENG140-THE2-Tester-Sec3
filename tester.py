import time
import os
import sys

wrong=0

compileF = "gcc -Wall -ansi -pedantic-errors the2.c -o the2"; 
compileFF = os.popen(compileF)
time.sleep(1)

def areSame(test, correct):
    if test == correct:
        return 1
    else:
        return 0

for inputNo in range(1,11):
    print "Progress: " + str(inputNo) + "/10 testcases"
    inputDir = "input/" + str(inputNo) + ".txt"

    run = "./the2 < input/" + str(inputNo) + ".txt"
    stream = os.popen(run)
    output = stream.read()

    outputDir = "output/"+ str(inputNo) + ".txt"
    
    f = open(outputDir,"r")
    correctOut = f.read()

    if areSame(output,correctOut) == 0:
        print "You failed at " + str(inputNo) + ". testcase"
        print "Correct Output:\n"+correctOut
        print "\nYour Output:\n"+output
        wrong+=1


print "You failed " + str(wrong) + " times on 10 testcases."