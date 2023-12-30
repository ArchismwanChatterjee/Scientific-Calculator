import streamlit as st
from home import home_page
from simple import simple_calculator 
from mathematical import math_calculator
from matrix import matrix_calculator
from trigo import trigo_calculator


def main():
    # Add elements to the sidebar
    st.sidebar.header("Select the calculator")
    selected_page = st.sidebar.radio("Choose", ["Home", "Simple","Mathematical","Matrix", "Trigonometric"])

    # Display different content based on the selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Simple":
        simple_calculator()
    elif selected_page=="Mathematical":
        math_calculator()
    elif selected_page=="Matrix":
        matrix_calculator()
    elif selected_page=="Trigonometric":
        trigo_calculator()

        
if __name__ == "__main__":
    main()

