import streamlit as st
import requests

st.title("🎬 Movie Search App")

movie_name = st.text_input("Enter Movie Name")

API_KEY = "2e4d56a0"

if st.button("Search"):

    if movie_name:

        url = f"https://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":

            if data.get("Poster") != "N/A":
                st.image(data["Poster"], width=250)

            st.subheader(data["Title"])
            st.write("⭐ IMDb Rating:", data["imdbRating"])
            st.write("📅 Year:", data["Year"])
            st.write("🎭 Genre:", data["Genre"])
            st.write("🎬 Director:", data["Director"])
            st.write("👥 Actors:", data["Actors"])
            st.write("🌍 Language:", data["Language"])
            st.write("⏱ Runtime:", data["Runtime"])
            st.write("📝 Plot:")
            st.write(data["Plot"])

        else:
            st.error(data.get("Error"))

    else:
        st.warning("Please Enter Movie Name")