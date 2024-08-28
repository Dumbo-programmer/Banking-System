import random
import string
import datetime

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
        'category': random.choice(['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Travel', 'Savings', 'Miscellaneous', 'Health', 'Investments', 'Education', 'Business', 'Charity', 'Gifts', 'Insurance', 'Taxes', 'Subscriptions']),
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
for cat in ['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Travel', 'Savings', 'Miscellaneous', 'Investments', 'Education', 'Business', 'Charity', 'Gifts', 'Insurance', 'Taxes', 'Subscriptions']:
    budgets[cat] = randFloat(1000, 5000)

goals = {}
for goal in ['Vacation', 'Emergency Fund', 'New Car', 'Home Renovation', 'Gadget Upgrade', 'Retirement', 'Education Fund', 'Charitable Donations', 'Pet Fund', 'Wedding Fund']:
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

def expenseCategorizationAnalysis():
    # Analyze how expenses are distributed across categories
    category_expenses = {}
    for t in transList:
        if t['category'] not in category_expenses:
            category_expenses[t['category']] = 0
        category_expenses[t['category']] += t['amount']
    return category_expenses

def investmentDiversificationChecker():
    # Check if investments are well-diversified
    investments = {'Stocks': 5000, 'Bonds': 3000, 'Real Estate': 10000, 'Crypto': 2000, 'Precious Metals': 3000}
    total_investment = sum(investments.values())
    diversification = {k: (v / total_investment) * 100 for k, v in investments.items()}
    return diversification

def financialGoalAchievementTracker():
    # Track progress towards financial goals
    progress = {}
    for goal in goals:
        progress[goal] = (goals[goal] - random.randint(0, 10000))  # Simulating progress
    return progress

def monthlySpendingReports():
    # Generate a report of spending for each month
    monthly_report = {}
    for t in transList:
        month = t['date'].strftime('%Y-%m')
        if month not in monthly_report:
            monthly_report[month] = 0
        monthly_report[month] += t['amount']
    return monthly_report

def debtReductionStrategy():
    # Strategy to reduce debt based on available balance and interest rates
    total_debt = 10000  # Example value
    available_balance = viewBalance()
    if available_balance > total_debt:
        strategy = 'Pay off debt in full.'
    else:
        strategy = 'Pay minimum payments and allocate any extra funds towards debt.'
    return strategy

def annualTaxPreparationAssistant():
    # Assist with annual tax preparation
    tax_estimation = estimateTaxes()
    tax_deductions = {
        'Charitable Donations': sum(t['amount'] for t in transList if t['category'] == 'Charity'),
        'Medical Expenses': sum(t['amount'] for t in transList if t['category'] == 'Health'),
        'Mortgage Interest': 1200  # Example value
    }
    return {
        'Estimated Taxes': tax_estimation,
        'Tax Deductions': tax_deductions
    }


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
        'Loan Payment Tracker': trackLoanPayments(),
        'Debt Payoff Strategy': planDebtPayoff(),
        'Mortgage Calculator': calculateMortgage(),
        'Holiday Fund Management': manageHolidayFund(),
        'Luxury Spending Tracker': trackLuxurySpending(),
        'Financial Stress Analyzer': analyzeFinancialStress(),
        'Weekly Financial Challenges': weeklyFinanceChallenges(),
        'Subscription Cancellation Alerts': cancelSubscriptionAlerts(),
        'Monthly Bill Calendar': billCalendar(),
        'Cash Flow Forecasting': forecastCashFlow(),
        'Real-Time Market Analysis': analyzeMarketTrends(),
        'Interactive Budget Reports': interactiveBudgetReports(),
        'Expense Categorization Analysis': expenseCategorizationAnalysis(),
        'Investment Diversification Checker': investmentDiversificationChecker(),
        'Financial Goal Achievement Tracker': financialGoalAchievementTracker(),
        'Monthly Spending Reports': monthlySpendingReports(),
        'Debt Reduction Strategy': debtReductionStrategy(),
        'Annual Tax Preparation Assistant': annualTaxPreparationAssistant()
        
            }

