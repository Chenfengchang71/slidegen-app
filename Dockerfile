FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 curl && \
    pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

ENV STREAMLIT_PORT=8501
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV STREAMLIT_BROWSER_SERVER_ADDRESS=0.0.0.0

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
