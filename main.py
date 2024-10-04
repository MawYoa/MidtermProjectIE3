import streamlit as st
import os

file = "D:\\$FILES\\SCHOOL_FILES\\#Fourth_Year\\First_Semester\\CSIT342_Industry_Elective_3\\MidtermProject\\MidtermProjectIE3\\main.py"
thisfile = os.path.abspath(file)
if ('/' in thisfile): os.chdir(os.path.dirname(thisfile))

# -- PAGE SETUP --

profile_1_page= st.Page(
    
    page="MProject/views/mainpage.py",
    title="First Page",
    icon=":material/account_circle:",
    default=True,
)

profile_2_page= st.Page(
    
    page="MProject/views/dataPage.py",
    title="Data Page",
    icon=":material/account_circle:",
)


# NAVIGATION SETUP

pg = st.navigation(
    {
        "Info": [profile_1_page, profile_2_page],
    }    
)

# SHARED ON ALL PAGES
st.sidebar.text("For CSIT342 - Industry Elective 3")


# RUN NAVIGATION
pg.run()