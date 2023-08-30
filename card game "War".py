#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random  # Import the random module for generating random numbers

def main():
    print("Welcome to the War game!")  # Display a welcome message
    input("Press Enter to start.")    # Wait for the player to start

    player_score = 0   # Initialize player's score
    computer_score = 0  # Initialize computer's score
    rounds = 0          # Initialize round counter

    while rounds < 10:  # Play for 10 rounds (you can adjust)
        rounds += 1     # Increment the round counter
        print(f"Round {rounds}")  # Display current round

        player_card = random.randint(1, 10)    # Generate player's card
        computer_card = random.randint(1, 10)  # Generate computer's card

        print(f"Your card: {player_card}")  # Display player's card
        input("Press Enter to play your card.")  # Wait for player
        print(f"Computer's card: {computer_card}")  # Display computer's card

        if player_card > computer_card:
            print("You won this round!")  
            player_score += 1  
        elif computer_card > player_card:
            print("Computer won this round.")  
            computer_score += 1  
        else:
            print("It's a tie in this round.")  

        print(f"Current score: Player {player_score} - Computer {computer_score}") 
        input("Press Enter to continue.")  

    if player_score > computer_score:
        print("Congratulations! You won the game!")  
    elif computer_score > player_score:
        print("Computer won the game. Try again.")  
    else:
        print("It's a tie! No one wins this time.")  

if __name__ == "__main__":
    main()  # Start the game


# In[ ]:




