# PYTHON LOGIC-BUILDING PRACTICE
# Organized collection of the questions in your original practice.py file.
#
# HOW TO USE THIS FILE:
# 1. Questions are grouped by topic and arranged from basics to strings/lists.
# 2. Every question starts with a comment explaining what to find.
# 3. Each solution is commented out so the whole file does not run every input
#    at once. To practise a question, uncomment its code block and run it.
# 4. Repeated attempts have been combined into one version.
# 5. A few obvious mistakes in the original attempts were corrected.
#
# NOTE: These are beginner practice solutions. Some use built-in functions
# where useful; loop-based approaches are used for most list/string questions.


# ============================================================
# SECTION 1: CONDITIONS AND BASIC LOGIC
# ============================================================

# Q1. Check whether a number is positive or non-positive.
# n = int(input("Enter a number: "))
# if n > 0:
#     print("Positive")
# else:
#     print("Zero or negative")


# Q2. Check whether a number is even or odd.
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Q3. Find the greatest number in a collection.
# numbers = [10, 20, 30, 40]
# greatest = numbers[0]
# for i in numbers:
#     if i > greatest:
#         greatest = i
# print("Greatest:", greatest)


# Q4. Check whether a year has 365 days (simple exercise from original file).
# Note: This checks the number entered, not whether a calendar year is a leap year.
# days = int(input("Enter number of days: "))
# if days == 365:
#     print("365 days")
# else:
#     print("Not 365 days")


# Q5. Check divisibility by 5 or 11.
# n = int(input("Enter a number: "))
# if n % 5 == 0:
#     print("Divisible by 5")
# elif n % 11 == 0:
#     print("Divisible by 11")
# else:
#     print("Not divisible by 5 or 11")


# Q6. Check whether a single character is a vowel or not.
# ch = input("Enter one character: ")
# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
#     print("Not a vowel")


# Q7. Identify whether a single character is a lowercase letter, uppercase
# letter, digit, or special character.
# ch = input("Enter one character: ")
# if "a" <= ch <= "z":
#     print("Lowercase letter")
# elif "A" <= ch <= "Z":
#     print("Uppercase letter")
# elif "0" <= ch <= "9":
#     print("Digit")
# else:
#     print("Special character or other character")


# Q8. Make a simple calculator for +, -, *, /, and %.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# operator = input("Enter operator (+, -, *, /, %): ")
# if operator == "+":
#     print(a + b)
# elif operator == "-":
#     print(a - b)
# elif operator == "*":
#     print(a * b)
# elif operator == "/":
#     if b != 0:
#         print(a / b)
#     else:
#         print("Cannot divide by zero")
# elif operator == "%":
#     if b != 0:
#         print(a % b)
#     else:
#         print("Cannot use modulo with zero")
# else:
#     print("Invalid operator")


# ============================================================
# SECTION 2: FOR-LOOP BASICS
# ============================================================

# Q9. Print numbers from 1 to N.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     print(i)


# Q10. Print even numbers from 1 to N.
# n = int(input("Enter N: "))
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i)


# Q11. Find the sum of numbers from 1 to N.
# n = int(input("Enter N: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum:", total)


# Q12. Print the next 10 numbers starting from a given number.
# n = int(input("Enter starting number: "))
# for i in range(n, n + 10):
#     print(i)


# ============================================================
# SECTION 3: STRING LOGIC
# ============================================================

# Q13. Count vowels in a string without using string methods.
# s = input("Enter a string: ")
# vowels = 0
# for ch in s:
#     if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"
#             or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"):
#         vowels += 1
# print("Vowels:", vowels)


# Q14. Reverse a string without slicing.
# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# print("Reversed:", rev)


# Q15. Check whether a string is a palindrome.
# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# Q16. Count the frequency of each character in a string.
# s = input("Enter a string: ")
# visited = ""
# for ch in s:
#     if ch not in visited:
#         count = 0
#         for other in s:
#             if ch == other:
#                 count += 1
#         print(ch, "=", count)
#         visited += ch


# Q17. Remove spaces from a string.
# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch != " ":
#         result += ch
# print("Without spaces:", result)


# Q18. Remove every occurrence of a chosen character from a string.
# s = input("Enter a string: ")
# remove_char = input("Character to remove: ")
# result = ""
# for ch in s:
#     if ch != remove_char:
#         result += ch
# print("Result:", result)


# Q19. Find the first non-repeating character in a string.
# s = input("Enter a string: ")
# found = False
# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1
#     if count == 1:
#         print("First non-repeating character:", s[i])
#         found = True
#         break
# if not found:
#     print("No non-repeating character")


# Q20. Count vowels and consonants (ignore spaces, digits, and symbols).
# s = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         vowels += 1
#     elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
#         consonants += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants)


# ============================================================
# SECTION 4: LIST BASICS
# ============================================================

# Q21. Find the largest and smallest elements in a list.
# numbers = [10, 4, 25, 7, 2]
# largest = numbers[0]
# smallest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print("Largest:", largest)
# print("Smallest:", smallest)


# Q22. Find the sum of all elements in a list.
# numbers = [10, 20, 30]
# total = 0
# for i in numbers:
#     total += i
# print("Sum:", total)


# Q23. Count even and odd elements in a list.
# numbers = [1, 2, 3, 4, 5, 6]
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("Even:", even)
# print("Odd:", odd)


# Q24. Find the second-largest DISTINCT element in a list.
# numbers = [10, 20, 20, 15]
# largest = numbers[0]
# second = None
# for i in numbers:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i != largest and (second is None or i > second):
#         second = i
# print("Second largest distinct element:", second)
# If there are fewer than two distinct values, second remains None.


# Q25. Reverse a list in place without reverse() or slicing.
# numbers = [10, 20, 30, 40, 50]
# n = len(numbers)
# for i in range(n // 2):
#     temp = numbers[i]
#     numbers[i] = numbers[n - 1 - i]
#     numbers[n - 1 - i] = temp
# print("Reversed list:", numbers)


# Q26. Print each duplicate element only once.
# numbers = [1, 2, 3, 2, 4, 3]
# visited = []
# for i in numbers:
#     if i not in visited:
#         count = 0
#         for j in numbers:
#             if i == j:
#                 count += 1
#         if count > 1:
#             print("Duplicate:", i)
#         visited.append(i)


# Q27. Remove duplicates while preserving original order.
# numbers = [1, 2, 3, 2, 4, 3]
# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print("Unique elements:", unique)


# Q28. Find the frequency of each element in a list.
# numbers = [1, 2, 2, 3, 3, 4, 5, 5, 5]
# visited = []
# for i in numbers:
#     if i not in visited:
#         count = 0
#         for j in numbers:
#             if i == j:
#                 count += 1
#         print(i, "=", count)
#         visited.append(i)


# Q29. Find common unique elements between two lists.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# common = []
# for i in a:
#     if i in b and i not in common:
#         common.append(i)
# print("Common elements:", common)


# Q30. Move all zeros to the end while preserving the order of non-zero items.
# numbers = [0, 1, 0, 3, 12]
# result = []
# zero_count = 0
# for i in numbers:
#     if i == 0:
#         zero_count += 1
#     else:
#         result.append(i)
# for i in range(zero_count):
#     result.append(0)
# print(result)


# ============================================================
# END OF ORGANIZED PRACTICE FILE
# ============================================================
