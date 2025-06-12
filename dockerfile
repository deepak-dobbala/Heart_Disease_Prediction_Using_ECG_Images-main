
# 1. Base image
FROM python:3.11-slim

# 2. Avoid .pyc files & ensure output is streamed
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Create & switch to the app directory
WORKDIR /app

# 4. Copy and install dependencies first (layer‑caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project files
COPY . .

# 6. Expose the Flask port
# … your existing Dockerfile up to COPY . .

# Expose the port (optional)
EXPOSE 5000

# Replace the CMD with this:
# - Uses the PORT environment variable Render will set
ENV FLASK_APP=flask/app_flask.py
CMD ["flask", "run", "--host=0.0.0.0", "--port", "${PORT}"]