def main():
    while True:
        print("\nFinancial Management System")
        print("1. View Accounts")
        print("2. Add Transaction")
        print("3. View Budgets")
        print("4. Add Budget")
        print("5. View Goals")
        print("6. Add Goal")
        print("7. View Balance")
        print("8. Check Budgets")
        print("9. View Transactions")
        print("10. Generate Income Prediction")
        print("11. Collaborative Budgets")
        print("12. Calculate Loan Payment")
        print("13. Expense Classification")
        print("14. Manage Crypto Assets")
        print("15. Detect Fraud")
        print("16. Calculate Debt Consolidation")
        print("17. Get Financial Advice")
        print("18. Custom Dashboards")
        print("19. Personal News Feed")
        print("20. Round Up Savings")
        print("21. Automatic Investment Management")
        print("22. Financial Lockdown")
        print("23. Micro Investment")
        print("24. Goal Tracking")
        print("25. Business Expenditure Tracking")
        print("26. Emergency Funds Tracker")
        print("27. Investment Portfolio Analysis")
        print("28. Expense Categorization Analysis")
        print("29. Investment Diversification Checker")
        print("30. Financial Goal Achievement Tracker")
        print("31. Monthly Spending Reports")
        print("32. Debt Reduction Strategy")
        print("33. Annual Tax Preparation Assistant")
        print("34. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for acc_id, acc_info in accounts.items():
                print(f"Account ID: {acc_id}, Balance: ${acc_info['balance']:.2f}")
        elif choice == '2':
            acc_id = input("Enter account ID: ")
            if acc_id in accounts:
                trans = randTrans()  # Example transaction
                addTransaction(acc_id, trans)
                print("Transaction added.")
            else:
                print("Account ID not found.")
        elif choice == '3':
            print(viewBudgets())
        elif choice == '4':
            category = input("Enter budget category: ")
            amount = float(input("Enter budget amount: "))
            addBudget(category, amount)
            print("Budget updated.")
        elif choice == '5':
            print(viewGoals())
        elif choice == '6':
            goal_name = input("Enter goal name: ")
            amount = float(input("Enter goal amount: "))
            addGoal(goal_name, amount)
            print("Goal added.")
        elif choice == '7':
            print(f"Total Balance: ${viewBalance():.2f}")
        elif choice == '8':
            print(checkBudgets())
        elif choice == '9':
            acc_id = input("Enter account ID: ")
            if acc_id in accounts:
                transactions = viewTransactions(acc_id)
                for trans in transactions:
                    print(trans)
            else:
                print("Account ID not found.")
        elif choice == '10':
            print(incomePrediction())
        elif choice == '11':
            print(collaborativeBudgets())
        elif choice == '12':
            loan_amount = float(input("Enter loan amount: "))
            interest_rate = float(input("Enter interest rate (%): "))
            term_years = int(input("Enter term (years): "))
            print(f"Monthly Payment: ${calcLoan(loan_amount, interest_rate, term_years):.2f}")
        elif choice == '13':
            transaction = randTrans()
            print(f"Transaction Classification: {expenseClassification(transaction)}")
        elif choice == '14':
            print(manageCrypto())
        elif choice == '15':
            transaction = randTrans()
            print(f"Fraud Detection: {'Suspicious' if detectFraud(transaction) else 'Not Suspicious'}")
        elif choice == '16':
            debts = [float(d) for d in input("Enter debts (comma separated): ").split(',')]
            print(f"Debt Consolidation: ${calculateDebtConsolidation(debts):.2f}")
        elif choice == '17':
            print(advancedFinancialAdvisor())
        elif choice == '18':
            print(customDashboards())
        elif choice == '19':
            print(personalNewsFeed())
        elif choice == '20':
            roundUpSavings()
            print("Round-Up Savings processed.")
        elif choice == '21':
            print(automaticInvestmentManagement())
        elif choice == '22':
            lock_time = input("Enter lock time (e.g., '2025-01-01'): ")
            print(financialLockdown(lock_time))
        elif choice == '23':
            amount = float(input("Enter micro-investment amount: "))
            print(microInvest(amount))
        elif choice == '24':
            print(goalTracking())
        elif choice == '25':
            print(businessExpenditureTracking())
        elif choice == '26':
            print(emergencyFundsTracker())
        elif choice == '27':
            print(investmentPortfolioAnalysis())
        elif choice == '28':
            print(expenseCategorizationAnalysis())
        elif choice == '29':
            print(investmentDiversificationChecker())
        elif choice == '30':
            print(financialGoalAchievementTracker())
        elif choice == '31':
            print(monthlySpendingReports())
        elif choice == '32':
            print(debtReductionStrategy())
        elif choice == '33':
            print(annualTaxPreparationAssistant())
        elif choice == '34':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()