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
        self.temp_choice = customtkinter.CTkOptionMenu(self.frame, values=["Celsius", "Fahrenheit"], command=self.select_temp)
        self.temp_choice.set("Celsius")
        self.button = customtkinter.CTkButton(self.frame, text="Get Weather", command=self.on_get_weather)
        self.weather_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.weather_desc = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.temp_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.wind_text = customtkinter.CTkLabel(self.frame, text="", font=self.standard_font)
        self.recommended_clothing_text = customtkinter.CTkLabel(self.frame, font=self.title_font, text="")
        self.exit_button = customtkinter.CTkButton(self.frame, text="Exit", fg_color="red", hover_color="darkred", command=self.on_exit)

    def on_exit(self):
        """Callback for the 'Exit' button to close the application."""
        self.destroy()

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
        self.exit_button.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

    def on_get_weather(self):
        """
        Callback for the 'Get Weather' button.
        Fetches weather data for the entered city and updates the UI.
        """
        city = self.entry.get()
        self.recommended_clothing(city)

    def recommended_clothing(self, city):
        """Main method to update UI based on weather for a city."""
        try:
            weather_data = get_weather(city)
            self.weather = weather_data[0][0]
            weather_description = weather_data[0][1].capitalize()
            self.error_label.configure(text="")
        except Exception:
            self._show_error("City not found. Please check the spelling and try again.")
            return

        self._set_weather_image(self.weather)
        self._set_temperature_and_wind(weather_data)
        clothing_text = self._get_clothing_recommendation()
        self.recommended_clothing_text.configure(text=clothing_text)
        self.weather_text.configure(text=f"Weather: {self.weather}")
        self.weather_desc.configure(text=f"Description: {weather_description}")

    def _show_error(self, message):
        """
        Display an error message in the error label and clear other text fields.
        """
        self.error_label.configure(text=message)
        self.weather_text.configure(text="")
        self.weather_desc.configure(text="")
        self.temp_text.configure(text="")
        self.wind_text.configure(text="")
        self.recommended_clothing_text.configure(text="")
        self.image_label.configure(image=None)

    def _set_weather_image(self, weather):
        """Set the weather image based on weather type."""
        image_map = {
            "Thunderstorm": ["storm.png", "Wear protective clothing like a raincoat but stay inside if you can"],
            "Drizzle": ["rainy.png", "Wear a light raincoat or carry an umbrella."],
            "Rain": ["rainy.png", "Bring an umbrella, wear waterproof clothing."],
            "Snow": ["snowfall.png", "Wear a thick coat, warm layers, gloves, scarf."],
            "Clear": ["sun.png", ""],
            "Clouds": ["cloud.png", ""],
            "Mist": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Smoke": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Haze": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."],
            "Dust": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Fog": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Sand": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."],
            "Ash": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Squall": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."], "Tornado": ["haze.png", "Wear face mask for dust/ash, caution for visibility but stay inside if you can."]
        }
        filename = image_map.get(weather, None)
        if filename:
            img = customtkinter.CTkImage(
                light_image=Image.open(f'weather icons/{filename[0]}'),
                dark_image=Image.open(f'weather icons/{filename[0]}'),
                size=(300, 300)
            )
            self.image_label.configure(image=img)
        else:
            self.image_label.configure(image=None)

        self.weather_string = image_map.get(filename[1], "")

    def _set_temperature_and_wind(self, weather_data):
        """Calculate and display temperature and wind speed."""
        temp = weather_data[1]
        wind = weather_data[2]
        self.celsius = round(temp - 273.15, 1)
        self.fahrenheit = round((temp - 273.15) * 9/5 + 32, 1)
        self.wind_speed = round(wind, 1)
        self.temp_text.configure(text=f"Temperature: {self.celsius}°C")

    def _get_clothing_recommendation(self):
        """Return a clothing recommendation string based on temperature."""
        if self.celsius <= 0:
            self.temp_string = "Wear a thick coat, thermal layers, hat, scarf, and gloves."
        elif self.celsius <= 10:
            self.temp_string = "Wear a medium coat, sweater, and long pants."
        elif self.celsius <= 18:
            self.temp_string = "Wear a light jacket and long-sleeve shirt."
        elif self.celsius <= 25:
            self.temp_string = "Wear a t-shirt and pants."
        elif self.celsius <= 32:
            self.temp_string = "Wear a t-shirt, shorts, and sunglasses."
        else:
            self.temp_string = "Wear loose, light-colored clothing, hat, and sunscreen."

        if self.wind_speed <= 3:
            wind_speed_category = "No Wind"
            self.wind_string = ""
        elif self.wind_speed <= 7:
            wind_speed_category = "Some Wind"
            self.wind_string = ""
        elif self.wind_speed <= 13:
            wind_speed_category = "Very Windy"
            self.wind_string = "Wear a light windbreaker and secure loose accessories."
        else:
            wind_speed_category = "Hurricane"
            self.wind_string = "STAY INSIDE!"
        self.wind_text.configure(text=f"Wind: {wind_speed_category}")

        self.overall_string = (self.weather_string +" "+ self.temp_string +" " + self.wind_string)
        #self.overall_string =  self.wind_string
        self.recommended_clothing_text.configure(text=self.overall_string)

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