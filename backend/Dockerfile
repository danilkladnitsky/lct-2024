FROM python:3.9

WORKDIR /app

# Copy and install dependencies
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the app
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 3000

# Run the app
CMD ["python", "app.py"]
