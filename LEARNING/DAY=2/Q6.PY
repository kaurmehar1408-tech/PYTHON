 #Take a character as input and check if it's a vowel or consonant (assume lowercase input). 

char = input("Enter a character: ")
vowels = "aeiou"
if char.isalpha():
    if char in vowels:
        print(char,"is a vowel.")
    else:
        print(char ,"is a consonant.")
        