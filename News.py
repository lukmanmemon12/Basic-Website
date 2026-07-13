import streamlit as st
import requests

# -------------------------
# Streamlit Page Settings
# -------------------------
st.set_page_config(
    page_title="Live News App",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Live News App")
st.write("Read the latest news from NewsAPI")

# -------------------------
# News API Key
# -------------------------
API_KEY = "899351c35ac74b9b967177fcbcbfe586"

# -------------------------
# Search Box
# -------------------------
search = st.text_input(
    "🔍 Search News",
    placeholder="Technology, Sports, India..."
)

# -------------------------
# Category
# -------------------------
category = st.selectbox(
    "Select Category",
    [
        "general",
        "business",
        "entertainment",
        "health",
        "science",
        "sports",
        "technology"
    ]
)

# -------------------------
# API URL
# -------------------------
if search:
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={search}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    )
else:
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country=us&category={category}&apiKey={API_KEY}"
    )

# -------------------------
# Get News
# -------------------------
response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    articles = data.get("articles", [])

    if len(articles) == 0:
        st.warning("No news found.")

    for article in articles:

        with st.container():

            col1, col2 = st.columns([1, 2])

            with col1:
                if article["urlToImage"]:
                    st.image(article["urlToImage"], use_container_width=True)

            with col2:

                st.subheader(article["title"])

                st.write(article.get("description", "No description available."))

                st.write("**Source:**", article["source"]["name"])

                st.write("**Published:**", article["publishedAt"][:10])

                st.link_button(
                    "📖 Read Full News",
                    article["url"]
                )

            st.divider()

else:
    st.error("Failed to fetch news. Check your API key.")