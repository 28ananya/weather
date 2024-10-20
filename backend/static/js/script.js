// Function to fetch and update weather data
async function fetchWeatherData() {
    try {
        const response = await fetch('/api/weather');
        const data = await response.json();
        displayWeatherData(data);
    } catch (error) {
        console.error('Error fetching weather data:', error);
        displayErrorMessage(); // Display an error message in the UI
    }
}

// Function to display the weather data dynamically
function displayWeatherData(data) {
    const weatherContainer = document.getElementById('weather-container');
    weatherContainer.innerHTML = ''; // Clear previous data

    if (data.length === 0) {
        weatherContainer.innerHTML = '<p>No weather data available</p>';
        return;
    }

    data.forEach(city => {
        const card = document.createElement('div');
        card.className = 'weather-card';

        // Weather icons based on conditions
        const icon = getWeatherIcon(city.main);

        // Convert timestamp to a readable format
        const timestamp = new Date(city.timestamp * 1000).toLocaleString();

        // Display the city name, temp, feels_like, main, and timestamp with the weather icon
        card.innerHTML = `
            <h2>${city.city}</h2>
            <img src="${icon}" alt="${city.main} icon" />
            <div class="weather-details">
                <p>Current Temperature: ${city.temp.toFixed(2)}°C</p>
                
                <p>Feels Like: ${city.feels_like.toFixed(2)}°C</p>
                <p>Weather Condition: ${city.main}</p>
                
            </div>
        `;

        weatherContainer.appendChild(card);
    });
}

// Function to get weather icon based on weather condition
function getWeatherIcon(condition) {
    switch (condition.toLowerCase()) {
        case 'clear':
            return 'https://img.icons8.com/color/48/000000/sun.png';
        case 'rain':
            return 'https://img.icons8.com/color/48/000000/rain.png';
        case 'clouds':
            return 'https://img.icons8.com/color/48/000000/cloud.png';
        case 'mist':
            return 'https://img.icons8.com/color/48/000000/fog.png';
        case 'haze':
            return 'https://img.icons8.com/?size=48&id=15347&format=png';
        default:
            return 'https://img.icons8.com/color/48/000000/partly-cloudy-day.png';
    }
}

// Function to display an error message in the UI when there's an error
function displayErrorMessage() {
    const weatherContainer = document.getElementById('weather-container');
    weatherContainer.innerHTML = '<p>Error fetching weather data. Please try again later.</p>';
}

// Fetch weather data on page load
document.addEventListener("DOMContentLoaded", () => {
    fetchWeatherData();
    // Auto-refresh every 5 minutes (300000 milliseconds)
    setInterval(fetchWeatherData, 300000);
});
