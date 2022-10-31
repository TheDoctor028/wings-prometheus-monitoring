FROM python:3.8
# Default port for monitoring api
EXPOSE 9101
# The url to the wings api (with port) Default port: 8080
ENV API_URL http://localhost:8080
# API key to authenticate to the api
# can be generated in the panel (must have read server rights)
ENV API_KEY 1234566789
# Copy app to container
COPY ./src /app
WORKDIR /app
# Install dependencies
RUN pip install -r requirements.txt
# Start app
CMD ["python", "main.py"]
