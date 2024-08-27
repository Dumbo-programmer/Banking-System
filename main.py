import random
import string
import time
from datetime import datetime, timedelta

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
        self.recurring_transactions = []
        self.joint_users = [user_id]
        self.credit_score = random.randint(600, 750)
        self.currency = 'USD'
        self.budgets = {}
        self.transaction_categories = []
        self.emergency_fund = 0
        self.mfa_enabled = False
        self.mfa_code = None

        if acc_type == 'Premium':
            self.interest_rate *= 1.5
            self.overdraft_limit = -500

    def deposit(self, amount, savings=False, category='Miscellaneous'):
        if self.is_locked: return
        if savings:
            self.savings_balance += amount * self.multiplier
            self.history.append(f"Savings Deposit: {amount} {self.currency}, New Savings Balance: {self.savings_balance}")
        else:
            self.balance += amount * self.multiplier
            self.history.append(f"Deposit: {amount} {self.currency}, Category: {category}, New Balance: {self.balance}")
            self.update_budget(category, amount)
            self.check_emergency_fund()
        self.apply_interest()
        self.check_lock()

    def withdraw(self, amount, savings=False, category='Miscellaneous'):
        if self.is_locked: return
        if savings:
            if self.savings_balance >= amount:
                self.savings_balance -= amount * self.multiplier
                self.history.append(f"Savings Withdrawal: {amount} {self.currency}, New Savings Balance: {self.savings_balance}")
            else:
                self.notifications.append("Insufficient savings balance for withdrawal.")
        else:
            fee = self.apply_transaction_fee()
            self.balance -= (amount + fee) * self.multiplier
            self.history.append(f"Withdraw: {amount} {self.currency}, Fee: {fee}, Category: {category}, New Balance: {self.balance}")
            self.update_budget(category, -amount)
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
            self.history.append(f"Interest Applied: {interest} {self.currency}, New Balance: {self.balance}")
            self.last_interest_time = time.time()

    def take_loan(self, amount):
        if self.is_locked: return
        rate = self.adjust_loan_rate()
        self.loans.append((amount, rate))
        self.balance += amount
        self.history.append(f"Loan Taken: {amount} {self.currency}, Interest Rate: {rate}, New Balance: {self.balance}")
        self.apply_interest()
        self.check_lock()

    def repay_loan(self, amount):
        if self.is_locked or not self.loans: return
        loan_to_repay = self.loans.pop(0)
        repayment_amount = min(amount, loan_to_repay[0])
        self.balance -= repayment_amount
        self.history.append(f"Loan Repaid: {repayment_amount} {self.currency}, New Balance: {self.balance}")
        self.loans.insert(0, (loan_to_repay[0] - repayment_amount, loan_to_repay[1]))
        if loan_to_repay[0] - repayment_amount > 0:
            self.history.append(f"Remaining Loan: {loan_to_repay[0] - repayment_amount}")
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
        self.history.append(f"Invested in {portfolio}: {amount} {self.currency}, Profit/Loss: {profit_loss}, New Balance: {self.balance}")
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
        self.history.append(f"Reward Earned: {reward} {self.currency}, Total Rewards: {self.rewards}")

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
        return sum([loan[0] for loan in self.loans]), len(self.loans)

    def get_rewards(self):
        return self.rewards

    def get_investments(self):
        return self.investments

    def get_notifications(self):
        return self.notifications

    def set_recurring_transaction(self, amount, frequency, operation_type, savings=False):
        self.recurring_transactions.append((amount, frequency, operation_type, savings))

    def process_recurring_transactions(self):
        for transaction in self.recurring_transactions:
            amount, frequency, operation_type, savings = transaction
            if operation_type == 'deposit':
                self.deposit(amount, savings=savings)
            elif operation_type == 'withdraw':
                self.withdraw(amount, savings=savings)

    def add_joint_user(self, user_id):
        self.joint_users.append(user_id)

    def simulate_credit_score(self):
        score_change = random.randint(-20, 20)
        self.credit_score = min(max(self.credit_score + score_change, 300), 850)
        self.history.append(f"Credit Score Change: {score_change}, New Credit Score: {self.credit_score}")

    def adjust_loan_rate(self):
        return random.uniform(0.05, 0.1) if self.credit_score > 700 else random.uniform(0.1, 0.2)

    def generate_statement(self):
        statement = f"Monthly Statement for User {self.user_id}\n"
        statement += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
        statement += f"Balance: {self.balance} {self.currency}\n"
        statement += f"Savings Balance: {self.savings_balance} {self.currency}\n"
        statement += f"Loans: {self.get_loans()[0]} {self.currency}\n"
        statement += f"Investments: {len(self.get_investments())} active\n"
        statement += f"Rewards: {self.get_rewards()} {self.currency}\n"
        statement += f"Credit Score: {self.credit_score}\n"
        statement += "Recent Transactions:\n"
        statement += "\n".join(self.history[-10:])
        return statement

    def convert_currency(self, amount, target_currency):
        conversion_rates = {
            'USD': 1, 'EUR': 0.85, 'JPY': 110, 'GBP': 0.75
        }
        if self.currency in conversion_rates and target_currency in conversion_rates:
            converted_amount = amount * conversion_rates[target_currency] / conversion_rates[self.currency]
            self.history.append(f"Converted {amount} {self.currency} to {converted_amount} {target_currency}")
            return converted_amount
        else:
            self.notifications.append(f"Currency conversion not supported for {target_currency}")
            return amount

    def set_budget(self, category, limit):
        self.budgets[category] = limit

    def update_budget(self, category, amount):
        if category in self.budgets:
            self.budgets[category] -= amount
            if self.budgets[category] < 0:
                self.notifications.append(f"Budget exceeded for {category}")

    def check_emergency_fund(self):
        if self.balance > 500:
            surplus = (self.balance - 500) * 0.2
            self.emergency_fund += surplus
            self.balance -= surplus
            self.history.append(f"Transferred {surplus} {self.currency} to Emergency Fund, New Balance: {self.balance}")

    def enable_mfa(self):
        self.mfa_enabled = True
        self.generate_mfa_code()

    def generate_mfa_code(self):
        self.mfa_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.notifications.append(f"MFA Code Generated: {self.mfa_code}")

    def validate_mfa(self, code):
        if self.mfa_code == code:
            self.notifications.append("MFA Code validated successfully.")
            self.mfa_code = None
            return True
        else:
            self.notifications.append("MFA Code validation failed.")
            return False

    def get_global_summary(self):
        return {
            'global_balance': self.balance + self.savings_balance,
            'total_loans': self.get_loans()[0],
            'transaction_count': len(self.history),
            'total_penalties': self.get_penalties()[0],
            'total_investments': len(self.investments),
            'system_locked': self.is_locked,
            'currency': self.currency,
            'credit_score': self.credit_score,
            'emergency_fund': self.emergency_fund
        }
