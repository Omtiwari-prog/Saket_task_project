import math
import matplotlib.pyplot as plt
print("This program will help you calculate the Equated Monthly Installment (EMI) for your loan based on the principal amount, annual interest rate, and loan tenure.\n")
loantype = input("Enter the type of loan (Home, Car, Personal): ")
print(f"You have selected {loantype} loan.")
def calculate_emi(principal, annual_interest_rate, tenure_years):
    monthly_interest_rate = annual_interest_rate / (12 * 100)  # Convert annual interest rate to monthly and percentage to decimal
    total_payments= tenure_years * 12  # Total number of monthly payments   
    
    if monthly_interest_rate == 0:  # If interest rate is 0, EMI is simply principal divided by total payments
        emi = principal / total_payments
    
    emi = (principal * monthly_interest_rate * math.pow(1 + monthly_interest_rate, total_payments)) / (math.pow(1 + monthly_interest_rate, total_payments) - 1)
    return emi

# example :
principal_amount = int(input("Enter the principal amount: "))  # Principal loan amount
annual_interest_rate = int(input("Enter the annual interest rate (in %): "))  # Annual interest rate in percentage
tenure_years = int(input("Enter the loan tenure (in years): "))  # Loan tenure in years
emi = calculate_emi(principal_amount, annual_interest_rate, tenure_years)
print(f"The EMI for a loan of {principal_amount} at an annual interest rate of {annual_interest_rate}% for {tenure_years} years is: {emi:.2f}")


# All Details of loan
def loan_details(principal, annual_interest_rate, tenure_years):
    details = {}
    details['Principal Amount'] = principal
    details['Annual Interest Rate'] = annual_interest_rate
    details['Tenure (Years)'] = tenure_years
    details['EMI'] = calculate_emi(principal, annual_interest_rate, tenure_years)
    details['Total Payment'] = details['EMI'] * tenure_years * 12  # Total payment over the loan tenure
    details['Total Interest'] = details['Total Payment'] - principal  # Total interest paid
    return details

# Example usage of loan_details function
loan_info = loan_details(principal_amount, annual_interest_rate, tenure_years)

#print loan details
print("\nLoan Details:")
for key, value in loan_info.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
    

#option to save the loan details to a text file
with open("loan_details.txt", "w") as f:
    f.write("Loan Details:\n")
    for key, value in loan_info.items():
        if isinstance(value, float):
            f.write(f"{key}: {value:.2f}\n")
        else:
            f.write(f"{key}: {value}\n")
        print("\nLoan details have been saved to 'loan_details.txt'.")
        
        # monthly payment schedule:
        
        def monthly_payment_schedule(principal, annual_interest_rate, tenure_years):
            monthly_interest_rate = annual_interest_rate / (12 * 100)
            total_payments = tenure_years * 12
            emi = calculate_emi(principal, annual_interest_rate, tenure_years)
            schedule = []
            remaining_principal = principal
            
            for month in range(1, total_payments + 1):
                interest_payment = remaining_principal * monthly_interest_rate
                principal_payment = emi - interest_payment
                remaining_principal -= principal_payment
                
                schedule.append({
                    'Month': month,
                    'EMI': emi,
                    'Principal Payment': principal_payment,
                    'Interest Payment': interest_payment,
                    'Remaining Principal': remaining_principal if remaining_principal > 0 else 0
                })
                
            return schedule
        print("\nMonthly Payment Schedule:")
        payment_schedule = monthly_payment_schedule(principal_amount, annual_interest_rate, tenure_years)
        for entry in payment_schedule:
            print(f"Month {entry['Month']}: EMI = {entry['EMI']:.2f}, Principal = {entry['Principal Payment']:.2f}, Interest = {entry['Interest Payment']:.2f}, Remaining Principal = {entry['Remaining Principal']:.2f}")
    
    #Calculate emi for different interest rates and tenures
    def emi(principal,annual_intrest_rate,tenure_years):
        emi=calculate_emi(principal,annual_intrest_rate,tenure_years)
        return emi
    print("\nEMI for different interest rates and tenures:")
    interest_rates = [8, 79, 40, 21, 18]# Different annual interest rates
    tenures = [5, 10, 15, 20, 25]# Different loan tenures in years
    for rate in interest_rates:
        for tenure in tenures:
            emi_value = emi(principal_amount, rate, tenure)
            print(f"EMI for principal {principal_amount} at {rate}% interest for {tenure} years: {emi_value:.2f}")
            
# Down payment
down_payment =int(input("\n Enter the down payment amount"))
loan_amount = principal_amount -down_payment
print(f"down payment amount is {down_payment}")
print(f"loan amount is {loan_amount}")


labels = ['Principal Amount', 'Total Interest']
labels1 = [loan_info['Principal Amount'], loan_info['Total Interest']]
values = [loan_info['Principal Amount'], loan_info['Total Interest']]
plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'orange'])
plt.title('Loan Breakdown')
plt.ylabel('Amount')
plt.show()






