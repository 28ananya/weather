## Real-Time Weather Monitoring System
    This is a real-time weather monitoring system that fetches data from the OpenWeatherMap API and displays it in a user-friendly web interface. The backend is built with Flask, while the frontend uses HTML/CSS/JavaScript for dynamic updates. The application is containerized using Docker for easy setup and deployment.
## Features
    Fetches real-time weather data for multiple cities.
    Displays current temperature, feels-like temperature, and weather conditions.
    Automatically refreshes weather data every 5 minutes.
    Runs in a Docker container for ease of deployment.
## Table of Contents
    Features
    Prerequisites
    Installation
    Configuration
    Running the Application
## Prerequisites
    Before setting up the application, ensure you have the following installed:
    Docker
    Docker Compose
    OpenWeatherMap API Key (Sign up here to get your API key).
## Installation
## Clone the repository
    git clone  git clone add origin https://github.com/28ananya/weather.git
    cd weather
## Set up the configuration
    Create a configuration file to store your OpenWeatherMap API key:

    Create a file backend/config/settings.py and add your API key like this:

    API_KEY = "your_openweathermap_api_key"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    Replace "your_openweathermap_api_key" with your actual API key.

## Configuration
    Ensure the Dockerfile and docker-compose.yml are correctly set up.
    Docker will build the application using the Dockerfile, and the docker-compose.yml orchestrates the services.

## Running the Application
Using Docker
Build the Docker image and start the containers:
    docker-compose up --build
# Once the container is running, open your browser and go to:
    http://localhost:5000
# additionals
Extend the system to support additional weather parameters from the OpenWeatherMap
API (e.g., humidity, wind speed) and incorporate them into rollups/aggregates.
Explore functionalities like weather forecasts retrieval and generating summaries based
on predicted conditions.
