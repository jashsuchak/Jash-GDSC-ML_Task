def calculate(express):
    try:
        result = eval(express)
        return result
    except (SyntaxError, ZeroDivisionError, NameError) as e:
        return 'Error',e

while True:
    express = input("Enter an expression to calculate (or 'exit' to quit): ")
    
    if express.lower() == 'exit':
        break
    
    result = calculate(express)
    print("Result:", result)
