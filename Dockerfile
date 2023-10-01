# Use the official Python image with Python 3.6 as a base image
FROM python:3.6

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Create a directory for your code in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

# Copy your requirements.txt into the container at /code/
COPY ./requirements.txt /code/requirements.txt

# Install project dependencies
RUN pip install -r requirements.txt

# Install Gunicorn for serving your Django application
RUN pip install gunicorn

# Copy the rest of your project files into the container
COPY . /code/

# Run Django migrations
RUN python manage.py migrate

# Expose the port that your Django application will run on (usually 8000)
EXPOSE 8000

# Specify the command to run your application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
