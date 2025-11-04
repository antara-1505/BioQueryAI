# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /BioQuery-ai

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Set environment variable
ENV PYTHONPATH="${PYTHONPATH}:/BioQuery-ai"

# Run Streamlit
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
