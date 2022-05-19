import random
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
count =          0
while True:
    computer = random.choice(choices)

    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            count =0
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            count +=1
            if count == 3:
                player_score+=4
            else:
                player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            count =0
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            count +=1
            if count == 3:
                player_score+=4
            else:
                player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            count = 0
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            count +=1
            if count == 3:
                player_score+=4
            else:
                player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break