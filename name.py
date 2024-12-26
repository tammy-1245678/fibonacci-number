def fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    # First two terms of the Fibonacci series
    a, b = 0, 1
    
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # To move to a new line

# Input from the user
try:
    terms = int(input("Enter the number of terms: "))
    fibonacci_series(terms)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
