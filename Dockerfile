# Use the official Python image for your desired version
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Create and set the working directory
WORKDIR /code

# Copy the requirements file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /code/

# Expose the port on which the Django application will run
EXPOSE 8000

# Define the default command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

