#PRACTICAL 2
#AIM: A program that calculates the area and perimeter of a rectangle.
while True:
  1=float (input("Enter the length: "))
  b=float(input("\nEnter the breadth: "))
  print("\nl.Area\n2.Perimeter\n3.Exit")
  cho+int (input("\nEnter the choice: "))
if cho==1:
  area=1
  print("\nArea of the rectangle with length", end=" ")
  print (1, "and breadth", b, "is: ",area)
elif cho 2:
  per 2*(1+b)
elif cho--3:
  break
else:
  print("Invalid Input!")
