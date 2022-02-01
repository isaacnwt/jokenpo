linha = "-" * 50

signalsPt = ["pedra", "papel", "tesoura"]
signalsEn = ["stone", "paper", "scissors"]

def startsTheGame():
    print(linha)
    print("JOKENPY")
    print(linha)

    number_of_rounds = int(input("Set the number of rounds: "))
    return number_of_rounds

def round(p1_points, p2_points):
    choice = input("Chose your option: ")

    #if checksAnswer(choice, signalsPt):





def checksAnswer(word, signalList):
    if word in signalList:
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




