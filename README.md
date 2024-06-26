# mlops
trying out first mlops project


Here's a summary of what I have done in this project so far:

Data Loading and Analysis:
Loaded a CSV dataset using Pandas.
Analyzed the data to understand its structure and features.


Virtual Environment Setup:
Created a virtual environment to isolate the  project's dependencies.
Installed necessary Python packages within the virtual environment.


Model Building:
Built a machine learning model using scikit-learn's Logistic Regression.

Flask Application Setup:
Created a Flask application to serve the machine learning model.
Defined a /predict route to make predictions based on input data.
Configured the application to run on a specific port.

Dockerization:
Created a Dockerfile to containerize the Flask application.

Built a Docker image.
RUN a Docker container for the Flask application.


Continuous Integration/Continuous Deployment (CI/CD):
Set up a GitHub Actions workflow for CI/CD.
Automated the build and push of Docker images using GitHub Actions.
