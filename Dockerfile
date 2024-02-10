FROM python:3.9
WORKDIR /demo
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["bash","-c","python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]

# # Use an official Python runtime as a parent image
# FROM python:3.9-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /code

# # Copy the current directory contents into the container at /code
# COPY . /code/


# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r /code/requirements.txt

# RUN python /code/manage.py makemigrations
# RUN python /code/manage.py migrate
# # Expose the port that Django runs on
# EXPOSE 5000

# # Define the command to run your server using gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "Flyshare.wsgi:application"]
