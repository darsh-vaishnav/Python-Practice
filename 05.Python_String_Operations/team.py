#task 1
name = 'Darsh'
city = 'Kalol'
fav_language = "Python"
message = "I love coding!"

print("Name:", name)
print("City:", city)
print("Favorite Language:", fav_language)
print("Message:", message)

#task 2
empty_str = ""

print("String:", empty_str)
print("Length:", len(empty_str))
print("Data Type:", type(empty_str))

#task 3
text = "Python Programming"

print("Complete string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])

#task 4
text = "Programming"

print("String:", text)

print("First character:", text[0])
print("Second character:", text[1])
print("Fifth character:", text[4])
print("Last character:", text[10]) 

#task 5
text = "Programming"

print("String:", text)

print("Last character:", text[-1])
print("Second-last character:", text[-2])
print("Third-last character:", text[-3])
print("First character using negative index:", text[-11])

#task 6
full_name = "Darsh Vaishnav"

print("Full Name:", full_name)

print("First character:", full_name[0])
print("Last character:", full_name[-1])

space_index = full_name.index(" ")
print("First character of last name:", full_name[space_index + 1])

# task 7
text = "Python Programming"

print("Original String:", text)

print('"Python":', text[0:6])
print('"Programming":', text[7:18])
print('"Python Programming":', text[0:18]) 
print("First 5 characters:", text[0:5])
print("Last 5 characters:", text[-5:])

#task 8
text = "ABCDEFGHIJKL"

print("Original String:", text)

print("Every second character:", text[::2])
print("Every third character:", text[::3])
print("From index 1 to 8 with step 2:", text[1:8:2])
print("Reverse the string:", text[::-1])

#task 9
text = "Python Programming"

print("Original String:", text)

print("Last 5 characters:", text[-5:])
print("Last 10 characters:", text[-10:])
print("Characters from end with negative step (reverse):", text[::-1])
print("Last 5 characters reversed:", text[-1:-6:-1])

# task 10
text = "Python Programming"

print("Original String:", text)

print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Every second character:", text[::2])
print("String in reverse:", text[::-1])
print("Without first and last character:", text[1:-1])


message = "Hello Python"

print("Python" in message)
print("java" not in message)
print(message.find("java"))
print(message.index("Python"))


# Part 6 — Length

# Task 11
word = "Python"
sentence = "Python is easy"
sentence_spaces = "Python  is  easy"

print(len(word))
print(len(sentence))
print(len(sentence_spaces))


# Task 12
text = "Python Programming"

last_index = len(text) - 1
print(last_index)
print(text[last_index])


# Part 7 — Concatenation

# Task 13 — Full Name
first_name = "Darsh"
last_name = "Vaishnav"

full_name = first_name + " " + last_name
print(full_name)


# Task 14 — Sentence Creation
name = "Darsh"
age = "20"
city = "Ahmedabad"
language = "Python"

sentence = name + " is " + age + " years old and lives in " + city + ". He is learning " + language + "."
print(sentence)


# Task 15 — String and Integer
age = 20

print("Age: " + str(age))


# Part 8 — String Repetition

# Task 16
symbol = "*"

print(symbol * 3)
print(symbol * 5)
print(symbol * 10)


# Task 17 — Pattern
print("*" * 10)


# Part 9 — Case Conversion

# Task 18
text = "python programming language"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())


# Task 19 — Case-Insensitive Comparison
text1 = "Python"
text2 = "python"

print(text1 == text2)
print(text1.lower() == text2.lower())


# Part 10 — Searching

# Task 20 — Membership
text = "Python is a programming language"

print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)


# Task 21 — find()
print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))


# Task 22 — index()
print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))

print(text.find("Java"))


# Task 23 — Count Characters
text = "banana"

print(text.count("a"))
print(text.count("n"))
print(text.count("b"))


# Task 24 — Starts and Ends
filename = "student_notes.pdf"

print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))


# Part 11 — Replacing

# Task 25 — Replace a Word
text = "I am learning Java"

text = text.replace("Java", "Python")
print(text)


# Task 26 — Multiple Replacements
text = "apple apple apple"

text = text.replace("apple", "mango")
print(text)


# Task 27 — Limited Replacement
text = "apple apple apple"

text = text.replace("apple", "mango", 1)
print(text)


# Task 28 — Check Immutability
text = "Python"

text.upper()
print(text)

text = text.upper()
print(text)


# Part 12 — Whitespace

# Task 29
text = "   Python Programming   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())


# Task 30 — User Input
name = input("Enter your name: ")
name = name.strip()

print(name)


# Part 13 — Split and Join

# Task 31 — Split
text = "Python is easy to learn"

words = text.split()
print(words)


# Task 32 — Split with Separator
text = "apple,banana,mango,orange"

fruits = text.split(",")
print(fruits)


# Task 33 — Join
words = ["Python", "is", "easy"]

sentence = " ".join(words)
print(sentence)


# Task 34 — Join with Different Separators
words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))


# Part 14 — String Formatting

# Task 35 — F-String
name = "Darsh"
age = 20
city = "Ahmedabad"

print(f"My name is {name}, I am {age} years old, and I live in {city}.")


# Task 36 — Arithmetic Inside F-String
a = 10
b = 20

print(f"The sum is {a + b}")


# Part 15 — Error Identification

# Task 37 — A
text = "Python"
print(text[5])


# Task 37 — B
text = "Python"
text = "J" + text[1:]
print(text)


# Task 37 — C
age = 20
print("Age: " + str(age))


# Task 37 — D
text = "Python"
print(text.find("Java"))


# Part 16 — Practical Challenge

# Task 38 — Name Processor
name = input("Enter your full name: ")

print(name)
name = name.strip()

print(name)
print(name.upper())
print(name.lower())
print(name.title())
print(len(name))
print(name[0])
print(name[-1])
print("a" in name.lower())


# Part 17 — Practical Challenge

# Task 39 — Sentence Analyzer
sentence = input("Enter a sentence: ")

print(sentence)
print(len(sentence))

words = sentence.split()
print(len(words))

print(sentence[0])
print(sentence[-1])
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print("Python" in sentence)

character = input("Enter a character: ")
print(sentence.count(character))


# Part 18 — Final Challenge

# Task 40 — Student Information
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = input("Enter age: ").strip()