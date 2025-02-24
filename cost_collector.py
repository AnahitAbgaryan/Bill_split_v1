def expenses_input():
    expenses = []
    participants = []
    
    num_expenses = int(input("Enter the number of expenses: "))
    
    for i in range(num_expenses):
        payer = input(f"Enter the payer's name for expense N{i + 1}: ")
        amount = float(input(f"Enter the total amount for expense  N{i + 1}: "))
        category = input(f"Enter the category of expense N{i + 1}: ")
        participants_input = input(f"Enter the names of participants for expense N{i + 1} (comma separated): ")
        participants_list = participants_input.split(",")
        
        expenses.append({
            'payer': payer,
            'amount': amount,
            'category': category,
            'participants': participants_list
        })
        
        for person in participants_list:
            if person not in participants:
                participants.append(person)
    
    return expenses, participants