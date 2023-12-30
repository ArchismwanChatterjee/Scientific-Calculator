import streamlit as st
from PIL import Image


def home_page():

    st.image("logo.png",width=200)
    st.title("Scientific Calculator")

    st.write("Refer to the sidebar to choose the type of calculator, it consists of simple, mathematical, matrix, trigonometrical operations.")

    st.info("If you are viewing on mobile then you may opt to switch to landscape mode for smooth experience")

    st.success("Thanks for visiting 🤩!!")

if __name__ == "__main__":
    home_page()
