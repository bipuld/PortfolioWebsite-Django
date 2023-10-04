# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for your PostgreSQL database
ENV DATABASE_URL="postgres://username:password@hostname:port/database_name"

# Set environment variable for Django's secret key (replace with your secret key)
ENV DJANGO_SECRET_KEY="your-secret-key"

# Set environment variable to indicate that this is a Docker environment
ENV DOCKER_ENVIRONMENT=True

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
