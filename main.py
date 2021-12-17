import math

#How to instantiate variables
# def talk(name, location, temp):
#   print(f"hello {name}")
#   print(f"How's the weather in {location}?")
#   cel = int((temp - 32) * 5 / 9)
#   print(f"It is currently {cel} degrees celsius")
# talk("Megan", "Spring Hill", 70)
# talk(temp=46, name="Andy", location="Denver")


#How many cans of paint, round up
# def paint_calc(height, width, cover):
#   paint = math.ceil((height * width) / cover)
#   print(paint)
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#prime number checker
# def prime_checker(number):
#   factors = 0
#   for digit in range(1, number):
#     if number % digit == 0:
#       factors = factors + 1
#   print(factors)
#   if factors == 1 or number == 1:
#     print(f"{number} is a prime number")
#   else:
#     print(f"{number} is not a prime number")
# n = int(input("Check this number: "))
# prime_checker(number=n)


#Caeser Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
text_array = []
new_string = ""
for letter in text:
  number = alphabet.index(letter)
  text_array.append(number)
print(text_array)
for digit in text_array:
  if direction == "encode":
    new_number = digit + shift
    if new_number > 26:
      new_number = new_number - 27
  if direction == "decode":
    new_number = digit - shift
    if new_number < 0:
      new_number = new_number + 27
  new_string = new_string + alphabet[new_number]
print(new_string)
print(" ")