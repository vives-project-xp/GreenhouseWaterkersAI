# Gebruik een officiële Python-basisimage
FROM python:3.11-slim

# Stel de werkdirectory in
WORKDIR /app

# Kopieer alleen de vereiste bestanden
COPY dashboard /app/dashboard
COPY requirements.txt /app

# Installeer de vereisten
RUN python -m venv myenv && \
    ./myenv/bin/pip install --upgrade pip && \
    ./myenv/bin/pip install -r requirements.txt

# Stel de virtuele omgeving in als standaard Python
ENV PATH="/app/myenv/bin:$PATH"

# Exposeer de standaard Streamlit-poort
EXPOSE 8501

# Start het Streamlit-dashboard
CMD ["streamlit", "run", "dashboard/main.py", "--server.port=8501", "--server.address=0.0.0.0"]