import streamlit as st
import requests

# OpenWeather API Key
API_KEY = "7da2c7a97e1b02c488cfa1bad949df7d"

st.title("🌤 Simple Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city:

        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            st.success(f"Weather in {data['name']}")

            st.write(f"🌡 Temperature : {data['main']['temp']} °C")
            st.write(f"☁ Weather : {data['weather'][0]['description'].title()}")
            st.write(f"💧 Humidity : {data['main']['humidity']} %")
            st.write(f"🌬 Wind Speed : {data['wind']['speed']} m/s")

        else:
            st.error("City not found!")

    else:
        st.warning("Please enter a city name.")