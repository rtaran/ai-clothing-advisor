# Weather App with OpenAI Integration

A Python-based weather application that combines real-time weather data with OpenAI-powered clothing suggestions. The app provides current weather information and personalized clothing recommendations based on weather conditions.

## 🌟 Features

- **Weather Information**: Get real-time weather data for any city worldwide
- **Smart Clothing Suggestions**: Receive AI-powered clothing recommendations based on current weather
- **Location Support**: Global coverage with city and country-based location search
- **Current Conditions**: Display temperature and wind speed information
- **Interactive Menu**: User-friendly command-line interface

## 🛠️ Technologies Used

- Python 3.12.3
- Requests library for API interactions
- OpenAI API for clothing suggestions
- API Ninjas for geocoding
- Open-Meteo API for weather data
- UV package manager for dependency management

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone [git@github.com:rtaran/ai-clothing-advisor.git]
   cd weather-app
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   # Install uv if not already installed
   pip install uv
   
   # Install dependencies using uv
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your API keys:
     ```
     API_GEO_KEY=your_api_ninjas_key
     API_OPENAI_KEY=your_openai_key
     ```

## 🚀 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Follow the prompts**
   - Enter city name
   - Enter country name
   - Use the menu to access different features

3. **Available Options**
   - Get coordinates
   - Get current weather
   - Display weather information
   - Get clothing suggestions
   - View weekly forecast
   - Export data to CSV
   
## 📝 Menu Options
1. Get coordinates
2. Get current weather
3. Display weather info
4. Suggest clothing
5. Get weekly forecast
6. Export DB to CSV
7. Exit

## 🔑 API Keys Required

This application requires two API keys to function:
- API Ninjas key for geocoding (Get it from [API Ninjas](https://api-ninjas.com))
- OpenAI API key for clothing suggestions (Get it from [OpenAI](https://platform.openai.com))

## 📦 Project Structure
weather-app/
├── main.py # Main application file
├── weather_oop.py # Weather class implementation
├── .env # Environment variables (not in repo)
├── .env.example # Example environment file
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚙️ Development

For adding new dependencies to the project: