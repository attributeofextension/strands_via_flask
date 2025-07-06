# Use Python 3.13 base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./src .

# Set environment variables
ENV FLASK_APP=webserver.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV PYTHONUNBUFFERED=1
ENV WATCHDOG_TIMEOUT=5

# Expose port 5000
EXPOSE 8000

# Run the application
CMD ["python", "webserver.py"]