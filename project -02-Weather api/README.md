# 🌦️ Weather API App (Python)

A simple Python application that fetches real-time weather information using a Weather API. Users can enter a city name and view the current temperature, weather condition, humidity, wind speed, and other details.

## 📌 Features

- Get real-time weather data
- Search weather by city name
- Displays:
  - 🌡️ Temperature
  - ☁️ Weather Condition
  - 💧 Humidity
  - 💨 Wind Speed
  - 🌍 Country
  - 🤒 Feels Like Temperature
- Easy-to-use command-line interface
- Error handling for invalid city names

## 🛠️ Technologies Used

- Python 3.x
- Requests Library
- Weather API (OpenWeatherMap API)

## 📂 Project Structure

```
Weather-API/
│
├── weather.py
├── requirements.txt
├── README.md
└── screenshots/
    └── output.png (optional)
```

## 📦 Requirements

Install the required package:

```bash
pip install requests
```

or

```bash
pip install -r requirements.txt
```

## 🔑 Get Your API Key

1. Visit **https://openweathermap.org/api**
2. Create a free account.
3. Generate your API key.
4. Replace the API key in the Python file:

```python
API_KEY = "YOUR_API_KEY"
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/Weather-API.git
```

2. Open the project folder

```bash
cd Weather-API
```

3. Run the application

```bash
python weather.py
```

## 💻 Sample Output

```
========= Weather App =========

Enter City Name: Mumbai

City: Mumbai
Country: IN
Temperature: 30°C
Feels Like: 33°C
Humidity: 72%
Weather: Broken Clouds
Wind Speed: 4.6 m/s
```

## 🚀 Future Improvements

- GUI using Tkinter
- Weather Forecast for 5 Days
- Detect Current Location Automatically
- Save Search History
- Weather Icons
- Voice Assistant Integration

## 📚 Learning Outcomes

This project demonstrates:

- Working with REST APIs
- HTTP GET Requests
- JSON Data Parsing
- Error Handling
- Python Functions
- User Input
- External Libraries (Requests)

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Om Tiwari**

- GitHub: https://github.com/Omtiwari-prog
  
