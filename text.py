#This draws a line with a number of dashes correlating to the number passed in through 'length'
'''
def make_line(length):
    return f'+' + ('-' * length) + '+'

print(make_line(9))
'''

'''import math
#need to write a program as a function to track of the spread of infection through an animal population based on population, initial infected, rate of spread of the infection
def simulate_infection(population, initial_infected, r_number):
    population = int(population)
    initial_infected = int(initial_infected)
    r_number = float(r_number)

    days = 1
    deceased = 0
    currently_infected = initial_infected


    while population > 0 and currently_infected > 0:
        print(f'It is day {days} the total population is {max(0, population):,} and there are {currently_infected:,} infected')
        
        population -= currently_infected
        deceased += currently_infected

        newly_infected = math.ceil(currently_infected * r_number)
        currently_infected = min(newly_infected, population)

        days += 1
        
simulate_infection(1000000, 1000, 1.1)'''

### UNIT 2: TODO 7
### implement the simulate_account_balance function. The function has the following parameters:
# init_principal: A float indicating the initial principal balance.
# acc_rate: A float indicating the interest rate per year (e.g., 0.05 for 5%).
# acc_cmp_freq: An int indicating the number of times interest is applied per year.
# setup_fee: A float indicating the amount of dollars that is deduced from the init_principal when the account is set up (you only deduct once).
# years: An int indicating the number of years for which we would like to run the report.
# Based on the provided arguments, the function will print one or more lines each of which displays two values - year number (starting from 2) and current balance on the account - separated by a space.

'''import math
def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    #need to check for frequency to then do Pert fmla
    
    principal_after_fee = init_principal - setup_fee
    for even_year_princ in range(2, years + 2, 2):
        if acc_cmp_freq == 0:
            balance = principal_after_fee * math.exp(acc_rate * even_year_princ)
            print(f'{even_year_princ} {balance:.2f}')
        else:
            balance =principal_after_fee * (1 + acc_rate/acc_cmp_freq) ** (acc_cmp_freq * even_year_princ)
            print(f'{even_year_princ} {balance:.2f}')
        
simulate_account_balance(10000.00, 0.025, 12, 25.00, 10)
'''
