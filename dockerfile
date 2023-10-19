
FROM python:3.9.6-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


RUN pip install --no-cache-dir numpy pandas matplotlib seaborn scikit-learn mlflow

CMD ["python", "app.py"]