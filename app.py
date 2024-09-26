from operator import truediv

from utils.current_account import CurrentAccount
from utils.custom_exceptions import AccountNotFoundException, LowBalanceException
from utils.savings_account import SavingsAccount
import json

user_choices_prompt = '''\nPress 1 to Create new Account\nPress 2 to fetch account details\nPress 3 to fetch account balance\nPress 4 to tranfer money\nPress 5 to exit\nEnter your choice: '''
account_type_prompt = '''\nPress 1 to create savings account\nPress 2 to create current account\nEnter your choice: '''


def create_new_account():
    initial_balance = float(input('Enter initial balance: '))
    acc_type = input(account_type_prompt)
    if acc_type == '1':
        account = SavingsAccount(initial_balance, 'savings')
        acc_id = account.get_account_id
        print(f"Your account id is: {acc_id}")
    elif acc_type =='2':
        account = CurrentAccount(initial_balance, 'current')
        acc_id = account.get_account_id
        print(f"Your account id is: {acc_id}")
    else:
        print('Please enter correct choice!!!')


def fetch_account_details():
    account_id = int(input("Enter account id to fetch details: "))
    with open('database/accounts.json', 'r') as file:
        accounts = json.load(file)
    for account in accounts:
        if account["id"] == account_id:
            display_account(account)


def display_account(account):
    print(account)


def fetch_account_balance():
    account_id = int(input("Enter account id to fetch details: "))
    with open('database/accounts.json', 'r') as file:
        accounts = json.load(file)
    for account in accounts:
        if account["id"] == account_id:
            print(account["balance"])


def get_account_index(accounts, account_id):
    for index, account in enumerate(accounts):
        if account["id"] == account_id:
            return index
    else:
        raise AccountNotFoundException(f'No account found with account id {account_id}')


def transfer_money():
    source_account_id = int(input('Enter source account id: '))
    destination_account_id = int(input('Enter destination account id: '))
    amount = float(input('Enter amount to transfer: '))

    with open('database/accounts.json', 'r') as file:
        accounts = json.load(file)
    source_account_index = get_account_index(accounts, source_account_id)
    destination_account_index = get_account_index(accounts, destination_account_id)

    if accounts[source_account_index]["balance"] > amount:
        accounts[source_account_index]["balance"] -= amount
        accounts[destination_account_index]["balance"] += amount
    else:
        raise LowBalanceException()

    with open('database/accounts.json', 'w') as file:
        json.dump(accounts, file)


user_choices_mapping = {
    '1': create_new_account,
    '2': fetch_account_details,
    '3': fetch_account_balance,
    '4': transfer_money
}


def run_app():
    while True:
        user_choice = input(user_choices_prompt)
        try:
            user_choices_mapping[user_choice]()
        except KeyError:
            if user_choice == '5':
                break
            print('Please enter correct choice')


if __name__ == '__main__':
    run_app()