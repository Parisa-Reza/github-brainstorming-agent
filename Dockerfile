FROM python:3.12-slim

WORKDIR /app

# System packages needed by GitPython and tree-sitter builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install a lightweight CPU only version of torch first,
# so the full GPU version never gets pulled in by mistake
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Now install everything else your project needs
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render expects the app to listen on the port it provides
# through the PORT environment variable (default 10000)
EXPOSE 10000

CMD python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:${PORT:-10000} --insecure