import requests
import streamlit as st
mydata = requests.get("https://dummyjson.com/products")

response  = mydata.json()

print(response)

for product in response['products']:
    col1,col2,col3=st.columns(3)
    with col1:
        st.title(product["title"]) 
    with col2:
        st.title(product["price"])
    with col3:
        st.image(product["images"][0])

