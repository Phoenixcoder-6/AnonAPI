# Use official Python image
FROM python:3.10-slim-buster
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /app
# Copy files
COPY . /app
# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Run nltk setup to download data
RUN python nltk_setup.py
# Expose port
EXPOSE 8000
# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
