spongeBobFan = input("Are you a SpongeBob fan? ")

if spongeBobFan.lower() == "yes":
  print("Great! I'll ask some questions to see if you are a real fan.")
  spongeBobNeighbor = input("Name one of SpongeBob's neighbor's: " )
  
  if spongeBobNeighbor == "Patrick":
    print("Correct! Patrick is one of SpongeBob's neighbors.")
  elif spongeBobNeighbor == "Squidward":
    print("Yes! Squidward is one of SpongeBob's neighbors.")
  else:
    print("Incorrect. You are not a real fan.")

else:
  print("Aw man, you should watch it.")
