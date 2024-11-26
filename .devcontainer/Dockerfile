FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Avoid warnings and install system dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libssl-dev \
    pkg-config \
    lldb \
    python3-pip \
    python3-venv \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Reset DEBIAN_FRONTEND
ENV DEBIAN_FRONTEND=dialog

# Set up environment variables
ENV PATH="/root/.cargo/bin:${PATH}" \
    PYTHONPATH="${PYTHONPATH}:/workspace"
