FROM python:3.8
# Default port for monitoring api
ENV PORT 9001
EXPOSE 9001
# Default check interval
ENV CHECK_INTERVAL_S 5
# Copy app to container
COPY ./src /app
WORKDIR /app
# Install dependencies
RUN pip install -r requirements.txt
# Start app
CMD ["python", "main.py"]
