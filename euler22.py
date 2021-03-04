import os
import sys
import ast 
file = open("names.txt", "r")
contents = file.read()
name_lst = ast.literal_eval(contents)
name_lst = sorted(name_lst)
letter_lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def ab_value(name):
	value = 0
	for letter in name:
		value += letter_lst.index(letter)+1	
	return value
def name_score():
	name_sum = 0
	for i, name in enumerate(name_lst):
		name_sum += ab_value(name)*(i+1)
	return name_sum
print(name_score())