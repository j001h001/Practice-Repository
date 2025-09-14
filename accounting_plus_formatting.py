import math
#for making a fancy line
def make_line(length):
    return "+" + "-" * length + "+"

#for adding the formatting to the body of the function itself
# TODO 3: Place your code for `make_field` here
def make_field(content, length):
    content = str(content)
    spacing = (content).rjust(length)
    return f'|{spacing} |'

#simulating account balance over a fixed period of time every even numbered year
def simulate_account_balance_pp(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    """
    Simulates and prints the account balance at even-year intervals.

    Args:
        init_principal (float): The initial principal balance.
        acc_rate (float): The interest rate per year (e.g., 0.05 for 5%).
        acc_cmp_freq (int): The number of times interest is applied per year.
                             If 0, interest is compounded continuously.
        setup_fee (float): A one-time fee deducted from the principal at the start.
        years (int): The total number of years for the report.
    """
    principal_after_fee = init_principal - setup_fee
    
    #Setup the table formatting
    YEAR_WIDTH = 5
    BALANCE_WIDTH = 14

    YEAR_LINE_WIDTH = 6
    BALANCE_LINE_WIDTH = 15

    year_header = make_field("Year", YEAR_WIDTH)
    balance_header = make_field("Balance", BALANCE_WIDTH)

    year_line = make_line(YEAR_LINE_WIDTH)
    balance_line = make_line(BALANCE_LINE_WIDTH)

    #Create the header structure
    print(year_line + balance_line)
    print(year_header + balance_header)
    print(year_line + balance_line)

    # Loop through even years up to the total number of years specified.
    # The range (2, years + 1, 2) ensures we start at year 2 and step by 2.
    for year in range(2, years + 1, 2):
        if acc_cmp_freq == 0:
            # Continuous compounding case
            balance = principal_after_fee * math.exp(acc_rate * year)
        else:
            # Standard compound interest formula
            balance = principal_after_fee * (1 + acc_rate / acc_cmp_freq) ** (acc_cmp_freq * year)
        
        # Round the balance to 2 decimal places as per the hint.
        rounded_balance = round(balance, 2)
        
        # Print the year and the rounded balance. The default string conversion
        # will now handle the formatting as required by the tester.
        year_field = make_field(year, YEAR_WIDTH)
        balance_field = make_field(f'${rounded_balance:,.2f}',BALANCE_WIDTH)
        print(year_field + balance_field)

    print(year_line + balance_line)
# Call the function to produce the required output.
simulate_account_balance_pp(10000.00, 0.025, 12, 25.00, 10)