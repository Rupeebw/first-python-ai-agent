def get_weather(city):
    # Simulated weather data for different cities
    weather_data = {
        "California": "sunny with a high of 75°F",
        "New York": "rainy with a high of 60°F",
        "London": "cloudy with occasional showers, high of 55°F",
        "Singapore": "thunderstorms with a high of 85°F",
        "Sydney": "clear skies with a high of 70°F"
    }
    
    # Return the weather for the requested city, or a default message if the city is not found
    return weather_data.get(city, "Weather data not available for this location")
