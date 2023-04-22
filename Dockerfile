FROM python:3.11
# Use the python latest image
COPY . ./
# Copy the current folder content into the docker image
RUN pip install flask gunicorn langchain openai
# Install the required packages of the application
CMD gunicorn --bind :$PORT app:app
# Bind the port and refer to the app.py app