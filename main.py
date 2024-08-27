import random
import string
import datetime

def randStr(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def randDate():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    return start_date + (end_date - start_date) * random.random()

def randFloat(minV, maxV):
    return round(random.uniform(minV, maxV), 2)

def randTrans():
    return {
        'id': randStr(8),
        'date': randDate(),
        'amount': randFloat(-1000, 1000),
        'category': random.choice(['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Travel', 'Savings', 'Miscellaneous', 'Health', 'Investments', 'Education', 'Business', 'Charity']),
        'description': randStr(20)
    }

transList = []
for _ in range(700):
    transList.append(randTrans())

accounts = {}
for _ in range(7):
    acct_id = randStr(6)
    accounts[acct_id] = {'balance': randFloat(1000, 20000), 'transactions': []}
    for trans in transList:
        accounts[acct_id]['transactions'].append(trans)

budgets = {}
for cat in ['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Travel', 'Savings', 'Miscellaneous', 'Investments', 'Education', 'Business', 'Charity']:
    budgets[cat] = randFloat(1000, 5000)

goals = {}
for goal in ['Vacation', 'Emergency Fund', 'New Car', 'Home Renovation', 'Gadget Upgrade', 'Retirement']:
    goals[goal] = randFloat(5000, 50000)

receipts = {}
for _ in range(150):
    rec_id = randStr(8)
    receipts[rec_id] = randStr(30)

def addTransaction(acc, t):
    accounts[acc]['transactions'].append(t)

def viewTransactions(acc):
    return accounts[acc]['transactions']

def addBudget(cat, amt):
    budgets[cat] = amt

def viewBudgets():
    return budgets

def addGoal(name, amt):
    goals[name] = amt

def viewGoals():
    return goals

def viewBalance():
    total_balance = 0
    for account in accounts:
        total_balance += accounts[account]['balance']
    return total_balance

def checkBudgets():
    over_budget = {}
    for cat in budgets:
        spent = sum(t['amount'] for acc in accounts for t in accounts[acc]['transactions'] if t['category'] == cat)
        if spent > budgets[cat]:
            over_budget[cat] = spent - budgets[cat]
    return over_budget

def randomizeGoals():
    for g in goals:
        goals[g] += randFloat(-500, 500)
    return goals

def specialSavings(t):
    if t['amount'] < 0:
        rounded = round(t['amount']) - t['amount']
        if 'Savings' not in budgets:
            budgets['Savings'] = 0
        budgets['Savings'] += rounded

def incomePrediction():
    predict = {}
    for cat in budgets:
        predict[cat] = randFloat(1000, 3000)
    return predict

def collaborativeBudgets():
    shared = sum(budgets.values()) * 1.15
    return shared

def calcLoan(loan_amount, interest_rate, term_years):
    monthly_payment = loan_amount * (interest_rate / 100) / (1 - (1 + interest_rate / 100) ** -term_years)
    return monthly_payment

def expenseClassification(t):
    if t['amount'] > 0:
        return 'Income'
    else:
        return 'Expense'

def manageCrypto():
    crypto_assets = {'Bitcoin': 0.4, 'Ethereum': 1.8, 'Litecoin': 10.0, 'Dogecoin': 500.0}
    return crypto_assets

def detectFraud(t):
    suspicious = random.choice([True, False])
    return suspicious

def calculateDebtConsolidation(debts):
    return sum(debts) / len(debts)

def advancedFinancialAdvisor():
    advice = {
        'Save more': "Consider saving an additional 10% each month.",
        'Invest wisely': "Review your investment portfolio for better diversification.",
        'Debt reduction': "Focus on reducing high-interest debt first.",
        'Crypto Investments': "Consider allocating a small percentage to cryptocurrency."
    }
    return advice

def customDashboards():
    dbs = {'basic': {'view': 'Summary', 'widgets': ['balance', 'transactions', 'goals']}}
    dbs['advanced'] = {'view': 'Full Overview', 'widgets': ['budgets', 'crypto', 'advisor', 'loan calculator', 'expense tracker']}
    dbs['custom'] = {'view': 'User-Defined', 'widgets': ['income prediction', 'business tracking', 'emergency funds', 'investment analysis']}
    return dbs

def personalNewsFeed():
    return ['Crypto prices surge!', 'Stock market hits record high.', 'Savings account interest rates are declining.', 'Real estate prices on the rise.']

def roundUpSavings():
    for acc in accounts:
        for t in accounts[acc]['transactions']:
            specialSavings(t)

def automaticInvestmentManagement():
    investments = {'Stocks': 5000, 'Bonds': 3000, 'Real Estate': 10000, 'Crypto': 2000, 'Precious Metals': 3000}
    investments['Total'] = sum(investments.values())
    return investments

def financialLockdown(lock_time):
    return f"Financial transactions are locked until {lock_time}"

def microInvest(amount):
    return f"Invested ${amount} in micro-investment platforms."

def goalTracking():
    progress = {}
    for goal in goals:
        progress[goal] = random.randint(10, 90)
    return progress

def businessExpenditureTracking():
    total_business_expenses = sum(t['amount'] for t in transList if t['category'] == 'Business')
    return total_business_expenses

def emergencyFundsTracker():
    return f"Emergency funds are at ${goals['Emergency Fund']}."

def investmentPortfolioAnalysis():
    portfolio = {'Stocks': 4000, 'Bonds': 2000, 'Real Estate': 8000, 'Crypto': 1500, 'Precious Metals': 2000}
    return portfolio

def interactiveFinanceDashboard():
    return {
        'Dashboards': customDashboards(),
        'Advisor': advancedFinancialAdvisor(),
        'Crypto': manageCrypto(),
        'Income Prediction': incomePrediction(),
        'Collaborative Budgeting': collaborativeBudgets(),
        'Debt Management': calculateDebtConsolidation([2000, 5000, 3000]),
        'Loan Calculator': calcLoan(10000, 5, 15),
        'Expense Classification': [expenseClassification(t) for t in transList],
        'Financial Lockdown': financialLockdown('2025-01-01'),
        'Business Tracking': businessExpenditureTracking(),
        'Goal Progress': goalTracking(),
        'Investment Analysis': investmentPortfolioAnalysis(),
        'Emergency Funds': emergencyFundsTracker(),
        'Round-Up Savings': roundUpSavings(),
        'Investment Management': automaticInvestmentManagement(),
        'News Feed': personalNewsFeed(),
        'Fraud Detection': detectFraud(randTrans()),
        'Micro Investments': microInvest(100),
        'Precious Metals Tracking': trackPreciousMetals(),
        'Daily Transaction Report': dailyTransactionReport(),
        'Tax Estimation': estimateTaxes(),
        'Retirement Planning': retirementPlan(),
        'Education Fund Tracker': educationFundTracking(),
        'Monthly Budget Planner': monthlyBudgetPlanner(),
        'Holiday Spending Tracker': holidaySpendingTracker(),
        'Charity Contributions': trackCharityContributions(),
        'Subscription Management': manageSubscriptions(),
        'Carbon Footprint Tracker': carbonFootprintTracking(),
        'Crowdfunding Contributions': trackCrowdfunding(),
        'Insurance Policy Tracker': manageInsurancePolicies(),
        'Credit Score Estimation': estimateCreditScore(),
        'Loan Comparison Tool': compareLoans(),
        'Family Budgeting Tool': manageFamilyBudget(),
        'Career Progression Tracker': careerTracking(),
        'Household Inventory Management': manageInventory(),
        'Gifting Planner': planGifts(),
        'Pet Expenses Tracker': managePetExpenses(),
        'Vehicle Maintenance Schedule': manageVehicleMaintenance(),
        'Home Improvement Tracker': trackHomeImprovements(),
        'Health Savings Account Tracker': trackHealthSavings(),
        'Fitness Expenses Tracker': manageFitnessExpenses(),
        'Hobby Budget Tracker': manageHobbyBudget(),
        'Vacation Planning Tool': planVacation(),
        'Daily Expense Challenges': dailyChallenges(),
        'Automated Expense Analysis': analyzeExpenses(),
        'Interest Rate Optimizer': optimizeInterestRates(),
        'Donation Tracker': manageDonations(),
        'Emergency Contact List': manageEmergencyContacts(),
        'Daily Reminders': setDailyReminders(),
        'Monthly Spending Overview': monthlySpendingOverview(),
        'Weekly Savings Goal Tracker': weeklySavingsGoals(),
        'Customized Investment Portfolio': customizePortfolio(),
        'Personalized Finance Tips': personalizedFinanceTips(),
        'Spending Pattern Analysis': analyzeSpendingPatterns(),
        'Debt Repayment Schedule': debtRepaymentSchedule(),
        'Investment Growth Projection': projectInvestmentGrowth(),
        'Savings Account Comparison': compareSavingsAccounts(),
        'Budget Adjustment Alerts': budgetAdjustmentAlerts(),
        'Personalized Loan Offers': personalizedLoanOffers()
    }
