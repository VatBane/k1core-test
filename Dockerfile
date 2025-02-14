# Base image
FROM python:3.12.6-slim as builder

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv for dependency management
RUN pip install uv

# Create and switch to a non-root user
RUN useradd -m worker

# Create virtual environment
RUN python -m venv /home/worker/venv
ENV PATH="/home/worker/venv/bin:$PATH"

# Copy and install dependencies
WORKDIR /home/worker/src
COPY --chown=worker:worker pyproject.toml .
RUN uv pip install --no-cache -e .

# Final image
FROM python:3.12.6-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and switch to a non-root user
RUN useradd -m worker

# Copy virtual environment from builder
COPY --from=builder --chown=worker:worker /home/worker/venv /home/worker/venv
ENV PATH="/home/worker/venv/bin:$PATH"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Create directory structure
WORKDIR /home/worker/src

# Copy application code
COPY --chown=worker:worker src/ /home/worker/src/
COPY --chown=worker:worker pyproject.toml /home/worker/

# Set Python path to include the app directory
ENV PYTHONPATH="/home/worker/src:$PYTHONPATH"

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports (adjust as needed for your application)
EXPOSE 8000
EXPOSE 8001

# Switch to non-root user
USER worker

# Start supervisord
CMD ["/usr/bin/supervisord"]