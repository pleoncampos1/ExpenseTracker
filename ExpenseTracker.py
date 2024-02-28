
"""
Created on Tue Feb 27 20:49:21 2024

@author: Piero
"""

import pandas as pd

class FinanceTracker:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['Date', 'Description','Amount'])
        
    def add_transaction(self, date, description, amount):
        new_transaction = pd.DataFrame([[date, description, amount]], columns=['Date', 'Description', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
        
#example usage
tracker = FinanceTracker()
tracker.add_transaction('2024-02-27', 'Groceries', -50)

#print out the results
print("Transactions:")
print(tracker.transactions)
