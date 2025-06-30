import customtkinter
from PIL import Image
from weather_recommender import get_weather

class WeatherApp(customtkinter.CTk):
    """
    Main application class for the Weather App GUI.
    Handles widget creation, layout, and user interactions.
    """

    def __init__(self):
        """
        Initialize the WeatherApp window and set up fonts, widgets, and layout.
        """
        super().__init__()
        self.title("Weather App")
        self.geometry("1400x800")
        self.setup_fonts()
        self.setup_widgets()
        self.setup_layout()

    def setup_fonts(self):
        """Set up custom fonts for the application."""
        self.title_font = customtkinter.CTkFont(family="Arial", size=30, weight="bold", underline=True)
        self.standard_font = customtkinter.CTkFont(family="Arial", size=20)

    def setup_widgets(self):
        """Create all widgets used in the application."""
        self.frame = customtkinter.CTkFrame(master=self)
        self.title = customtkinter.CTkLabel(self.frame, text="Weather App :>", font=self.title_font)
        self.image_label = customtkinter.CTkLabel(self.frame, text="")
        self.error_label = customtkinter.CTkLabel(self.frame, text="", text_color="red", font=self.standard_font)
        self.entry = customtkinter.CTkEntry(self.frame, placeholder_text="City/Town")
        self.temp_choice = customtkinter.CTkOptionMenu(self.frame, values=["Celcius", "Fahrenheit"], command=self.select_temp)
        self.button = customtkinter.CTkButton(self.frame, text="Get Weather", command=self.on_get_weather)
        self.weather_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.weather_desc = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.temp_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.wind_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.recommended_clothing_text = customtkinter.CTkLabel(self.frame, font=self.title_font, text="")

    def setup_layout(self):
        """Arrange widgets in the frame using grid and configure grid weights."""
        # Configure grid columns and rows to expand with window resizing
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        for i in range(5):
            self.frame.grid_rowconfigure(i, weight=1)

        self.frame.pack(fill="both", expand=True)

        # Place widgets in the grid
        self.title.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")
        self.entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")
        self.temp_choice.grid(row=2, column=0, pady=10, padx=10, sticky="ew")
        self.temp_choice.set("Celcius")
        self.button.grid(row=3, column=0, pady=10, padx=10, sticky="ew")
        self.weather_text.grid(row=1, column=1, pady=10, padx=10, sticky="ew")
        self.weather_desc.grid(row=2, column=1, pady=10, padx=10, sticky="ew")
        self.temp_text.grid(row=3, column=1, pady=10, padx=10, sticky="ew")
        self.wind_text.grid(row=4, column=1, pady=10, padx=10, sticky="ew")
        self.recommended_clothing_text.grid(row=3, column=2, pady=10, padx=10, sticky="ew")
        self.error_label.grid(row=5, column=0, columnspan=3, pady=10, padx=10, sticky="ew")
        self.image_label.grid(row=1, column=2, pady=10, padx=10, sticky="nsew")

    def on_get_weather(self):
        """
        Callback for the 'Get Weather' button.
        Fetches weather data for the entered city and updates the UI.
        """
        city = self.entry.get()
        self.recommended_clothing(city)

    def recommended_clothing(self, city):
        """
        Fetch weather data and update UI elements with weather info, images, and recommendations.
        Handles errors gracefully if the city is not found or API fails.
        """
        try:
            weather_data = get_weather(city)
            self.weather = weather_data[0][0]
            weather_description = weather_data[0][1]
            weather_description = weather_description.capitalize()
            self.error_label.configure(text="")
        except Exception:
            # Handle errors such as city not found or API/network issues
            self.error_label.configure(text="City not found. Please check the spelling and try again.")
            self.weather_text.configure(text="")
            self.weather_desc.configure(text="")
            self.temp_text.configure(text="")
            self.wind_text.configure(text="")
            self.recommended_clothing_text.configure(text = "")
            self.image_label.configure(image=None)
            return

        if self.weather == "Thunderstorm":
            weather_string = "Wear protective clothing like a raincoat but stay inside if you can"
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/storm.png'), dark_image=Image.open('weather icons/storm.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather == "Drizzle":
            weather_string = "Wear light rain gear (e.g., waterproof jacket)"
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/rainy.png'), dark_image=Image.open('weather icons/rainy.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather == "Rain":
            weather_string = "Bring an umbrella, wear waterproof clothing."
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/rainy.png'), dark_image=Image.open('weather icons/rainy.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather == "Snow":
            weather_string = "Wear a thick coat, warm layers, gloves, scarf"
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/snowfall.png'), dark_image=Image.open('weather icons/snowfall.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather == "Clear":
            weather_string = ""
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/sun.png'), dark_image=Image.open('weather icons/sun.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather == "Clouds":
            weather_string = ""
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/cloud.png'), dark_image=Image.open('weather icons/cloud.png'), size=(300, 300))
            self.image_label.configure(image=img)
        elif self.weather in ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado"]:
            weather_string = "Wear face mask for dust/ash, caution for visibility but stay inside if you can."
            img = customtkinter.CTkImage(light_image=Image.open('weather icons/haze.png'), dark_image=Image.open('weather icons/haze.png'), size=(300, 300))
            self.image_label.configure(image=img)
        else:
            weather_string = ""

        temp = weather_data[1]
        self.celsius = round(temp - 273.15, 1)
        self.fahrenheit = round((temp - 273.15) * 9/5 + 32, 1)

        if self.celsius <= 0:
            temp_string = "Wear a thick coat, thermal layers, hat, scarf, and gloves."
        elif self.celsius <= 10:
            temp_string = "Wear a medium coat, sweater, and long pants."
        elif self.celsius <= 18:
            temp_string = "Wear a light jacket and long-sleeve shirt."
        elif self.celsius <= 25:
            temp_string = "Wear a t-shirt and pants."
        elif self.celsius <= 32:
            temp_string = "Wear a t-shirt, shorts, and sunglasses."
        else:
            temp_string = "Wear loose, light-colored clothing, hat, and sunscreen."

        self.wind_speed = weather_data[2]
        self.wind_speed = round(self.wind_speed, 1)

        if self.wind_speed <= 3:
            wind_speed_category = "No Wind"
            wind_string = ""
        elif self.wind_speed <= 7:
            wind_speed_category = "Some Wind"
            wind_string = ""
        elif self.wind_speed <= 13:
            wind_speed_category = "Very Windy"
            wind_string = "Wear a light windbreaker and secure loose accessories."
        else:
            wind_speed_category = "Hurricane"
            wind_string = "STAY INSIDE!"

        output_string = (weather_string +" "+ temp_string +" " + wind_string)
        self.weather_text.configure(text = "Weather: " + self.weather)
        self.weather_desc.configure(text = "Weather Description: " + weather_description)

        self.temp_text.configure(text = "Temperature: "+ str(self.celsius) + "°C")
        self.wind_text.configure(text = "Wind: " + wind_speed_category)
        self.recommended_clothing_text.configure(text = output_string)

    def select_temp(self, choice):
        """
        Callback for temperature unit selection.
        Updates the temperature display according to the selected unit.
        """
        if choice == "Celsius":
            self.temp_text.configure(text = "Temperature: "+ str(self.celsius) + "°C")
        elif choice == "Fahrenheit":
            self.temp_text.configure(text = "Temperature: "+ str(self.fahrenheit) + "°F")

if __name__ == "__main__":
    # Start the Weather App
    app = WeatherApp()
    app.mainloop()