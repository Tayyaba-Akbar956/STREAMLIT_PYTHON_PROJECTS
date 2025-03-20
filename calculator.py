import streamlit as st
import math

# Title of the app
st.title("Simple Calculator")

# Initialize session state to store the current input
if "input" not in st.session_state:
    st.session_state.input = ""
if "display" not in st.session_state:
    st.session_state.display = ""
if st.session_state.input == "Error":
    st.session_state.input = ""
    st.session_state.display = ""
    


# Display the current input
st.text_input("Display", value=st.session_state.input, key="display", disabled=True)

# Function to handle button clicks
def button_click(value):
    if value == "AC":
        st.session_state.input = ""  # Clear the input
        st.session_state.display = ""  # Clear the display
    elif value == "="or value == "Ans":
        try:
            # Evaluate the input expression
            st.session_state.input = str(eval(st.session_state.input))
            st.session_state.display = st.session_state.input
        except:
            st.session_state.input = "Error"  # Handle invalid expressions
            st.session_state.display = "Error"
    elif value == "＋":
        st.session_state.input += "+"
        st.session_state.display += "+"  # Update display
    elif value == "−":
        st.session_state.input += "-"
        st.session_state.display += "-"  # Update display
    elif value == "x":
        st.session_state.input += "*"
        st.session_state.display += "x"  # Update display
    elif value == "÷":
        st.session_state.input += "/"
        st.session_state.display += "÷"
    elif value == "inv":
        st.session_state.input += "1/"
        st.session_state.display += "1/"
    elif value == "%":
        st.session_state.input += "/100"
        st.session_state.display += "/100"
    elif value == "x^y":
        st.session_state.input += "**"
        st.session_state.display += "^"

    elif value == "√":
        st.session_state.input += "**0.5"
        st.session_state.display += "√"

    elif value == "EXP":
        st.session_state.input += "*10**"
        st.session_state.display += "E"

    elif value == "π":
        st.session_state.input += str (math.pi)
        st.session_state.display += "π"

    elif value == "e":
        st.session_state.input += str (math.e)
        st.session_state.display += "e"

    elif value == "sin":
        st.session_state.input += "math.sin("
        st.session_state.display += "sin("

    elif value == "cos":
        st.session_state.input += "math.cos("
        st.session_state.display += "cos("

    elif value == "tan":
        st.session_state.input += "math.tan("
        st.session_state.display += "tan("

    elif value == "ln":
        st.session_state.input += "math.log("
        st.session_state.display += "ln("

    elif value == "log":
        st.session_state.input += "math.log10("
        st.session_state.display += "log("

    elif value == "x!":
        try:
            num = int(eval(st.session_state.input))
            st.session_state.input = str(math.factorial(num))
            st.session_state.display = st.session_state.input
        except:
            st.session_state.input = "Error"
            st.session_state.display = "Error"
    elif value == "CE":
        st.session_state.input = st.session_state.input[:-1]  # Remove last character
        st.session_state.display = st.session_state.display[:-1]  # Update display


    else:
        # Append the clicked button value to the input
        st.session_state.input += value
        st.session_state.display += value

# Create 6 equal-width columns
cols = st.columns(7)  

# Define button layout row-wise
buttons = [
    [ "x!", "(", ")","%", "CE","AC","Ans"],
    ["Inv", "sin", "ln", "7", "8", "9","÷"],
    ["π", "cos", "log", "4", "5", "6","x"],
    ["e", "tan", "√", "1", "2", "3","−"],
    ["EXP", "x^y", ".", "0","＋", "="]
]

for row in buttons:
    for i, button in enumerate(row):
        cols[i].button(button, on_click=button_click, args=(button,), use_container_width=True)

