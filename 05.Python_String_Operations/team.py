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
