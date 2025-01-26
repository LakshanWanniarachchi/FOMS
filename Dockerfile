# Use the official Python image from the Docker Hub
FROM python:3.9

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Copy the rest of the application code to the working directory
COPY . .

# Set the command to run Gunicorn with proper array syntax
CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]
