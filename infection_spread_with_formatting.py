import math

def make_line(length):
    return "+" + "-" * length + "+"

# TODO 3: Place your code for `make_field` here
def make_field(content, length):
    content = str(content)
    spacing = (content + ' ').rjust(length)
    return f'|{spacing}|'


#This is the function for the infected rates etc. the core calculation
## everything else is just fuckin formatting which is super annoying... lol
def simulate_infection_pp(population, initial_infected, r_number):
    population = int(population)
    initial_infected = int(initial_infected)
    r_number = float(r_number)

    days = 1
    deceased = 0
    currently_infected = initial_infected

    #Setup the table formatting
    DAY_WIDTH = 5
    POP_WIDTH = 12

    day_header = make_field("Day", DAY_WIDTH)
    pop_header = make_field("Population", POP_WIDTH)

    day_line = make_line(DAY_WIDTH)
    pop_line = make_line(POP_WIDTH)

    print(day_line + pop_line)
    print(day_header + pop_header)
    print(day_line + pop_line)

    while population > 0 or currently_infected > 0:
        day_field = make_field(days, DAY_WIDTH)
        pop_field = make_field(f'{population:,}', POP_WIDTH)
        print(day_field + pop_field)

        population -= currently_infected
        deceased += currently_infected

        newly_infected = math.ceil(currently_infected * r_number)
        currently_infected = min(newly_infected, population)

        days += 1

    final_day_field = make_field(days, DAY_WIDTH)
    final_pop_field = make_field(0, POP_WIDTH)
    print(final_day_field + final_pop_field)
    print(day_line + pop_line)
    
simulate_infection_pp(192023, 5, 1.411246411052212)