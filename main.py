# Homework, Michał Wapiński, 79846

# Define number
a = 57189230573124233

# Function to check if it is prime

if a > 1:
   for w in range (2, a):
      if (a % w) == 0:
         print(a, "is not a prime number")
         break
      else:
         print(a, "is a prime number")

else:
   print(a, "is not a prime number");