import random
import string
import time

class Account:
    def __init__(self, user_id, acc_type='Basic'):
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
        self.acc_type = acc_type
        self.investments = []
        self.rewards = 0
        self.savings_balance = 0
        self.fraud_flagged = False
        self.notifications = []

        if acc_type == 'Premium':
            self.interest_rate *= 1.5
            self.overdraft_limit = -500

    def deposit(self, amount, savings=False):
        if self.is_locked: return
        if savings:
            self.savings_balance += amount * self.multiplier
            self.history.append(f"Savings Deposit: {amount}, New Savings Balance: {self.savings_balance}")
        else:
            self.balance += amount * self.multiplier
            self.history.append(f"Deposit: {amount}, New Balance: {self.balance}")
        self.apply_interest()
        self.check_lock()

    def withdraw(self, amount, savings=False):
        if self.is_locked: return
        if savings:
            if self.savings_balance >= amount:
                self.savings_balance -= amount * self.multiplier
                self.history.append(f"Savings Withdrawal: {amount}, New Savings Balance: {self.savings_balance}")
            else:
                self.notifications.append("Insufficient savings balance for withdrawal.")
        else:
            fee = self.apply_transaction_fee()
            self.balance -= (amount + fee) * self.multiplier
            self.history.append(f"Withdraw: {amount}, Fee: {fee}, New Balance: {self.balance}")
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
            self.notifications.append("Account locked due to penalty.")
        self.check_lock()

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
            self.notifications.append("Account locked due to loan repayment.")
        self.apply_interest()

    def invest(self, portfolio, amount):
        if self.is_locked or self.balance < amount: return
        risk = random.uniform(0.7, 1.3)
        profit_loss = amount * (random.uniform(0.05, 0.2) if portfolio == 'high-risk' else random.uniform(0.02, 0.1)) * risk
        self.balance += profit_loss - amount
        self.investments.append((portfolio, amount, profit_loss))
        self.history.append(f"Invested in {portfolio}: {amount}, Profit/Loss: {profit_loss}, New Balance: {self.balance}")
        self.check_lock()

    def apply_transaction_fee(self):
        fee = 0
        if self.acc_type == 'Basic':
            fee = 2
        elif self.acc_type == 'Premium':
            fee = 1
        return fee

    def add_reward(self):
        reward = random.randint(5, 20)
        self.rewards += reward
        self.history.append(f"Reward Earned: {reward}, Total Rewards: {self.rewards}")

    def fraud_check(self, amount):
        if abs(amount) > self.balance * 0.9 or len(self.history) > 50:
            self.fraud_flagged = True
            self.notifications.append("Fraudulent activity detected!")
            self.is_locked = True

    def check_lock(self):
        if self.fraud_flagged or len(self.history) > 30 or self.balance < self.overdraft_limit:
            self.is_locked = True

    def reset(self):
        self.is_locked = False
        self.balance = 0
        self.history.clear()
        self.penalties.clear()
        self.loans.clear()
        self.investments.clear()
        self.rewards = 0
        self.savings_balance = 0
        self.fraud_flagged = False
        self.notifications.clear()

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history

    def get_penalties(self):
        return sum(self.penalties), len(self.penalties)

    def get_loans(self):
        return sum(self.loans), len(self.loans)

    def get_rewards(self):
        return self.rewards

    def get_investments(self):
        return self.investments

    def get_notifications(self):
        return self.notifications


class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.system_locked = False
        self.global_balance = 0
        self.total_loans = 0
        self.transaction_count = 0
        self.total_penalties = 0
        self.total_investments = 0

    def create_account(self, user_id, acc_type='Basic'):
        if user_id not in self.accounts:
            self.accounts[user_id] = Account(user_id, acc_type)

    def perform_operation(self, user_id, amount, operation_type, savings=False):
        if self.system_locked: return
        if user_id in self.accounts:
            account = self.accounts[user_id]
            if operation_type == 'deposit':
                account.deposit(amount, savings=savings)
            elif operation_type == 'withdraw':
                account.withdraw(amount, savings=savings)
            elif operation_type == 'loan':
                account.take_loan(amount)
                self.total_loans += amount
            elif operation_type == 'repay':
                account.repay_loan(amount)
                self.total_loans -= amount
            elif operation_type == 'invest':
                account.invest(random.choice(['low-risk', 'high-risk']), amount)

            account.apply_penalty()
            account.add_reward()
            account.fraud_check(amount)
            self.transaction_count += 1
            if account.is_locked:
                self.system_locked = True
            self.global_balance += account.get_balance()
            self.total_penalties += account.get_penalties()[0]
            self.total_investments += sum([inv[2] for inv in account.get_investments()])

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
        self.total_penalties = 0
        self.total_investments = 0

    def get_audit_log(self):
        logs = {}
        for user_id, account in self.accounts.items():
            logs[user_id] = {
                'balance': account.get_balance(),
                'history': account.get_history(),
                'penalties': account.get_penalties(),
                'loans': account.get_loans(),
                'rewards': account.get_rewards(),
                'investments': account.get_investments(),
                'notifications': account.get_notifications()
            }
        return logs

    def get_global_summary(self):
        return {
            'global_balance': self.global_balance,
            'total_loans': self.total_loans,
            'transaction_count': self.transaction_count,
            'total_penalties': self.total_penalties,
            'total_investments': self.total_investments,
            'system_locked': self.system_locked
        }
