# define the function
def factorial(n):
 # Initialize
    x = 1
# Include a for loop, looping from 1 to n + 1
    for i in range(1, n + 1):
        x = x * i
    return x
# Display output
print(factorial(5))
