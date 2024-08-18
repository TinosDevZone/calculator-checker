def get_numbers():
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  return num1, num2

def choose_operation():
  print("Would you like to +, -, / or *? :")
  operation = input() 
  return operation

def calculate(num1, num2, operation):
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  else:
    print("Invalid operation")
    result = None
  return result

def main():
  while True:
      num1, num2 = get_numbers()
      operation = choose_operation()
      result = calculate(num1, num2, operation)
      if result is not None:
          print(f"{num1} {operation} {num2} = {result}")
      print("Would you like to do another calculation? (y/n):")
      another_calculation = input()
      if another_calculation.lower() != "y":
          print("Goodbye!")
          break

main()
