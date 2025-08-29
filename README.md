# ForecastFit

A modern, user-friendly desktop application for checking the current weather and receiving personalized clothing recommendations based on real-time conditions. Built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for a sleek interface and powered by the OpenWeatherMap API.

---

## Features

- **Current Weather:** Instantly fetches and displays the current weather for any city or town worldwide.
- **Clothing Recommendations:** Suggests what to wear based on temperature, wind, and weather conditions.
- **Weather Icons:** Visual representation of the weather (sun, rain, snow, etc.).
- **Temperature Units:** Switch easily between Celsius and Fahrenheit.
- **Error Handling:** Friendly messages for invalid city names or network issues.
- **Clean, Responsive UI:** Modern layout that adapts to window resizing.
- **Exit Button:** Quickly close the application.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Pillow](https://pypi.org/project/Pillow/) (`pip install pillow`)
- [customtkinter](https://pypi.org/project/customtkinter/) (`pip install customtkinter`)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (`pip install python-dotenv`)
- [requests](https://pypi.org/project/requests/) (`pip install requests`)
- An [OpenWeatherMap API key](https://openweathermap.org/api)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API key:**
    - Create a `.env` file in the project root:
      ```
      _KEYAPI=your_openweathermap_api_key_here
      ```

4. **Ensure the `weather icons` folder exists** in the project directory with the required PNG images (e.g., `sun.png`, `rainy.png`, etc.).

---

## Usage

1. **Run the application:**
    ```bash
    python [weather_gui.py](http://_vscodecontentref_/0)
    ```

2. **Enter a city or town** in the input field and click **"Get Weather"**.

3. **View the results:**
    - The current weather, description, temperature, wind speed, and a weather icon will be displayed.
    - Clothing recommendations will appear based on the weather and wind conditions.
    - Switch between Celsius and Fahrenheit using the dropdown menu.

4. **Exit the app** at any time using the red "Exit" button.

---

## Example

![Weather App Screenshot]([https://shorturl.at/0H4he](https://github.com/wojjjteeek/ForecastFit/blob/62ee2945bce56bdbebfc8a9cc258a9cfaa2bd0d5/Example.png))

---

## Troubleshooting

- **City not found:** Make sure the city name is spelled correctly.
- **No weather icon:** Ensure the required image files are present in the `weather icons` folder.
- **API errors:** Check your internet connection and that your API key is valid.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or new features.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for the weather data API.
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern Tkinter widgets.
