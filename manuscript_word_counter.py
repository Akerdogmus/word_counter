#!/usr/bin/python
fname = input("Enter file name: ")
#fname ="/home/ros/manuscript.txt" 
num_words = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
