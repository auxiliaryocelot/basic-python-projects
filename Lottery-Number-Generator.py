####################################
#                                  #
# Lottery Ticket Number Generator  #
#                                  #
####################################

import random

### Ask the user for a selection

game_selection = int(input("""Which game would you like numbers for? Type "1" for Mega Millions, or "2" for Powerball: """))
mm_numbers = []
pb_numbers = []

### If user selects "1", generate 5 random numbers and a random Megaball number

if game_selection == 1:
    for m in range (5):
        mm_numbers.append(random.randint(1, 70))
    mm_numbers.sort()
    print(f'Mega Millions Numbers: {mm_numbers}')
    megaball = random.randint(1, 25)
    print(f"Megaball Number: {megaball}")

### If user selects "2", generate 5 random numbers and a random Powerball number

elif game_selection == 2:
    for p in range(5):
        pb_numbers.append(random.randint(1, 69))
    pb_numbers.sort()
    print(f"Powerball Numbers: {pb_numbers}")
    powerball = random.randint(1, 26)
    print(f"Powerball Number: {powerball}")

### If any other numbers are entered, error message displays

else:
    print("Incorrect input. Please try again.")


### Probably not the best way to keep the program from
### immediately closing, but I'm open to suggestions!

input("")
