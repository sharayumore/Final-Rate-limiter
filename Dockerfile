# Use official Python slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Ensure Flask can find templates
COPY templates/ ./templates/

# Expose the port Gunicorn will run on
EXPOSE 8000

# Command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]