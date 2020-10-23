def ReverseName(x):
  return x[::-1]

print("enter your First name?")
fname=input()
print("enter your last name?")
lname=input()
fname = ReverseName(fname)
lname = ReverseName(lname)
print(fname+ " " + lname)
