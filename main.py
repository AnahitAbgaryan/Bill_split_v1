from cost_collector import expenses_input
from cost_splitter import split_amount
from cost_splitter import calculate_settlement 



def bill_splitter():
    print("Bill Splitter Starts!")

    expenses, participants = expenses_input()

    balances = split_amount(expenses, participants)

    calculate_settlement(balances)


bill_splitter()
