import requests
import streamlit as st

# Page Title
st.title("🛍️ Makeup Products Store")

# API Data
mydata = requests.get("https://dummyjson.com/products")
response = mydata.json()

# Product Loop
for product in response['products']:

    # Container for each product
    with st.container():
        
        # 3 Columns
        col1, col2, col3 = st.columns([1, 2, 1])

        # Image
        with col1:
            st.image(product["images"][0], width=120)

        # Product Details
        with col2:
            st.subheader(product["title"])
            st.write(product["description"][:80] + "...")
            st.success(f"💲 Price: ${product['price']}")

        # Button
        with col3:
            st.button("Buy Now", key=product["id"])

        # Line Separator
        st.markdown("---")
        
            

