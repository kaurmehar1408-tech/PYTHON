# Q-1 Create a string "Python is fun" and print its length.
# SOLUTION =
# str="Python Is Fun"
# print(len(str))

# Q-2 Access the first, middle, and last character of "Harmehar".
# SOLUTION =
# name = "Harmehar"
# print(name[0])
# print(name[3])
# print(name[7])

# Q-3 Slice "programming" to get "pro" and "gram".
# SOLUTION=
# str = "programming"
# print(str[0:3])
# print(str[3:7])

# Q-4 Reverse "Python" using slicing.
# SOLUTION = 
# string = "python"
# print(string[-1:-7])

# Q-5 Concatenate "Hello" and "World" with a space.
# SOLUTION = 
# st1 = "Hello"
# st2 = "World"
# stfinal = st1 + " " + st2
# print(stfinal)

# Q-6 Count how many times "a" appears in "banana".
# SOLUTION =
# st = "banana"
# print(st.count("a"))

# Q-7 Replace "Java" with "Python" in "I love Java".
# SOLUTION =
# str1 = " I Love Java "
# print(str1.replace("Java" , "Python"))

# Q-8 Convert " hello world " into uppercase and strip spaces.
# SOLUTION =
# s1 = " hello world"
# print(s1.upper())

# Q-9 Split "apple,banana,grapes" into a list.
# SOLUTION =
# list = " apple , banana , grapes"
# print(list.split(","))

# Q-10 Join ["2025","09","05"] into "2025-09-05".
# SOLUTION =
# print("-".join(["2025","09","05"]))

# ✅ Q11. Check if a string is a palindrome

# 👉 What is a Palindrome?
# A string that reads the same forwards and backwards, e.g., "madam", "level".
# s = "madam"
# if s == s[::-1]:
#     print(s, "is a palindrome")
# else:
#     print(s, "is not a palindrome")
# 🔍 Explanation:
# s[::-1] → This is Python’s slicing method to reverse a string.
# Example:
# "madam"[::-1] → "madam"
# Then we check if the reversed string is equal to the original string.
# If yes → Palindrome, else → Not a palindrome.

# ✅ Q12. Count the number of vowels in "Education"
# s = "Education"
# vowels = "aeiouAEIOU"
# count = 0
# for ch in s:
#     if ch in vowels:
#         count += 1
# print("Number of vowels:", count)

# 🔍 Explanation:
# We define the vowels string: "aeiouAEIOU" (lowercase + uppercase).
# Loop over each character in the string s.
# Check if the character is in the vowels string.
# If yes → increment the count by 1.
# Finally, print the total vowel count.

# ✅ Q13. Find the longest word in a sentence
# sentence = "I love learning Python programming"
# words = sentence.split()
# longest = max(words, key=len)
# print("Longest word is:", longest)

# 🔍 Explanation:
# sentence.split() → splits the sentence into a list of words:
# ['I', 'love', 'learning', 'Python', 'programming']
# max(words, key=len) → Finds the word with maximum length.
# We print the longest word.

# ✅ Q14. Check if two strings are anagrams
# ✅ Code:
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("They are anagrams")
# else:
#     print("Not anagrams")

# 🔍 Explanation:
# Anagrams → Same letters, different order.
# sorted(str1) → Sorts letters of the string alphabetically → returns a list of letters in order.

# Example:
# sorted("listen") → ['e', 'i', 'l', 'n', 's', 't']  
# sorted("silent") → ['e', 'i', 'l', 'n', 's', 't']
# If the sorted lists match → Anagrams.

# ✅ Q15. Reverse the order of words in a sentence
# sentence = "I am learning Python"
# words = sentence.split()
# reversed_sentence = " ".join(words[::-1])
# print("Reversed:", reversed_sentence)

# 🔍 Explanation:
# sentence.split() → splits the sentence into words:
# ['I', 'am', 'learning', 'Python']
# words[::-1] → Reverses the list:
# ['Python', 'learning', 'am', 'I']
# " ".join(...) → Joins the words back into a string with spaces.
# Final result:
# "Python learning am I"