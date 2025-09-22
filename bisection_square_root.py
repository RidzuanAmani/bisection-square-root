# I set initial range, like setting bounds in my Tower of Hanoi
def square_root_bisection(number, epsilon=0.0001):
    if number < 0:
        return "Cannot compute square root of a negative number"
    if number == 0:
        return 0
    
    low = 0
    high = number
    
    # I iterate to find the root, inspired by recursion in Merge Sort
    while high - low > epsilon:
        mid = (low + high) / 2
        mid_squared = mid * mid
        
        # I check accuracy, similar to validation in Luhn
        if mid_squared == number:
            return mid
        elif mid_squared < number:
            low = mid
        else:
            high = mid
    
    # I return the approximation, learned from Arithmetic Formatter precision
    return (low + high) / 2

# I test the function, like in my Probability Calculator
def main():
    test_number = float(input("Enter a number to find its square root: "))
    result = square_root_bisection(test_number)
    print(f"The square root of {test_number} is approximately {result}")

if __name__ == "__main__":
    main()
