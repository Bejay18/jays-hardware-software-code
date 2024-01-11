def conversation():
    print("Do you like coding in Python? Say Yes or No")
    answer = input()
    if answer == "Yes":
        print("that's Good!- The United States needs more coders!")
    elif answer== "maybe":
        print("I understand your reason, I hope you can change your mind when you return!")
    else:
        print("i don't understand your awnswer, please try again later")
    print("Goodbye")

def main():
    print("welcome to the coder's job conversation system!")
    conversation()
    print("thanks for talking to me!")

if __name__=="__main__":
    main()
