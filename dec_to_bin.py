def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0:
        remander = number % 2
        number = number // 2
        result = str(remander) + result
    return result

def main():
    num = input("Enter Decimal Number:")
    print("Decimal to Binary: {}".format(num, decimal_to_binary(num)))

if __name__ =="__main__":
    main()
