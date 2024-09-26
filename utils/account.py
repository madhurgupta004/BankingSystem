import json
class Account:
    def __init__(self, initial_balance, account_type):
        self.balance = initial_balance
        self.account_id = self.generate_account_id()
        self.account_type = account_type
        self.__write_account_data()

    def generate_account_id(self):
        with open('database/acc_ids.json', 'r') as file:
            json_object = json.load(file)
        account_id = json_object['last_id'] + 1
        json_object = {
            "last_id" : account_id
        }
        with open('database/acc_ids.json', 'w') as file:
            json.dump(json_object, file)
        return account_id

    def __write_account_data(self):
        with open('database/accounts.json', 'r') as file:
            accounts = json.load(file)
        new_account_object = {
            "id" : self.account_id,
            "type" : self.account_type,
            "balance" : self.balance
        }
        accounts.append(new_account_object)
        with open('database/accounts.json', 'w') as file:
            json.dump(accounts, file)

    @property
    def get_account_id(self):
        return self.account_id
