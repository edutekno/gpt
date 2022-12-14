import streamlit as st

# Take input from the user
num1 = st.number_input("Enter first number: ")
num2 = st.number_input("Enter second number: ")

# Perform the calculations
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

# Output the results
st.write("Sum: ", sum)
st.write("Difference: ", diff)
st.write("Product: ", prod)
st.write("Quotient: ", quot)
