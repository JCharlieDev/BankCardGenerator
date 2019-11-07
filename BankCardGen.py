#! /usr/bin/python
#
#
#	BankCardGen


#	Libaries
from decimal import *
import random
import os

#	Static variables (t and c may change)
t = 6
a = 209
c = 8388608

#	Generates random numbers using "Metodo congruencial multiplicativo"
def FourthBatch(seed):

	#	Sets the value Xn of the formula.
	xn = seed
	#	Empty strings that stores the first four digits.
	fourDigs = ""

	#	Integer to string.
	digs = str(seed)
	#	Indexing the last digit.
	index = int(digs[3])

	#	Iterating in the formula.
	for i in range(0, 7):

		xi = ((a * xn)%c)
		xn = xi		

	#	numbres to string
	newDigs = str(xn)

	#	Creating a new string of just the 1st four digits.
	for j in range(0, 4):

		fourDigs += newDigs[j]

	#	Converting string digits to int
	finalDigs = int(fourDigs)

	#	Returning four digits
	return finalDigs

#	Generates random numbers using "Metodo congruencial multiplicativo"
def ThirdBatch(seed):

	#	Sets the value Xn of the formula.
	xn = seed
	#	Empty strings that stores the second four digits.
	fourDigs = ""

	#	Integer to string.
	digs = str(seed)
	#	Indexing the second digit.
	index = int(digs[1])

	#	Iterating in the formula.
	for i in range(0, 7):

		xi = ((a * xn)%c)
		xn = xi		

	#	numbres to string
	newDigs = str(xn)

	#	Creating a new string of just the 1st four digits.
	for j in range(0, 4):

		fourDigs += newDigs[j]

	#	Converting string digits to int
	finalDigs = int(fourDigs)

	#	Returning four digits
	return finalDigs

#	Generates random numbers using "Metodo congruencial multiplicativo"
def SecondBatch(seed):

	#	Sets the value Xn of the formula.
	xn = seed
	#	Empty strings that stores the first four digits.
	fourDigs = ""

	#	Integer to string.
	digs = str(seed)
	#	Indexing the first digit.
	index = int(digs[0])

	#	Iterating in the formula.
	for i in range(0, index):

		xi = ((a * xn)%c)
		xn = xi		

	#	numbres to string
	newDigs = str(xn)

	#	Creating a new string of just the 1st four digits.
	for j in range(0, 4):

		fourDigs += newDigs[j]

	#	Converting string digits to int
	finalDigs = int(fourDigs)

	#	Returning four digits
	return finalDigs

#	Method that prints the numbers.
def GenerateRandom(seed):

	os.system('cls')
	return ("\nFelicidades!, su tarjeta Coppel es: \n\n" + 
		str(seed) + " " +
		 str(SecondBatch(seed)) + " " + 
		 str(ThirdBatch(SecondBatch(seed))) + " " + 
		 str(FourthBatch(ThirdBatch(SecondBatch(seed)))))

def GenerateCard():

	#	Condition that catches user input exception on the Screen Menu.
	while True:
		try:
			os.system('cls')
			n = int(input("Introduzca una semilla para generar tarjeta: "))
			
			break

		except:

			print ("\nIngrese un valor numerico...")

	#	Function recieves int user input to generate numbers.
	print (GenerateRandom(n))

#	Main Menu that executes all of the above.
def MainMenu():

	#	Condition that catches user input exception on the Screen Menu.
	while True:
		try:

			z = int(input("\n====== Menu ======\n\n1) Generar Tarjeta\n\n2) Salir\n\n"))
			
			if (z == 1):

				#	If true, call GenerateCard() method.
				GenerateCard()

			else:

				os.system("cls")
				break

		except:

			print ("\nIngrese un numero...")

#	Main
def main():

	#	Main Menu call (Screen Menu).
	MainMenu()

if __name__ == "__main__": main()