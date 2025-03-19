import streamlit as st
import pandas

st.set_page_config(layout="wide" )


st.title("the Best company")

content1 = """In computer networking, localhost is a hostname that refers to the current computer used to access it.
 The name localhost is reserved for loopback purposes. 
 It is used to access the network services that are running on the host via the loopback network interface."""
st.write(content1)

col1,col2,col3 = st.columns(3)

data = pandas.read_csv("data .csv",sep=",")

with col1:
    for index,items in data[0:4].iterrows():
        st.title(f"{items["first name"]} {items["last name"]} ")
        st.write(items["role"])
        st.image("images/"+items["image"])

with col2:
    for index,items in data[4:8].iterrows():
        st.title(f"{items["first name"]} {items["last name"]} ")
        st.write(items["role"])
        st.image("images/" + items["image"])

with col3:
    for index,items in data[8:12].iterrows():
        st.title(f"{items["first name"]} {items["last name"]} ")
        st.write(items["role"])
        st.image("images/" + items["image"])










