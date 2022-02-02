from random import choice

line = "-" * 50

signalsPt = ["pedra", "papel", "tesoura"]
#signalsEn = ["stone", "paper", "scissors"]


# Returns the number of rounds
def startsTheGame():
    print(line)
    print("JOKENPY")
    print(line)

    number_of_rounds = int(input("Set the number of rounds: "))
    print(line)
    return number_of_rounds

# Receives the player signal and choice random a signal
def round(p1_points, p2_points):
    signal = input("Choose your option: ")

    while not checksAnswer(signal, signalsPt):
        print(f"'{signal}' is not a option! Try again...")
        print(line)
        signal = input("Choose your option: ")

    print(choice(signalsPt).title())
    print(line)

# Returns the winner
#def comparesValues(p1_signal, p2_signal):
#    p1_signal = p1_signal.lower()

def checksAnswer(word, options):
    if word.lower() in options:
        return True
    return False


############################# MAIN #################################

rounds = startsTheGame()
round_count = 0
player_points = 0
comp_points = 0

while rounds > round_count:
    round(player_points, comp_points)
    round_count+=1
    