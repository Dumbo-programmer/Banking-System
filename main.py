import random
import string
import time

class Account:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0
        self.is_locked = False
        self.history = []
        self.multiplier = random.uniform(0.8, 1.2)
        self.penalties = []
        self.overdraft_limit = -100
        self.interest_rate = random.uniform(0.01, 0.05)
        self.last_interest_time = time.time()
        self.loans = []

    def deposit(self, amount):
        if self.is_locked: return
        self.balance += amount * self.multiplier
        self.history.append(f"Deposit: {amount}, New Balance: {self.balance}")
        self.apply_interest()
        self.check_lock()

    def withdraw(self, amount):
        if self.is_locked: return
        self.balance -= amount * self.multiplier
        self.history.append(f"Withdraw: {amount}, New Balance: {self.balance}")
        self.apply_interest()
        if self.balance < self.overdraft_limit:
            self.is_locked = True
        self.check_lock()

    def apply_penalty(self):
        penalty = self.balance * random.uniform(0.01, 0.05)
        self.penalties.append(penalty)
        self.balance -= penalty
        if self.balance < self.overdraft_limit:
            self.is_locked = True

    def apply_interest(self):
        if time.time() - self.last_interest_time > 10:  # Apply interest every 10 seconds
            interest = self.balance * self.interest_rate
            self.balance += interest
            self.history.append(f"Interest Applied: {interest}, New Balance: {self.balance}")
            self.last_interest_time = time.time()

    def take_loan(self, amount):
        if self.is_locked: return
        self.loans.append(amount)
        self.balance += amount
        self.history.append(f"Loan Taken: {amount}, New Balance: {self.balance}")
        self.apply_interest()
        self.check_lock()

    def repay_loan(self, amount):
        if self.is_locked or not self.loans: return
        loan_to_repay = self.loans.pop(0)
        repayment_amount = min(amount, loan_to_repay)
        self.balance -= repayment_amount
        self.history.append(f"Loan Repaid: {repayment_amount}, New Balance: {self.balance}")
        self.loans.insert(0, loan_to_repay - repayment_amount)
        if loan_to_repay - repayment_amount > 0:
            self.history.append(f"Remaining Loan: {loan_to_repay - repayment_amount}")

        if self.balance < self.overdraft_limit:
            self.is_locked = True
        self.apply_interest()

    def check_lock(self):
        if len(self.history) > 20 or self.balance < self.overdraft_limit:
            self.is_locked = True

    def reset(self):
        self.is_locked = False
        self.balance = 0
        self.history.clear()
        self.penalties.clear()
        self.loans.clear()

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history

    def get_penalties(self):
        return sum(self.penalties), len(self.penalties)

    def get_loans(self):
        return sum(self.loans), len(self.loans)


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.system_locked = False
        self.global_balance = 0
        self.total_loans = 0
        self.transaction_count = 0

    def create_account(self, user_id):
        if user_id not in self.accounts:
            self.accounts[user_id] = Account(user_id)

    def perform_operation(self, user_id, amount, operation_type):
        if self.system_locked: return
        if user_id in self.accounts:
            account = self.accounts[user_id]
            if operation_type == 'deposit':
                account.deposit(amount)
            elif operation_type == 'withdraw':
                account.withdraw(amount)
            elif operation_type == 'loan':
                account.take_loan(amount)
                self.total_loans += amount
            elif operation_type == 'repay':
                account.repay_loan(amount)
                self.total_loans -= amount

            account.apply_penalty()
            self.transaction_count += 1
            if account.is_locked:
                self.system_locked = True
            self.global_balance += account.get_balance()

    def transfer(self, from_user, to_user, amount):
        if from_user in self.accounts and to_user in self.accounts:
            self.perform_operation(from_user, amount, 'withdraw')
            self.perform_operation(to_user, amount, 'deposit')

    def reset_system(self):
        for account in self.accounts.values():
            account.reset()
        self.system_locked = False
        self.global_balance = 0
        self.total_loans = 0
        self.transaction_count = 0

    def get_audit_log(self):
        logs = {}
        for user_id, account in self.accounts.items():
            logs[user_id] = {
                'balance': account.get_balance(),
                'history': account.get_history(),
                'penalties': account.get_penalties(),
                'loans': account.get_loans()
            }
        return logs

    def get_system_status(self):
        if self.system_locked:
            return "System is locked"
        else:
            return f"Global Balance: {self.global_balance}, Total Loans: {self.total_loans}, Transactions: {self.transaction_count}"


class TransactionSystem:
    def __init__(self):
        self.bank = BankSystem()

    def run_transactions(self):
        users = ['user1', 'user2', 'user3', 'user4', 'user5']
        for user in users:
            self.bank.create_account(user)
            self.bank.perform_operation(user, random.randint(100, 500), 'deposit')
            self.bank.perform_operation(user, random.randint(50, 250), 'withdraw')
            if random.random() > 0.5:
                self.bank.perform_operation(user, random.randint(200, 1000), 'loan')
            if random.random() > 0.3:
                self.bank.perform_operation(user, random.randint(100, 300), 'repay')

        for _ in range(random.randint(1, 10)):
            from_user, to_user = random.sample(users, 2)
            self.bank.transfer(from_user, to_user, random.randint(20, 100))

        if random.random() > 0.7:
            self.bank.system_locked = True

    def get_overview(self):
        return self.bank.get_system_status()

    def get_audit_report(self):
        return self.bank.get_audit_log()


# Executing the system
ts = TransactionSystem()
for _ in range(5):
    ts.run_transactions()

print(ts.get_overview())
print(ts.get_audit_report())
