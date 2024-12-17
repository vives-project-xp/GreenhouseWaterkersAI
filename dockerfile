# Python images that is needed for main.py code
FROM python:3.11-slim

# Set workdirectory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app
# Copy the dashboard folder to the container
COPY dashboard /app/dashboard

# Install the necessary tools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose on the right port
EXPOSE 8501

# Set CMD instructions 
CMD ["streamlit", "run", "dashboard/main.py"]