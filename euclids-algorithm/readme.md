# Euclid's Algorithm

Find the greatest common denominator (GCD) of two integers.

## Example:

GCD of 20 and 8 is 4 (because 8 / 4 = 2; and 20 / 4 = 5)

## How the Algorithm Work

1. For two integer `a` and `b`, where `a > b`, divide `a` by `b`.

2. If the remainder, `r` is `0`, then stop: GCD is `b`.

3. Otherwise, set `a` to `b`, `b` to `r`, and repeat step 1 until `r` is `0`.

### GCD (20, 8)

|  a  |  b  |  r  |
|-----|:---:|----:|
| 20  |  8  |  4  |
| 8   |  4  |  0  |


## Via Code

### Starting Point

```python
def gcd(a, b):
  while (b != 0):       # Continue while b is not equal to zero
    t = a               # Temporary store the a variable
    a = b               # Set a equal to b ahead of time
    b = t % b           # Calculate for remainder, and assign remainder to b

  return a              # Return a as the Greatest Common Denominator, (Which was assign from b)

# Try out the function with a few examples

print(gcd(60, 96))   # Should be 12
print(gcd(20, 8))    # Should b 4

```