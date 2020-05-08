#this is the very start of this program
import random
import os
import datetime

def get_balance():
    opening_balance = input('Enter deposit amount :: ')
    try:
        opening_balance = int(opening_balance)
    except ValueError:
        print("don't be stupid" + " " + "Enter a digit")
        return get_opening_balance()
    else:
        return opening_balance

def get_account_type():
    keys = ['savings', 'current', 'joint']
    prompt = input('Enter account type. Enter "savings" for savings account, "joint" for joint account  and "current" for current account. ')
    if prompt not in keys:
        print('Invalid input! Enter "savings" , "joint" or "current".')
        return get_account_type()
    else:
        return prompt

def get_account_number():
    password = ''
    for x in range(1, 11):
        key = random.randint(0, 9)
        key = str(key)
        password += key
    return password

def get_login_time():
    now = datetime.datetime.now()
    now = now.strftime("%b-%d-%Y %H:%M")
    return now

def login():
    username = input('Enter username :: ').strip()
    username = username.lower()
    password = input('Enter password :: ').strip()
    password = password.lower()
    with open('staff.txt') as staff_data:
        staffs = staff_data.readlines()
        for line in staffs:
            line = line.strip().split(', ')
            if username == line[0] and password == line[1]:
                return True
        return False


def welcome():
    print('You are welcome to SN Bank!')
    prompt = input('Enter "1" to Create new bank account, "2" to Check Account Details or "3" to Logout :: ' )
    try:
        prompt = int(prompt)
    except ValueError:
        print('You can only enter a digit, e.g "1" to Create new bank account, "2" to Check Account Details or "3" to Logout :: ')
        return welcome()
    else:
        keys = [1, 2, 3]
        if prompt not in keys:
            print('Invalid input! Please enter "1, 2, "or" 3".')
            return welcome()

        else:
            if prompt == 1:
                account_name = input('Enter full name :: ')
                opening_balance = get_balance()
                account_type = get_account_type()
                account_email = input('Enter a valid email address.')
                account_number = get_account_number()
                print(f"Account name: {account_name}")
                print(f"Account balance: {opening_balance}")
                print(f"Account type: {account_type}")
                print(f"Account mail address: {account_email}")
                print(f"Account number: {account_number}")
                with open('customer.txt', 'a') as customer_file:
                    customer_file.write(f'{account_name}, {opening_balance}, {account_type}, {account_email}, {account_number}\n')
                    return welcome()



            elif prompt == 2:
                acc_number = input('Enter your account number :: ')
                with open('customer.txt') as customer_file:
                    customers = customer_file.readlines()
                    for customer in customers:
                        customer = customer.split(', ')
                        customer = (", ").join(customer).strip()
                        customer = customer.split(', ')
                        if acc_number == customer[4]:
                            print('Your account details is below :: ')
                            print(f'Account Name: {customer[0]}')
                            print(f'Account Balance: {customer[1]}')
                            print(f'Account Type: {customer[2]}')
                            print(f'Mail Address: {customer[3]}')
                            print(f'Account Number: {customer[4]}')
                            welcome()


            else:
                if os.path.exists("user.txt"):
                    print('Goodbye')
                    os.remove("user.txt")
                    return main()
                else:
                    pass


def main():
    prompt = input('Enter "Login" to login and "Close" to close app. :: ')
    prompt = prompt.lower()
    if prompt != 'login' and prompt != 'close':
        print('Invalid key! Ensure you enter the correct key.')
        return main()

    if prompt == 'login':
        if not login():
            print('Invalid input. Try again!')
            return auth_staff()
        else:
            print('Welcome Back!')
            time = get_login_time()
            with open('user.txt', 'w') as session:
                session.write(f'You have logged in successfully! Logged in time was {time}.')
            welcome()

    else:
        print('The app has been terminated.')
main()
