import requests
import streamlit as st
import webbrowser

# Page Title
st.title("🛍️ Makeup Products Store")

# Search Box
search = st.text_input("🔍 Search Products")

# API Data
response = requests.get("https://dummyjson.com/products").json()

# Filter Products
products = response["products"]

if search:
    products = [
        product for product in products
        if search.lower() in product["title"].lower()
    ]

# Product Loop
for product in products:

    with st.container():

        col1, col2, col3 = st.columns([1, 2, 1])

        # Product Image
        with col1:
            st.image(product["images"][0], width=120)

        # Product Details
        with col2:
            st.subheader(product["title"])
            st.write(product["description"][:80] + "...")
            st.success(f"💲 Price: ${product['price']}")

        # Buy Button
        with col3:
            if st.button("🛒 Buy Now", key=product["id"]):
                amazon_url = (
                    f"https://www.amazon.in/s?k="
                    f"{product['title'].replace(' ', '+')}"
                )
                webbrowser.open_new_tab(amazon_url)

        st.markdown("---")