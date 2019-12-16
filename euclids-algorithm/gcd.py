# Find the greatest common denominator of two numbers
# Using Euclid's algorithm

# Approach 
# 
#  Using a while loop, and detect when b is equal to zero as the stopping point

def gcd(a, b):
  while (b != 0):       # Continue while b is not equal to zero
    t = a               # Temporary store the a variable
    a = b               # Set a equal to b ahead of time
    b = t % b           # Calculate

  return a              # Return a as the Greatest Common Denominator, (Which was assign from b)

# Try out the function with a few examples

print(gcd(60, 96))   # Should be 12
print(gcd(20, 8))    # Should b 4