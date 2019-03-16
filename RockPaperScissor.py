from random import randint

Human_Score = 0
AI_Score = 0


while Human_Score < 2 and AI_Score < 2:
    print(f"The current score is:\n You ={Human_Score}\n ME ={AI_Score}\n ")
    print("Hello human, lets play a simple game of Rock, Paper, Scissor!!!")
    print("first to 2")
    Human = input("You start ").lower()
    num = [randint(0,2)]
    if num == 0:
        AI = "rock"
    elif num == 1:
        AI = "paper"
    else:
        AI = "scissor"
    
    if Human == AI:
        print("its a Tie, how can this be?!")        
    elif Human == "rock":
        if AI == "paper":
            print(f"{AI}, I win...Human!")
            AI_Score += 1
        else:
            print("YOU win...IMPOSSIBLE!")
            Human_Score += 1
    elif Human =="paper":
        if AI== "scissor":
            print(f"{AI}, I win...Human!")
            AI_Score += 1
        else:
            print("YOU win...IMPOSSIBLE!")
            Human_Score += 1
    elif Human =="scissor":
        if AI=="rock":
            print(f"{AI}, I win...Human")
            AI_Score += 1
        else:
            print("YOU win... IMPOSSIBLE!")
            Human_Score += 1
    else:
        print("that was not one of the options given to you human...focus please\n")
        print("\n")
print(f"The final Score is:Human = {Human_Score} to AI = {AI_Score} ")

