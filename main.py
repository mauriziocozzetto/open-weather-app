# modifica del codice di Federico Barbieri: 

import streamlit as st
import json
import requests
#from weather_info import get_weather, get_temperature, get_icon
import weather_info as wi


st.title("Weather App")
location = st.text_input("Inserisci una città:")

if len(location) != 0: 

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&lang=it&appid=6af383864baba1c9e63faa2b29996f90")  

    print(type(response))

    if response.status_code == 200: # requests.codes.ok
        json_text = response.text
        print(json_text)
    
        # si ottiene un dizionario
        json_dict = json.loads(json_text)

        # ottengo le info che mi servono
        st.header(wi.get_weather(json_dict))
        st.header(wi.get_temperature(json_dict))
        st.image(wi.get_icon(json_dict))
    else:
        st.error("Città non trovata")

