#!/usr/bin/env python3

import sys

def main():
	i = len(sys.argv)

	if i == 2:
		matching = sys.argv[1]
		user_input = input("What was the parameter? ")
		if user_input == matching:
			print("Good job!")
		else:
			print("Nope, sorry...")
	else:
		print("none")

main()