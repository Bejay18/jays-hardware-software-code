def while_counter(num):
    while num < 11:
        print("while count: {}" .format(num))
        num += 1


def for_counter(num):
    for count in range (num,11,1):
        print("for count: {}".format(count))


def main():
    counter = 0
    while_counter(counter)
    for_counter(counter)

if __name__ == "__main__":
    main()
