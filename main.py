import streamlit as st
import pandas

st.set_page_config(layout="wide")

company_title = """The Best Company"""
about_us = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. 
Fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque. Rhoncus dolor purus non enim praesent 
elementum facilisis leo vel. Id faucibus nisl tincidunt eget. Ut sem viverra aliquet eget sit amet. Egestas congue 
quisque egestas diam in arcu cursus. Erat nam at lectus urna duis """

our_team_header = "Our Team"

df = pandas.read_csv("data.csv")

st.header(company_title)
st.write(about_us)
st.subheader(our_team_header)

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])


with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("images/" + row["image"])





