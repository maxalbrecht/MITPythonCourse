def End_of_Year_Balance(balance, annualInterestRate, monthlyPaymentRate):
    """
    The following gives the remaining balance after 12 months on a credit
    card, given an initial balance, an annual interest rate, and 
    a monthly rate.
    ###
    balance - the outstanding balance on the credit card
    annualInterestRate - annual itnerest rate as a decimal
    montlyPaymentRate - minimum monthly payment rate as a decimal
    """
    months_left = 12
    while months_left > 0:
        balance = (
            (
                balance
                -(
                    balance
                    * monthlyPaymentRate
                 )
                
            )
            *(
                1
                +((annualInterestRate/12.0))
            )
            
        )
        months_left -= 1
    print(round(balance,2))

def Min_Payment_to_Pay_off_Card(balance, annualInterestRate):
    months_left = 12
    while months_left > 0:
        balance = (
                balance
                *(
                1
                +((annualInterestRate/12.0))
            )
            
        )
        months_left -= 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    