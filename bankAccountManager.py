# input from user options
# 3 options, option 1 -> see balance, option 2 -> add amount, option 3 -> withdraw amount
# for option 1, use function 1
# for option 2, use function 2
# for option 3, use function 3
# return the original amount at the end

balance = 0


def addBalance():
    global balance
    amount = float(input("Enter the amount to add: "))
    balance += amount
    print(f"Amount {amount} added to the balance. Current balance is {balance}")


def withdrawBalance():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance to withdraw")
    else:
        balance -= amount
        print(
            f"Amount {amount} withdrawn from the balance. Current balance is {balance}")


def seeBalance():
    global balance
    print(f"Current balance is {balance}.")


while True:
    user_input = input("Enter the option to choose: ")
    if user_input == "1":
        addBalance()
    elif user_input == "2":
        withdrawBalance()
    elif user_input == "3":
        seeBalance()
    elif user_input == "q":
        break
    else:
        print("Invalid balance")

print(f"Final balance is {balance}")
