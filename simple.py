import streamlit as st


def simple_calculator():
    st.title("Simple Calculator")
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    col1, col2, col3, col4 = st.columns(4)

    # Button to perform addition
    if col1.button("Addition"):
        result = num1 + num2
        st.text("")
        st.success(f"Result (Addition): {result}")
    
    # Button to perform subtraction
    if col2.button("Subtraction"):
        result = num1 - num2
        st.text("")
        st.success(f"Result (Subtraction): {result}")

    # Button to perform multiplication
    if col3.button("Multiplication"):
        result = num1 * num2
        st.text("")
        st.success(f"Result (Multiplication): {result}")

    # Button to perform division
    if col4.button("Division"):
        if num2 != 0:
            result = num1 / num2
            st.text("")
            st.success(f"Result (Division): {result}")
        else:
            st.error("Error: Division by zero")

if __name__ == "__main__":
    simple_calculator()

