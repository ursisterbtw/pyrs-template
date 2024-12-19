FROM debian:bullseye-slim AS base
# Set environment variables
ENV RUSTUP_HOME=/usr/local/rustup \
   CARGO_HOME=/usr/local/cargo \
   PATH=/usr/local/cargo/bin:$PATH
# Install base dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
   curl \
   ca-certificates \
   build-essential \
   libssl-dev \
   pkg-config \
   git \
   gnupg \
   && rm -rf /var/lib/apt/lists/*
# ==============================
# Rust Installation
# ==============================
FROM base AS rust-builder
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile minimal \
   && rustup component add rustfmt clippy \
   && cargo install cargo-watch
# ==============================
# Python Installation
# ==============================
FROM base AS python-builder
RUN apt-get update && apt-get install -y --no-install-recommends \
   python3 \
   python3-pip \
   python3-venv \
   python3-distutils \
   python3-setuptools \
   && rm -rf /var/lib/apt/lists/* \
   && python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel
# ==============================
# Node.js Installation
# ==============================
FROM base AS node-builder
RUN mkdir -p /etc/apt/keyrings \
   && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
   && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" > /etc/apt/sources.list.d/nodesource.list \
   && apt-get update \
   && apt-get install -y nodejs \
   && npm install -g npm@latest
# ==============================
# Final Image
# ==============================
FROM debian:bullseye-slim
# Install minimal runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
   ca-certificates \
   git \
   gnupg \
   curl \
   python3 \
   python3-pip \
   python3-venv \
   python3-distutils \
   python3-setuptools \
   && rm -rf /var/lib/apt/lists/* \
   && python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel
# Copy Node.js setup and install
COPY --from=node-builder /etc/apt/keyrings/nodesource.gpg /etc/apt/keyrings/
COPY --from=node-builder /etc/apt/sources.list.d/nodesource.list /etc/apt/sources.list.d/
RUN apt-get update && apt-get install -y nodejs \
   && rm -rf /var/lib/apt/lists/*
# Copy Rust
COPY --from=rust-builder /usr/local/cargo /usr/local/cargo
COPY --from=rust-builder /usr/local/rustup /usr/local/rustup
# Copy Python and its dependencies
COPY --from=python-builder /usr/bin/python3 /usr/bin/python3
COPY --from=python-builder /usr/bin/pip3 /usr/bin/pip3
COPY --from=python-builder /usr/lib/python3 /usr/lib/python3
COPY --from=python-builder /usr/lib/python3.9 /usr/lib/python3.9
COPY --from=python-builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=python-builder /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages
COPY --from=python-builder /usr/local/lib/python3.9/dist-packages /usr/local/lib/python3.9/dist-packages
# Set environment variables
ENV RUSTUP_HOME=/usr/local/rustup \
   CARGO_HOME=/usr/local/cargo \
   PATH=/usr/local/cargo/bin:$PATH \
   PYTHONPATH=/usr/lib/python3.9:/usr/local/lib/python3.9:/usr/lib/python3/dist-packages:/usr/local/lib/python3.9/dist-packages \
   LANG=C.UTF-8
# Verify installations
RUN python3 --version && \
   pip3 --version && \
   node --version && \
   npm --version && \
   rustc --version && \
   cargo --version
WORKDIR /app
CMD ["bash"]