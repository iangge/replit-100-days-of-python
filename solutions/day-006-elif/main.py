username = input("Username: ")
password = input("Password: ")

if username == "ian" and password == "ians-password":
  print("Welcome Ian!")
elif username == "bill" and password == "bills-password":
  print("Welcome Bill!")
elif username == "zoe" and password == "zoes-password":
  print("Welcome Zoe!")
else:
  print("Username and password combination unknown. Please try again.")
