#! /usr/bin/python
#-*- coding:utf-8 -*-
#
#	Jose Carlos Muñoz Ramirez.
#	al15211330.AT.ite.DOT.edu.DOT.mx
#	Libraries.
from decimal import *
import random
import os


#	Generates pseudo-random numbers using "Multiplicative congruential method".
def CardGenerator(seed, a, m):

	#	xn it's a changing value of new seeds to determine the digits of the card.
	xn = seed

	#	strings in which the digits will be stored and converted to int.
	secondBatch = ""
	thirdBatch = ""
	fourthBatch = ""

	#	Variable that will be used to index iterations.
	digs = str(seed)

	#	Iterations used based on the seed parameter.
	firstIndex = int(digs[0])
	secondIndex = int(digs[1])
	fourthIndex = int(digs[3])

	#	Iteration to determine the pseudo-random numbers. 
	for i in range(0, firstIndex):

		xi = ((a * xn)%m)
		xn = xi	

	secondDigits = str(xn)

	#	Taking the 1st four numbers of the pseudo-random number.
	for j in range(0, 4):

		secondBatch += secondDigits[j]

	secondCardDigs = int(secondBatch)
	xn = secondCardDigs

	for i in range(0, secondIndex):

		xi = ((a * int(xn))%m)
		xn = xi

	thirdDigits = str(xn)

	for j in range(0, 4):

		thirdBatch += thirdDigits[j]

	thirdCardDigs = int(thirdBatch)
	xn = thirdCardDigs

	for i in range(0, fourthIndex):

		xi = ((a * xn)%m)
		xn = xi		

	fourthDigits = str(xn)

	for j in range(0, 4):

		fourthBatch += fourthDigits[j]

	fourthCardDigs = int(fourthBatch)

	#	Adding all the digits into one string.
	bankCard = (str(secondCardDigs) + " " + str(thirdCardDigs) + " " + str(fourthCardDigs))

	#	Returns the last 3 sets of digits of the card XXXX-XXXX-XXXX
	return bankCard

#	Method that generates and prints the bank card.
def CardParameters(seed, a, m):

	os.system('cls')
	return ("\nCongratulations!, your card is: \n\n" + 
		str(seed) + " " +
		 str(CardGenerator(seed, a, m)))

def GenerateCard():

	#	Condition that catches user input exception on the Screen Menu.
	while True:
		try:
			os.system('cls')
			n = int(input("Enter a seed to generate a card: "))
			os.system('cls')
			a = int(input("Set a value for a: "))
			os.system('cls')
			m = int(input("Set a value for m: "))
			break

		except:

			print ("\nEnter a numeric value...")

	#	Function recieves int user input to generate numbers.
	print (CardParameters(n, a, m))

#	Main Menu that executes all of the above.
def MainMenu():

	#	Condition that catches user input exception on the Screen Menu.
	while True:
		try:

			z = int(input("\n====== Menu ======\n\n1) Generate Card\n\n2) Exit\n\n"))
			
			if (z == 1):

				#	If true, call GenerateCard() method.
				GenerateCard()

			else:
				#	Clears screen
				os.system("cls")
				break

		except:

			print ("\nEnter a numeric value...")

#	Main
def main():

	#	Main Menu call (Screen Menu).
	MainMenu()

if __name__ == "__main__": main()