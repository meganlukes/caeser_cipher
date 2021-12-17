import math
# def talk(name, location, temp):
#   print(f"hello {name}")
#   print(f"How's the weather in {location}?")
#   cel = int((temp - 32) * 5 / 9)
#   print(f"It is currently {cel} degrees celsius")
# talk("Megan", "Spring Hill", 70)
# talk(temp=46, name="Andy", location="Denver")

#How many cans of paint, round up
def paint_calc(height, width, cover):
  paint = math.ceil((height * width) / cover)
  print(paint)
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)