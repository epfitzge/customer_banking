# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    user_balance = input("Please enter the balance of your savings account ($): ")
    user_interest = input("Please enter the interest rate on your savings account (%): ")
    user_maturity = input("Please enter the number of months you will have your savings account: ")

    user_balance = float(user_balance)
    user_interest = float(user_interest)
    user_maturity = int(user_maturity)
    
       
    # Call the create_savings_account function and pass the variables from the user.
    new_account_balance, interest_earned = create_savings_account(user_balance, user_interest, user_maturity)
    

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"You have earned ${interest_earned:.2f} in interest on your savings account, and your new account balance is ${new_account_balance:.2f}")
    

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    user_cd_balance = input("Please enter the balance of your CD account ($): ")
    user_cd_interest = input("Please enter the interest rate on your CD account (%): ")
    user_cd_maturity = input("Please enter the number of months until your CD account maturity: ")

    user_cd_balance = float(user_cd_balance)
    user_cd_interest = float(user_cd_interest)
    user_cd_maturity = int(user_cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    new_cd_balance, interest_earned = create_cd_account(user_cd_balance, user_cd_interest, user_cd_maturity)


    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"You have earned ${interest_earned:.2f} in interest on your CD account, and your new account balance is ${new_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()