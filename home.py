import streamlit as st
from PIL import Image


def home_page():

    st.image("logo.png",width=150)

    st.title("Scientific Calculator")

    st.write("Refer to the sidebar to choose the type of calculator, it consists of simple, mathematical, matrix, trigonometrical operations.")

    container = st.container()

    with container:
        st.write("* Simple calculator performs simple operations like addition,subtraction,multiplication,division")
        st.text("")
        st.write("* Mathermatical calculator performs math operations like logarithm, exponents, root and more ...")
        st.text("")
        st.write("* Matrix calculator performs matrix operations like dot & cross product, inverse, rank and more ...")
        st.text("")
        st.write("* Trigonometric calculator gives the value for sin θ, cos θ, tan θ,... and also visualize the curve")
        st.text("")


    st.info("If you are viewing on mobile then you may opt to switch to landscape mode for smooth experience")

    st.success("Thanks for visiting 🤩!!")

if __name__ == "__main__":
    home_page()
