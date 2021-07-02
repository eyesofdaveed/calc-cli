print("Welcome to Command Line Interface for basic calculator operations")
print("Type --help or -h to get all avaiable commands")

def sumNum():
    nums = list(map(int, input("Type in numbers followed by space you want to add on the next line: \n").split()))
    return str(sum(nums))

def sumOdd():
    nums = list(map(int, input("Type in numbers followed by space you want to add on the next line: \n").split()))
    result = 0
    for num in nums:
        if num%2 == 1:
            result = result + num
    return str(result)
    
def sumEven():
    nums = list(map(int, input("Type in numbers followed by space you want to add on the next line: \n").split()))
    result = 0
    for num in nums:
        if num%2 == 0:
            result = result + num
    return str(result)

def sumFloat():
    nums = list(map(float, input("Type in numbers followed by space you want to add on the next line: \n").split()))
    return str(sum(nums))

def help():
    print("List of all available commands: \n \
    add - returns sum of listed numbers \n \
    -f - returns sum of all float numbers \n \
    even/odd - returns sum of only even or odd numbers in the list \n \
    -q/--quit - exit the CLI")

command = input("User: ")
while command != "-q" and command != "--quit":
    if command == "add":
        print("Sum of all numbers:" + sumNum())
    elif command == "odd":
        print("Sum of all add numbers: " + sumOdd())
    elif command == "even":
        print("Sum of all even numbers: " + sumEven())
    elif command == "-f":
        print("Sum of all float numbers: " + sumFloat())
    elif command == "--help" or command == "-h":
        print(help())
    else:
        print("Unknown command, please refer to --help/-h to get all available commands.")

    command = input("User: ")

print("CLI terminated, Bye-bye...")