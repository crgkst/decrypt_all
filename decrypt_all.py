#this script solves encryptions from https://www.trytodecrypt.com/decrypt.php
#currently it can solve for levels 1-9, after that its method of solving doesn't really work any more
#this is solved for in decrypt_v2 which is not planned for release until it's limits are surpassed

#running this takes a fair bit of alt+tab, copy, paste and entering
#but it works, and solves for 1-9

#created: OCT 10 2022 

#imports
import pyperclip

#declare variables
alphabet = ""
alphabet_codes = []
letters = ""
answer = ""


#for all the available characters get their encryption codes
pyperclip.copy(".,?-_:!0123456789abcdefghijklmnopqrstuvwxyz")
alphabet = alphabet + input("Enter '.,?-_:!0123456789abcdefghijklmnopqrstuvwxyz' code: ")
pyperclip.copy("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
alphabet = alphabet + input("Enter 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ' code: ")

#get if the codes get reversed when entered
r = input("alphabet is reversed? (y/n): ")
#set the string of letters we just captured
if r == "y":
    letters = "zyxwvutsrqponmlkjihgfedcba9876543210!:_-?,. ZYXWVUTSRQPONMLKJIHGFEDCBA"
else:
    letters = ".,?-_:!0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

#get the length of each character
ln = int(len(alphabet)) / int(len(letters))
ln = int(ln)

#turn the alphabet string into an array of codes
alphabet_codes = [alphabet[i:i+ln] for i in range(0, len(alphabet), ln)]
#print("alphabet codes: ", alphabet_codes)

#split up letters into their own array
n = 1
letters_arr = [letters[i:i+n] for i in range(0, len(letters), n)]

#create a dictionary mapping codes to their associated letter
combined = dict(zip(alphabet_codes,letters_arr))
#print("dictionary: ", combined)

lookup = input("Enter the lookup code: ")

#print("lookup array: ", lookup_arr)

for i in lookup_arr:
    if i in combined:
        answer = answer + combined[i]

if r == "y":
    answer = answer[::-1]

pyperclip.copy(answer)
print(answer)
