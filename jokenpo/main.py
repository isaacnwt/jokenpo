from random import choice

line = "-" * 50

signalsPt = ["pedra", "papel", "tesoura"]
signalsEn = ["stone", "paper", "scissors"]

def startsTheGame():
    print(line)
    print("JOKENPY")
    print(line)

    number_of_rounds = int(input("Set the number of rounds: "))
    return number_of_rounds

def round(p1_points, p2_points):
    signal = input("Choose your option: ")

    while not checksAnswer(signal, signalsPt):
        print(f"'{signal}' is not a option! Try again...")
        print(line)
        signal = input("Choose your option: ")

    print(choice(signalsPt).title())
    print(line)





def checksAnswer(word, options):
    if word in options:
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




