#que 1
text = "Python"

print(text[0])#P
print(text[3])#t
print(text[-1])#n
print(text[-2])#o

#que2
text = "Programming"

print(text[0:4])#Pro
print(text[3:8])#gramm
print(text[:5])#Progr
print(text[5:])#amming

#que 3
text = "Python"

print(text[::2])#Pto
print(text[1::2])#yhn
print(text[::-1])#nothyP

#que 4
text = "Hello World"

print(len(text))#11
print(text[5])#_
print(text[-1])#d


#que5

text = "Python Programming"

print("Python" in text) # True
print("Java" in text) #False
print("Java" not in text) #True

#que 6
text = "banana"

print(text.find("a"))#3
print(text.find("z"))#-1
print(text.count("a"))#3

#que 7
text = "Python"

print(text.upper())#PYTHON
print(text.lower())#python
print(text.capitalize())#Python
print(text.title())#Python
print(text.swapcase())#pYTHON

#que 8
text = "I like Java"

print(text.replace("Java", "Python"))#I like Python

#que 9

text = "Hello"

print(text + " World")#Hello World
print(text * 3)#HelloHelloHello


