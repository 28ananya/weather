# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire current directory (including backend) into the container
COPY . /app

# Expose port 5000 for Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "backend/app.py"]
