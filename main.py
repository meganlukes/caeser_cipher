def talk(name, location, temp):
  print(f"hello {name}")
  print(f"How's the weather in {location}?")
  cel = int((temp - 32) * 5 / 9)
  print(f"It is currently {cel} degrees celsius")
talk("Megan", "Spring Hill", 70)
talk(temp=46, name="Andy", location="Denver")