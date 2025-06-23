from weather_recommender import get_weather
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def recommended_clothing(city):
    list = get_weather(city)
    weather = list[0][0]
    weather_description = list[0][1]

    if weather == "Thunderstorm":
        weather_string = "Wear protective clothing like a raincoat but stay inside if you can"
    elif weather == "Drizzle":
        weather_string = "Wear light rain gear (e.g., waterproof jacket)"
    elif weather == "Rain":
        weather_string = "Bring an umbrella, wear waterproof clothing."
    elif weather == "Snow":
        weather_string = "Wear a thick coat, warm layers, gloves, scarf"
    elif weather == "Clear":
        weather_string = ""
    elif weather == "Clouds":
        weather_string = ""
    elif weather == "Mist" or "Smoke" or "Haze" or "Dust" or "Fog" or "Sand" or "Ash" or "Squall" or "Tornado":
        weather_string = "Wear face mask for dust/ash, caution for visibility but stay inside if you can."
    else:
        weather_string = ""

    temp = list[1]
    celsius = temp - 273.15
    celsius = round(celsius, 1)
    fahrenheit = (temp - 273.15) * 9/5 + 32
    fahrenheit = round(fahrenheit, 1)

    if celsius <= 0:
        temp_string = "Wear a thick coat, thermal layers, hat, scarf, and gloves."
    elif celsius <= 10:
        temp_string = "Wear a medium coat, sweater, and long pants."
    elif celsius <= 18:
        temp_string = "Wear a light jacket and long-sleeve shirt."
    elif celsius <= 25:
        temp_string = "Wear a t-shirt and pants."
    elif celsius <= 32:
        temp_string = "Wear a t-shirt, shorts, and sunglasses."
    else:
        temp_string = "Wear loose, light-colored clothing, hat, and sunscreen."

    wind_speed = list[2]
    wind_speed = round(wind_speed, 1)

    if wind_speed <= 3:
        wind_speed_category = "Small or No Wind"
        wind_string = ""
    elif wind_speed <= 7:
        wind_speed_category = "Pretty Windy"
        wind_string = ""
    elif wind_speed <= 13:
        wind_speed_category = "Very Windy"
        wind_string = "Wear a light windbreaker and secure loose accessories."
    else:
        wind_speed_category = "Hurricane"
        wind_string = "STAY INSIDE!"

    output_string = (weather_string + temp_string + wind_string)
    print(weather)
    print(celsius)
    print(wind_speed_category)
    print("----------------------")
    return output_string

def clicked():
    print("clicked")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

title = customtkinter.CTkLabel(frame, text = "Weather App")
title.pack(pady = 20, padx = 55)

entry = customtkinter.CTkEntry(frame, placeholder_text = "City/Town")
entry.pack(pady = 20, padx = 55)

button = customtkinter.CTkButton(frame, text="Get Weather", command= lambda: recommended_clothing(entry.get()))
button.pack(pady = 20, padx = 55)   

print(entry.get())


root.mainloop()