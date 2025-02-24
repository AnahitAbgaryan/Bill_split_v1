


def split_amount(expenses, participants):

    balances = {participant: 0 for participant in participants}
    
    for expense in expenses:
        payer = expense['payer']
        amount = expense['amount']
        category = expense['category']
        participants = expense['participants']
        
        
        share = amount / len(participants)
        

        for participant in participants:
            if participant != payer:
                balances[participant] += share  
                balances[payer] -= share    

    return balances


def calculate_settlement(balances):
    
    print("\n--- Settlement ---")
    for participant, balance in balances.items():
        if balance > 0:
            print(f"{participant} is owed {balance} AMD")
        elif balance < 0:
            print(f"{participant} owes {-balance} AMD")
        else:
            print(f"{participant} has a balanced account.")