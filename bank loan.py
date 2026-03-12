from datetime import datetime
import schedule
import time
import os
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

user = 'root'
password = '2005'
host = 'localhost'          
port = 3306                 
database = 'bankdb'

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

df = pd.read_csv(r"C:\Users\Dell\Documents\project 500.csv")


df = df[['age',
         'annual_income',
         'credit_score',
         'debt_to_income_ratio',
         'loan_amount',
         'interest_rate',
         'loan_term',
         'employment_status',
         'loan_paid_back']]

print(len(df))

def create_charts(df):

 os.makedirs("loan_reports", exist_ok=True)
 today = datetime.now().strftime('%Y%m%d')
 
#Loan Paid Back Count

 loan_counts = df['loan_paid_back'].value_counts()  
 labels = ['Paid Back', 'Not Paid Back']

 plt.figure(figsize=(6,4))
 plt.bar(labels, loan_counts, color='skyblue')
 plt.title("Loan Paid Back Count")
 plt.xlabel("Loan Status")
 plt.ylabel("Number of Customers")
 plt.savefig(f"loan_reports/loan_paid_back_count_{today}.png")
 plt.show()
 plt.close()


#Credit Score Distribution

 plt.figure(figsize=(6,4))
 plt.hist(df['credit_score'], bins=10, color='green', edgecolor='black')
 plt.title("Credit Score Distribution")
 plt.xlabel("Credit Score")
 plt.ylabel("Number of Customers")
 plt.savefig(f"loan_reports/credit_score_distribution_{today}.png")
 plt.show()
 plt.close()


#Annual Income vs Loan Amount

 plt.figure(figsize=(6,4))
 plt.scatter(df['annual_income'], df['loan_amount'], color='orange')
 plt.title("Income vs Loan Amount")
 plt.xlabel("Annual Income")
 plt.ylabel("Loan Amount")
 plt.savefig(f"loan_reports/income_vs_loan_{today}.png")
 plt.show()
 plt.close()

#Debt-to-Income Ratio Distribution

 plt.figure(figsize=(6,4))
 plt.hist(df['debt_to_income_ratio'], bins=10, color='red', edgecolor='black')
 plt.title("Debt-to-Income Ratio Distribution")
 plt.xlabel("Debt-to-Income Ratio")
 plt.ylabel("Number of Customers")
 plt.savefig(f"loan_reports/debt_to_income_distribution_{today}.png")
 plt.show()
 plt.close()


#Age Distribution

 plt.figure(figsize=(6,4))
 plt.hist(df['age'], bins=10, color='purple', edgecolor='black')
 plt.title("Age Distribution of Customers")
 plt.xlabel("Age")
 plt.ylabel("Number of Customers")
 plt.savefig(f"loan_reports/age_distribution_{today}.png")
 plt.show()
 plt.close()


# Average Interest Rate by Employment Status

 emp_interest = df.groupby("employment_status")["interest_rate"].mean()

 plt.figure(figsize=(6,4))
 plt.bar(emp_interest.index, emp_interest.values, color='blue')
 plt.title("Average Interest Rate by Employment Status")
 plt.xlabel("Employment Status")
 plt.ylabel("Average Interest Rate")
 plt.savefig(f"loan_reports/interest_by_employment_{today}.png")
 plt.show()
 plt.close()

print("All 6 plots are generated")
create_charts(df)

def bank_loan():
    create_charts(df)

schedule.every().day.at("18:00").do(bank_loan)

while True:
    schedule.run_pending()
    time.sleep(60)












































































