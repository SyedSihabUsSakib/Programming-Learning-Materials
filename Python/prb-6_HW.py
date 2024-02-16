import random
def playRockPaperScissor(rounds):
    playerScore = 0
    computerScore = 0
    actions = ['rock','paper','scissor']
    for round in range(0,rounds):
        playersChoice = input()
        computersChoice = random.choice(actions)
        print(f"Computer: {computersChoice}")
        # print(playersChoice, computersChoice)
        if playersChoice == 'rock':
            if computersChoice == 'paper':
                computerScore+=1
            elif computersChoice == 'scissor':
                playerScore += 1
        elif playersChoice == 'paper':
            if computersChoice == 'rock':
                playerScore+=1
            elif computersChoice == 'scissor':
                computerScore += 1
        elif playersChoice == 'scissor':
            if computersChoice == 'rock':
                computerScore+=1
            elif computersChoice == 'paper':
                playerScore += 1
    if playerScore>computerScore:
        winner = "Player"
    elif computerScore>playerScore:
        winner = "Computer"
    else:
        winner = "Tied"
    return (playerScore,computerScore,winner)

rounds = int(input())
ans = playRockPaperScissor(rounds)
print(f"Your Score: {ans[0]}")
print(f"Computer's Score: {ans[1]}")
if ans[2] == 'Player':
    print("You have won the game!")
elif ans[2] == 'Computer':
    print("Computer has won the game!")
else:
    print("The game is tied")