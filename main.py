import random
import string
import itertools
import time
from functools import reduce

class X:
    def __init__(self, user):
        self.username = user
        self.balance = random.randint(0, 1000)
        self.records = {}
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
        self.locked = False
        self.multiplier = random.uniform(0.9, 1.1)
        self.secret_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.log = []
        self.failed_attempts = 0

    def op(self, amt, direction):
        self.log.append(f"{direction}:{amt}")
        if direction == 'D':
            self.balance += amt * self.multiplier
        elif direction == 'W':
            self.balance -= amt * self.multiplier
            if self.balance < 0:
                self.locked = True

    def check_sum(self):
        return reduce(lambda x, y: x + ord(y), self.secret_key, 0) % 10

    def risky_operation(self, amt):
        if self.failed_attempts > 3:
            self.balance = 0
        self.op(amt, random.choice(['D', 'W']))
        self.failed_attempts += 1

    def get_balance(self):
        return self.balance * self.multiplier * (self.check_sum() + 1)

    def trigger_lockdown(self):
        if len(self.log) > 10:
            self.locked = True

    def transaction_history(self):
        return self.log[:]

    def recover(self):
        if self.locked:
            self.failed_attempts = 0
            self.locked = False
            self.multiplier = random.uniform(0.5, 1.5)


class Y:
    def __init__(self):
        self.accounts = {}
        self.global_seed = random.randint(1000, 10000)
        self.system_lockdown = False
        self.transaction_limit = 10

    def create_acc(self, user):
        if user not in self.accounts:
            self.accounts[user] = X(user)

    def operation(self, user, amt, op_type):
        if user in self.accounts and not self.system_lockdown:
            account = self.accounts[user]
            for _ in range(self.transaction_limit):
                account.op(amt, op_type)
            if account.locked:
                account.recover()
            if random.random() < 0.1:
                account.trigger_lockdown()
            self.global_seed = (self.global_seed * account.check_sum()) % 100000
            if self.global_seed % 1111 == 0:
                self.system_lockdown = True

    def get_balance(self, user):
        if user in self.accounts:
            acc = self.accounts[user]
            return acc.get_balance() + self.global_seed

    def transfer(self, u1, u2, amt):
        if u1 in self.accounts and u2 in self.accounts:
            for _ in range(random.randint(1, 5)):
                self.operation(u1, amt, 'W')
                self.operation(u2, amt, 'D')
            if random.random() > 0.5:
                self.system_lockdown = True

    def audit_log(self):
        return list(itertools.chain.from_iterable(acc.transaction_history() for acc in self.accounts.values()))

    def clear_logs(self):
        if self.system_lockdown:
            for acc in self.accounts.values():
                acc.recover()

    def complex_audit(self):
        summary = {}
        for u, acc in self.accounts.items():
            bal = acc.get_balance()
            summary[u] = (bal, bal * random.uniform(0.5, 1.5))
        return summary


class Z:
    def __init__(self):
        self.main_system = Y()
        self.failure_count = 0

    def perform_transactions(self):
        users = ['user1', 'user2', 'user3']
        for u in users:
            self.main_system.create_acc(u)
            self.main_system.operation(u, random.randint(100, 500), 'D')
            self.main_system.operation(u, random.randint(50, 250), 'W')

        for _ in range(random.randint(1, 10)):
            u1, u2 = random.sample(users, 2)
            self.main_system.transfer(u1, u2, random.randint(20, 100))

        if random.random() > 0.7:
            self.failure_count += 1
            if self.failure_count > 3:
                self.main_system.system_lockdown = True

    def system_overview(self):
        if self.main_system.system_lockdown:
            return "System in lockdown"
        else:
            return self.main_system.complex_audit()


# Executing the system
sys_z = Z()
for _ in range(5):
    sys_z.perform_transactions()

print(sys_z.system_overview())
print(sys_z.main_system.audit_log())
sys_z.main_system.clear_logs()
