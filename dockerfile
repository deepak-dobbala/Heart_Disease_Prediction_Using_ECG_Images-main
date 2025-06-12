# 1. Base image
FROM python:3.11-slim

# 2. Avoid .pyc files & ensure output is streamed
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Create & switch to the app directory
WORKDIR /app

# 4. Copy and install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your project files
COPY . .

# 6. Expose port 5000 (convention)
EXPOSE 5000

# 7. Set the Flask app entrypoint
ENV FLASK_APP=flask/app_flask.py

# 8. Override CMD to use Flask CLI, binding to $PORT
#    Use shell form so $PORT is expanded at runtime
CMD flask run --host=0.0.0.0 --port $PORT
