print("Missionaries and Cannibals Problem")

# Initial state: 3 cannibals and 3 missionaries on the left side
cannibalLeft = 3
missionaryLeft = 3
boat = 'left'
cannibalRight = 0
missionaryRight = 0
step = 1

# Main game loop
while not (cannibalLeft == 0 and missionaryLeft == 0):
    print(f"Step {step}:")
    print(f"Left Bank -> Cannibals: {cannibalLeft}, Missionaries: {missionaryLeft}")
    print(f"Boat is on the {boat} bank.")
    print(f"Right Bank -> Cannibals: {cannibalRight}, Missionaries: {missionaryRight}")
    print("-" * 40)

    # Get user input for the number of cannibals and missionaries to move
    print("Choose your move:")
    cannibals = int(input("Number of cannibals to move: "))
    missionaries = int(input("Number of missionaries to move: "))

    # Validate move: boat can carry only 1 or 2 people
    if 0 <= cannibals + missionaries <= 2 and cannibals >= 0 and missionaries >= 0:
        # Handle boat movement from left to right
        if boat == 'left':
            if cannibals <= cannibalLeft and missionaries <= missionaryLeft:
                # Update the state after moving the boat to the right
                new_cannibalLeft = cannibalLeft - cannibals
                new_missionaryLeft = missionaryLeft - missionaries
                new_cannibalRight = cannibalRight + cannibals
                new_missionaryRight = missionaryRight + missionaries

                # Check if the new state is valid (no one gets eaten)
                if (new_missionaryLeft >= new_cannibalLeft or new_missionaryLeft == 0) and \
                        (new_missionaryRight >= new_cannibalRight or new_missionaryRight == 0):
                    # Apply the new state
                    cannibalLeft = new_cannibalLeft
                    missionaryLeft = new_missionaryLeft
                    cannibalRight = new_cannibalRight
                    missionaryRight = new_missionaryRight
                    boat = 'right'
                    step += 1
                else:
                    print("Invalid move. Missionaries eaten! Try again.")
            else:
                print("Invalid move. Too many people to move from left bank. Try again.")

        # Handle boat movement from right to left
        else:
            if cannibals <= cannibalRight and missionaries <= missionaryRight:
                # Update the state after moving the boat to the left
                new_cannibalLeft = cannibalLeft + cannibals
                new_missionaryLeft = missionaryLeft + missionaries
                new_cannibalRight = cannibalRight - cannibals
                new_missionaryRight = missionaryRight - missionaries

                # Check if the new state is valid (no one gets eaten)
                if (new_missionaryLeft >= new_cannibalLeft or new_missionaryLeft == 0) and \
                        (new_missionaryRight >= new_cannibalRight or new_missionaryRight == 0):
                    # Apply the new state
                    cannibalLeft = new_cannibalLeft
                    missionaryLeft = new_missionaryLeft
                    cannibalRight = new_cannibalRight
                    missionaryRight = new_missionaryRight
                    boat = 'left'
                    step += 1
                else:
                    print("Invalid move. Missionaries eaten! Try again.")
            else:
                print("Invalid move. Too many people to move from right bank. Try again.")
    else:
        print("Invalid move. The boat can only hold 1 or 2 people. Try again.")

# Once the goal is reached
print("Congratulations! You successfully transported all missionaries and cannibals across the river.")
print(f"Step {step}:")
print(f"Left Bank -> Cannibals: {cannibalLeft}, Missionaries: {missionaryLeft}")
print(f"Boat is on the {boat} bank.")
print(f"Right Bank -> Cannibals: {cannibalRight}, Missionaries: {missionaryRight}")
