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
        'Expense Categorization Tool': categorizeExpenses(),
        'Automated Bill Payments': automateBillPayments(),
        'Debt Snowball Tool': debtSnowballStrategy(),
        'Home Loan Prequalification': prequalifyHomeLoan(),
        'Student Loan Refinancing Tool': refinanceStudentLoans(),
        'Family Vacation Budgeting': planFamilyVacationBudget(),
        'Side Income Tracking': trackSideIncome(),
        'Future Value Estimator': estimateFutureValue(),
        'Retirement Savings Projection': projectRetirementSavings(),
        'Emergency Budget Planning': planEmergencyBudget(),
        'Annual Spending Review': reviewAnnualSpending(),
        'Lifestyle Inflation Calculator': calculateLifestyleInflation(),
        '401(k) Contribution Calculator': calculate401kContributions(),
        'Self-Employment Tax Estimator': estimateSelfEmploymentTax(),
        'Daily Cash Flow Management': manageDailyCashFlow(),
        'Online Shopping Tracker': trackOnlineShopping(),
        'Refund Tracker': manageRefunds(),
        'Home Energy Cost Calculator': calculateHomeEnergyCosts(),
        'Weekly Savings Challenge': weeklySavingsChallenges(),
        'Charitable Giving Strategy': planCharitableGiving(),
        'Business Travel Expenses Tracker': trackBusinessTravelExpenses(),
        'Medical Expense Planner': planMedicalExpenses(),
        'Education Cost Estimator': estimateEducationCosts(),
        'Insurance Premium Calculator': calculateInsurancePremium(),
        'Household Chore Budgeting': budgetHouseholdChores(),
        'Investment Rebalancing Tool': rebalanceInvestments(),
        'High-Interest Debt Alert': alertHighInterestDebt(),
        'Spousal Budget Collaboration': collaborateSpousalBudget(),
        'Flexible Spending Account Tracker': trackFSA(),
        'Childcare Expense Tracker': manageChildcareExpenses(),
        'Subscription Renewal Alerts': alertSubscriptionRenewal(),
        'Shared Expense Splitter': splitSharedExpenses(),
        'Stock Option Portfolio Tracker': trackStockOptions(),
        'Recurring Payment Tracker': manageRecurringPayments(),
        'Property Tax Estimator': estimatePropertyTax(),
        'Future Budget Forecasting': forecastFutureBudget(),
        'Annual Financial Planning Tool': planAnnualFinances(),
        'Debt-to-Income Ratio Calculator': calculateDTIRatio(),
        'Work-Life Balance Tracker': trackWorkLifeBalance(),
        'Charitable Giving Match Calculator': matchCharitableGiving(),
        'Crowdfunding Investment Tracker': trackCrowdfundingInvestments(),
        'Salary Negotiation Tool': negotiateSalary(),
        'Business Profit Margin Calculator': calculateProfitMargin(),
        'Freelance Income Estimator': estimateFreelanceIncome(),
        'Event Budgeting Tool': planEventBudget(),
        'Personal Financial Snapshot': financialSnapshot(),
        'Online Subscription Budgeting': budgetOnlineSubscriptions(),
        'Family Financial Goals Tracker': trackFamilyFinancialGoals(),
        'Charity Fundraising Tracker': trackCharityFundraising(),
        'Vehicle Lease Calculator': calculateLeaseCosts(),
        'Rental Income Tracker': trackRentalIncome(),
        'Dividends Tracker': manageDividends(),
        'Mobile Payment Tracker': trackMobilePayments(),
        'Debt Avalanche Tool': debtAvalancheStrategy(),
        'Financial Accountability Partner': partnerAccountability(),
        'Peer-to-Peer Lending Tracker': trackP2PLending(),
        'Luxury Item Budgeting': budgetLuxuryItems(),
        'Family Financial Meeting Planner': planFamilyFinanceMeetings(),
        'Financial Goals Accountability': goalAccountability(),
        'Virtual Assistant Financial Tracker': trackVirtualAssistant(),
        'Long-Term Financial Vision Board': createVisionBoard(),
        'Emergency Cash Stash Planner': planEmergencyCash(),
        'Pet Insurance Premium Calculator': calculatePetInsurance(),
        'Side Hustle Budgeting': budgetSideHustle(),
        'Local Business Investment Tracker': trackLocalBusinessInvestments(),
        'Remote Work Expense Tracker': trackRemoteWorkExpenses(),
        'Personal Finance Podcast': manageFinancePodcast(),
        'Group Financial Challenges': manageGroupFinanceChallenges(),
        'Shared Goal Tracker': trackSharedGoals(),
        'Real Estate Investment Planning Tool': planRealEstateInvestments(),
        'Personal Shopping List Tracker': trackShoppingList(),
        'Luxury Travel Budgeting Tool': budgetLuxuryTravel(),
        'Professional Development Budgeting': budgetProfessionalDevelopment(),
        'Shared Wallet': manageSharedWallet(),
        'Cash Flow Analyzer': analyzeCashFlow(),
        'Advanced Tax Planning Tool': planAdvancedTaxes(),
        'Rent vs. Buy Calculator': calculateRentVsBuy(),
        'Investment Club Manager': manageInvestmentClub(),
        'Debt Forgiveness Tracker': trackDebtForgiveness(),
        'Time Off Budgeting Tool': budgetTimeOff(),
        'Vacation Savings Plan': saveForVacation(),
        'Retirement Income Estimator': estimateRetirementIncome(),
        'Self-Care Budgeting Tool': budgetSelfCare(),
        'Debt Consolidation Tracker': trackDebtConsolidation(),
        'Job Offer Comparison Tool': compareJobOffers(),
        'Side Business Budgeting': budgetSideBusiness(),
        'Financial Emergency Planning Tool': planFinancialEmergencies(),
        'Real-Time Expense Alerts': alertRealTimeExpenses(),
        'Financial Mentor Program': manageFinanceMentor(),
        'Annual Bonus Budgeting': budgetAnnualBonus(),
        'Community Fundraising Tracker': trackCommunityFundraising(),
        'Financial Trend Analyzer': analyzeFinanceTrends(),
        'Work-From-Home Budgeting Tool': budgetWorkFromHome(),
        'Mental Health Budgeting Tool': budgetMentalHealth(),
        'Short-Term Rental Income Estimator': estimateShortTermRentalIncome(),
        'Annual Charity Giving Planner': planAnnualCharityGiving(),
        'Entrepreneurship Budgeting Tool': budgetEntrepreneurship(),
        'Disaster Recovery Fund Tracker': trackDisasterRecoveryFund(),
        'Crowdfunding Campaign Manager': manageCrowdfundingCampaigns(),
        'Holiday Gifting Budget': budgetHolidayGifts(),
        'Personal Debt Recovery Tracker': trackDebtRecovery(),
        'Financial Independence Planner': planFinancialIndependence(),
        'Pet Care Budget Planner': planPetCareBudget(),
        'Subscription Budget Optimization Tool': optimizeSubscriptionBudget(),
        'Advanced Bill Payment Scheduler': scheduleAdvancedBillPayments(),
        'Crowdfunding Project Analysis': analyzeCrowdfundingProjects(),
        'Luxury Good Purchase Tracker': trackLuxuryGoodPurchases(),
        'Life Event Budgeting Tool': budgetLifeEvents(),
        'Online Course Budget Planner': planOnlineCourses(),
        'Professional Networking Budgeting': budgetNetworking(),
        'Child Education Savings Tracker': trackChildEducationSavings(),
        'Remote Work Savings Estimator': estimateRemoteWorkSavings(),
        'Emergency Medical Fund Tracker': trackEmergencyMedicalFunds(),
        'Luxury Vehicle Purchase Planner': planLuxuryVehiclePurchase(),
        'Personal Wealth Management Tool': managePersonalWealth(),
        'Retirement Community Savings Planner': planRetirementCommunitySavings(),
        'Community Investment Tracker': trackCommunityInvestments(),
        'Future Tax Liability Estimator': estimateFutureTaxLiability(),
        'Financial Behavior Analysis Tool': analyzeFinancialBehavior(),
        'Medical Expense Tax Deduction Estimator': estimateMedicalTaxDeductions(),
        'Debt Repayment Snowball Planner': planDebtRepaymentSnowball(),
        'Pet Care Savings Estimator': estimatePetCareSavings(),
        'Custom Financial Goal Tracker': trackCustomFinancialGoals(),
        'Home Energy Efficiency Planner': planHomeEnergyEfficiency(),
        'Professional Liability Insurance Estimator': estimateProfessionalLiabilityInsurance(),
        'Small Business Financing Tool': planSmallBusinessFinancing(),
        'Self-Employed Health Insurance Tracker': trackSelfEmployedHealthInsurance(),
        'Group Subscription Budgeting Tool': budgetGroupSubscriptions(),
        'Extended Family Financial Planner': planExtendedFamilyFinances(),
        'Comprehensive Income Analysis Tool': analyzeComprehensiveIncome(),
        'Environmental Impact Budgeting Tool': budgetEnvironmentalImpact(),
        'Charitable Trust Fund Tracker': trackCharitableTrustFund(),
        'Personal Health and Wellness Budgeting Tool': budgetHealthAndWellness(),
        'Startup Fundraising Tracker': trackStartupFundraising(),
        'Social Impact Investment Tracker': trackSocialImpactInvestments(),
        'Real-Time Expense Sharing Tool': shareRealTimeExpenses(),
        'Rental Property Renovation Planner': planRentalPropertyRenovation(),
        'Health Savings Contribution Calculator': calculateHealthSavingsContributions(),
        'Home Office Tax Deduction Estimator': estimateHomeOfficeTaxDeductions(),
        'Vehicle Insurance Deductible Planner': planVehicleInsuranceDeductibles(),
        'Luxury Lifestyle Budget Planner': planLuxuryLifestyleBudget(),
        'Tax-Advantaged Investment Tracker': trackTaxAdvantagedInvestments(),
        'Business Expansion Financing Tool': planBusinessExpansionFinancing(),
        'Home-Based Business Expense Tracker': trackHomeBasedBusinessExpenses(),
        'Luxury Property Investment Planner': planLuxuryPropertyInvestments(),
        'Personal Travel Expense Sharing Tool': sharePersonalTravelExpenses(),
        'Professional Membership Fee Tracker': trackProfessionalMembershipFees(),
        'Vehicle Purchase Financing Tool': planVehiclePurchaseFinancing(),
        'Luxury Vacation Club Tracker': trackLuxuryVacationClub(),
        'Cryptocurrency Tax Liability Estimator': estimateCryptocurrencyTaxLiability(),
        'Group Vacation Budgeting Tool': budgetGroupVacation(),
        'Home Improvement Tax Deduction Estimator': estimateHomeImprovementTaxDeductions(),
        'Luxury Fitness Membership Tracker': trackLuxuryFitnessMembership(),
        'Environmental Conservation Fund Tracker': trackConservationFund(),
        'Luxury Event Planning Tool': planLuxuryEvents(),
        'Small Business Sustainability Planner': planSmallBusinessSustainability(),
        'Real Estate Tax Planning Tool': planRealEstateTaxes(),
        'Online Marketplace Income Tracker': trackMarketplaceIncome(),
        'Charity Walk/Run Fundraising Tracker': trackCharityWalkRunFundraising(),
        'Personal Finance Research Tool': researchPersonalFinance(),
        'Vacation Rental Income Estimator': estimateVacationRentalIncome(),
        'Group Investment Portfolio Tracker': trackGroupInvestments(),
        'Future Retirement Community Planner': planFutureRetirementCommunity(),
    }