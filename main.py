class Customer:
    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.account = []

    def open_account(self,customer_id):
        if customer_id not in self.account:
            self.account.append(customer_id)
        else:
            print("Your Account already exist in our system")

    def close_account(self, customer_id):
        if customer_id in self.account:
            self.account.remove(customer_id)
        else:
            print("Your account is not present in our system")

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nname: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"


class Account(Customer):

    def __init__(self, account_number, account_type):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
        self.transactions = []

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Credited : Rs{amount }")
            # print("Remaining Balance is: ", self.balance)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Debited : Rs{amount}")
            # print("Remaining Balance is: ",self.balance)


    def __str__(self):
        return f'Account number: {self.account_number} \nAccount type: {self.account_type} \nBalance: {self.balance}'

# creat customers
alice = Customer(1,"Alice Smith","123 Main St","555-1234")
bob = Customer(2, "Bob Johnson","456 Ook St","555-5678")

alice_savings = Account(101,"Savings")
alice_current = Account(102,"Current")
bob_current = Account(103,"Current")

# open accounts
alice.open_account(alice_savings)
alice.open_account(alice_current)
bob.open_account(bob_current)

alice_savings.deposite(1000)
alice_savings.withdraw(500)
alice_current.deposite(2000)
alice_current.withdraw(1500)
bob_current.deposite(1500)
bob_current.withdraw(800)

print(alice)

print("Customer Details - Alice:")
print("\nAccount Details - Alice:")
for account in alice.account:
    print(account)
    print("Transaction History:")
    for transaction in account.transactions:
        print(transaction)
    print()

print("\nCustomer Details - Bob:")
print(bob)
print("\nAccount Details - Bob:")
for account in bob.account:
    print(account)
    print("Ttansaction History:")
    for transaction in account.transactions:
        print(transaction)
    print()

