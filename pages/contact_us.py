import streamlit as st

st.set_page_config()

st.header("contact me")


with st.form(key="my_form"):
    user_email = st.text_input("your email address")
    message = st.text_area("your message")
    button = st.form_submit_button()


    