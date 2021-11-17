def get_weather(json_dict):
    return json_dict['weather'][0]['description'].title() # title() fa le maiuscole

def get_temperature(json_dict):
    return str(json_dict['main']['temp']) + " Cº"


def get_icon(json_dict):
    return f"http://openweathermap.org/img/wn/{json_dict['weather'][0]['icon']}@4x.png"
    

