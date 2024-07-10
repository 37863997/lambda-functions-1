def math_operations(a, b):
    """
    The function takes two numbers as input 
    It then performs the following operations using lambda functions:
    1. Calculates and returns the sum of the two numbers.
    2. Calculates and returns the product of the two numbers.
    """
    sum_lambda = lambda x, y: x + y
    product_lambda = lambda x, y: x * y
    
    return sum_lambda(a, b), product_lambda(a, b)

def main():
    # Capture inputs from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result, product_result = math_operations(num1, num2)

    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The product of {num1} and {num2} is: {product_result}")

if __name__ == "__main__":
    main()
