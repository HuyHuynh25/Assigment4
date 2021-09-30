########################################################################
##
## CS 101 Lab
## Assignment 4
## Huynh Gia Huy - Jim Huynh
## hghydv@umsystem.edu
##
## PROBLEM : Create a gambling program that simulate a slot machine in Pierson Hall.
##
## ALGORITHM : 
##      Step 1: Start
##      Step 2: Define functions to do specific actions
##      Step 3: Call functions to set random intergers for reels
##      Step 4: Call functions to spin, calculate won/loss, and then loop
##      Step 5: When loop ends call play again
##      Step 6: End
## 
## ERROR HANDLING:
##      Do not enter strings for any integer calls
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import random
def play_again():
    user_input = input('Do you want to play again? ==> ')
    user_input = user_input.upper()
    while user_input != 'Y' and user_input != 'YES' and user_input != 'N' and user_input != 'NO':
        print('You must enter Y/YES/N/NO to continue. Please try again')
        user_input = input('Do you want to play again? ==> ')
        user_input = user_input.upper()
    if user_input == 'Y' or user_input == 'YES':
        return True
    if user_input == 'N' or 'NO':
        print('Have a great day!!')
        return False
def get_wager(bank):
    chips = int(input('How many chips do you want to wager? ==> '))
    if chips <= 0:
        print('The wager must be greater than 0. Please try again.')
        return get_wager(bank)
    elif chips > bank:
        print('The wager cannot be greater than the amount in your bank:', bank)
        return get_wager(bank)
    return chips
def get_slot_results() -> tuple:
    reela = random.randint(1, 10)
    reelb = random.randint(1, 10)
    reelc = random.randint(1, 10)
    return reela, reelb, reelc
def get_matches(reel) -> int:
    reela = reel[0]
    reelb = reel[1]
    reelc = reel[2]
    matches = 0
    if reela == reelb or reelb == reelc or reela == reelc:
        matches = 2
    if reela == reelb == reelc:
        matches = 3
    return matches
def get_bank() -> int:
    chips = int(input('How many chips do you want to start with? ==> '))
    if chips <= 0:
        print('Too low of a value, you can only choose 1-100 chips.')
        return get_bank()
    elif chips > 100:
        print('Too high of a value, you can only choose 1-100 chips.')
        return get_bank()
    return chips
def get_payout(wager, matches):
    if matches == 3:
        payout = wager * 10 - wager
    elif matches == 2:
        payout = wager * 3 - wager
    else:
        payout = -1 * wager
    return payout
if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        i = 0
        startchip = bank
        last = bank
        while bank > 0:
            wager = get_wager(bank)
            reel = get_slot_results()
            print('Your spin {} {} {}'.format(reel[0], reel[1], reel[2]))
            matches = get_matches(reel)
            print('You matched {} reels'.format(matches))
            payout = get_payout(wager, matches)
            print('You won/lost', payout)
            bank += payout
            i += 1
            print('Current bank:', bank)
            print()
            if last < bank:
                last = bank
            elif bank < 1:
                break


        print("You lost all {} in {} spins".format(last, i))
        print("The most chips you had was", last)
        playing = play_again()

