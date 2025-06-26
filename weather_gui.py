from weather_recommender import get_weather
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1400x800")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=35, fill="both", expand=True)

image_label = customtkinter.CTkLabel(frame, text="")
image_label.grid(row=2, column=2, pady=10, padx=10, sticky="nsew")

title_font = customtkinter.CTkFont(family="Arial", size=30, weight ="bold", underline=True)
standard_font = customtkinter.CTkFont(family="Arial", size=20)

# Add this label for error messages (place it in your UI setup code)
error_label = customtkinter.CTkLabel(frame, text="", text_color="red", font=standard_font)
error_label.grid(row=5, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

def recommended_clothing(city):
    global celsius, fahrenheit
    try:
        list = get_weather(city)
        weather = list[0][0]
        weather_description = list[0][1]
        weather_description = weather_description.capitalize()
        error_label.configure(text="")
    except Exception:
        error_label.configure(text="City not found. Please check the spelling and try again.")
        weather_text.configure(text="")
        weather_desc.configure(text="")
        temp_text.configure(text="")
        wind_text.configure(text="")
        image_label.configure(image=None)
        return

    if weather == "Thunderstorm":
        weather_string = "Wear protective clothing like a raincoat but stay inside if you can"
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/storm.png'), dark_image=Image.open('weather icons/storm.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather == "Drizzle":
        weather_string = "Wear light rain gear (e.g., waterproof jacket)"
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/rainy.png'), dark_image=Image.open('weather icons/rainy.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather == "Rain":
        weather_string = "Bring an umbrella, wear waterproof clothing."
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/rainy.png'), dark_image=Image.open('weather icons/rainy.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather == "Snow":
        weather_string = "Wear a thick coat, warm layers, gloves, scarf"
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/snowfall.png'), dark_image=Image.open('weather icons/snowfall.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather == "Clear":
        weather_string = ""
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/sun.png'), dark_image=Image.open('weather icons/sun.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather == "Clouds":
        weather_string = ""
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/cloud.png'), dark_image=Image.open('weather icons/cloud.png'), size=(200, 200))
        image_label.configure(image=img)
    elif weather in ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado"]:
        weather_string = "Wear face mask for dust/ash, caution for visibility but stay inside if you can."
        img = customtkinter.CTkImage(light_image=Image.open('weather icons/haze.png'), dark_image=Image.open('weather icons/haze.png'), size=(200, 200))
        image_label.configure(image=img)
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
        wind_speed_category = "No Wind"
        wind_string = ""
    elif wind_speed <= 7:
        wind_speed_category = "Some Wind"
        wind_string = ""
    elif wind_speed <= 13:
        wind_speed_category = "Very Windy"
        wind_string = "Wear a light windbreaker and secure loose accessories."
    else:
        wind_speed_category = "Hurricane"
        wind_string = "STAY INSIDE!"

    output_string = (weather_string +" "+ temp_string +" " + wind_string)
    weather_text.configure(text = "Weather: " + weather)
    weather_desc.configure(text = "Weaher Description: " + weather_description)

    temp_text.configure(text = "Temperature: "+ str(celsius) + "°C")
    wind_text.configure(text = "Wind: " + wind_speed_category)
    recommended_clothing_text = customtkinter.CTkLabel(root, text = output_string)

def select_temp(choice):
    if choice == "Celcius":
        temp_text.configure(text = "Temperature: "+ str(celsius) + "°C")
    elif choice == "Fahrenheit":
        temp_text.configure(text = "Temperature: "+ str(fahrenheit) + "°F")

# Configure grid weights for frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

title = customtkinter.CTkLabel(frame, text="Weather App :>", font=title_font)
title.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

entry = customtkinter.CTkEntry(frame, placeholder_text="City/Town")
entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

temp_choice = customtkinter.CTkOptionMenu(frame, values=["Celcius", "Fahrenheit"], command=select_temp)
temp_choice.grid(row=2, column=0, pady=10, padx=10, sticky="ew")
temp_choice.set("Celcius")

button = customtkinter.CTkButton(frame, text="Get Weather", command=lambda: recommended_clothing(entry.get()))
button.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

weather_text = customtkinter.CTkLabel(frame, text="", font=standard_font)
weather_text.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

weather_desc = customtkinter.CTkLabel(frame, text="", font=standard_font)
weather_desc.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

temp_text = customtkinter.CTkLabel(frame, text="", font=standard_font)
temp_text.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

wind_text = customtkinter.CTkLabel(frame, text="", font=standard_font)
wind_text.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

root.mainloop()