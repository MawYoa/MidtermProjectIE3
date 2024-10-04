import streamlit as st


st.title('My First Streamlit App')
st.write('Welcome to my Streamlit app!')


# -- PAGE SETUP --

profile_1_page= st.Page(
    page="MidtermProjectIE3/views/main_page.py",
    title="First Page",
    icon=":material/account_circle:",
    default=True,
)