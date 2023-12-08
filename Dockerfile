# Start with a Python build image
FROM python:3.8 as builder
WORKDIR /app
COPY requirements.txt .
# Install PortAudio library
RUN apt-get update && apt-get install -y portaudio19-dev
# Install Python packages
RUN pip install -r requirements.txt

# Use a distroless image
FROM gcr.io/distroless/python3
COPY --from=builder /app /app
WORKDIR /app
CMD ["app.py"]
