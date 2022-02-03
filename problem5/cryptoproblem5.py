# Hayden Olmstead
# 2/2/2022
# Applied Cryptography CS 4920
#
# problem 5
# This program is designed to be a program for the Caesar cipher

# The program is written in Python and utilizes numpy as a library to
# work with matrices easier
#
# I first read in the text from the file, scrub away the non-letters,
# perform the shifts necessary to encrypt the file, and then print to an
# output file
#
#
# #the main logic of the program can be found below the functions
# each problem on the homework sheet is divided into individual answers#

# function for encrypting a message
# this function only takes plain text, and the amount to be shifted by,
# gettingthe plaintext is another function
def encrypt(plaintext, s, filename):
    # go through each element in the plaintext and convert it to the
    # character that is s amount of spaces down
    ciphertext = ''
    for x in plaintext:
        cipherx = chr((ord(x) + s - 97) % 26 + 97)

        ciphertext = ciphertext + cipherx

    # print the plaintext to an output file
    with open(filename, 'w') as file_object:
        file_object.write(ciphertext)

# function for decrypting a message
# this function only takes ciphertext, then converts it to plain text, in
# an output file


def decrypt(ciphertext, s, filename):
    # go through each element and shift it by the amount specified in x
    plaintext = ''
    for element in ciphertext:

        plainx = chr((ord(element) - s - 97) % 26 + 97)

        plaintext = plaintext + plainx

    # print the output to an output file
    with open(filename, 'a') as file_object:
        file_object.write(plaintext)
        file_object.write("\n")


# getting the plaintext function
def getFilteredText(filename):
    # read the infomration from the file into a list
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()

    # scrub the content string to get rid of characters we wont use
    filteredplaintext = ''
    content = lines[1]
    for char in content:
        if((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
            filteredplaintext += char

    finalplaintext = filteredplaintext.lower()

    return finalplaintext

# function for getting the key needed


def getKey(filename):
    with open(filename) as file_object:
        content = file_object.read()

    intKey = ord(content[0]) - 97

    return intKey
# main logic of the program


# get file names
classEncInputFile = 'problem5/class_input_b.txt'
classEncOutputFile = 'problem5/class_output_b.txt'

myinputfile = 'problem5/my_plaintext.txt'
myoutputfile = 'problem5/my_ciphertext.txt'

classdecinputfile = 'problem5/class_input_c.txt'
classdecoutputfile = 'problem5/class_output_c.txt'

myinputdecfile = 'problem5/my_ciphertext.txt'
myoutputdecfile = 'problem5/myDecInputFile.txt'


# PROBLEM B ANSWER
# get the plaintext from the input file
classInputText = getFilteredText(classEncInputFile)

# run encryption on that text
encrypt(classInputText, getKey(classEncInputFile), classEncOutputFile)


# PROBLEM C ANSWER
# get the ciphertext from the file
decryptfileText = getFilteredText(classdecinputfile)

# run decryption on the text
decrypt(decryptfileText, getKey(classdecinputfile), classdecoutputfile)


# PROBLEM D ANSWER
# get the plaintext from the input file
myInputText = getFilteredText(myinputfile)

# run encryption on that text
encrypt(myInputText, getKey(myinputfile), myoutputfile)

# now run decryption on that output
decInputText = getFilteredText(myoutputdecfile)
decrypt(decInputText, getKey(myoutputdecfile), myoutputdecfile)
