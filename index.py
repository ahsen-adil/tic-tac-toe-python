import random
import streamlit as st

# Title of the app
st.title("Rock-Paper-Scissors Game")

# Description
st.subheader("Enter your move and play against the computer!")

# List of valid moves
item_list = ["Rock", "Paper", "Scissor"]

# User input through radio buttons
user_input = st.radio("Choose your move:", options=item_list, index=0)

if st.button("Play"):
    # Generate computer choice
    comp_choice = random.choice(item_list)

    # Display user and computer choices
    st.write(f"**Your choice:** {user_input}")
    st.write(f"**Computer's choice:** {comp_choice}")

    # Determine the winner
    if user_input == comp_choice:
        result = "Both chose the same. It's a tie!"
    elif user_input == "Rock":
        if comp_choice == "Paper":
            result = "Paper covers Rock. **Computer wins!**"
        else:
            result = "Rock smashes Scissor. **You win!**"
    elif user_input == "Paper":
        if comp_choice == "Scissor":
            result = "Scissor cuts Paper. **Computer wins!**"
        else:
            result = "Paper covers Rock. **You win!**"
    elif user_input == "Scissor":
        if comp_choice == "Paper":
            result = "Scissor cuts Paper. **You win!**"
        else:
            result = "Rock smashes Scissor. **Computer wins!**"

    # Display result
    st.success(result)
