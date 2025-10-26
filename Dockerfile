# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y curl && \
    curl -L -o torch-2.8.0-cp39-cp39-manylinux_2_28_x86_64.whl https://files.pythonhosted.org/packages/fd/dd/1630cb51b10d3d2e97db95e5a84c32def81fc26b005bce6fc880b0e6db81/torch-2.8.0-cp39-cp39-manylinux_2_28_x86_64.whl && \
    echo "06fcee8000e5c62a9f3e52a688b9c5abb7c6228d0e56e3452983416025c41381  torch-2.8.0-cp39-cp39-manylinux_2_28_x86_64.whl" | sha256sum -c - && \
    pip install torch-2.8.0-cp39-cp39-manylinux_2_28_x86_64.whl && \
    pip install --no-cache-dir --timeout=600 -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
