
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies 
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first 
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the full project into the container
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Streamlit environment settings 
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
