FROM python:3.11-slim

# Set shell options
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils=22.12.0-2+b1 \
	pngquant=2.17.0-1 \
	curl=7.88.1-10+deb12u8 \
    && rm -rf /var/lib/apt/lists/*

# Install texlive for LaTeX compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
	texlive-xetex=2022.20230122-3 \
	texlive-fonts-recommended=2022.20230122-3 \
	texlive-fonts-extra=2022.20230122-4 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install uv and add it to PATH
ENV PATH="/root/.local/bin:/app/.venv/bin:$PATH"
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Create necessary directories
RUN mkdir -p /app/src /app/resume /app/scripts

# Copy scripts first
COPY scripts/build_resume.sh /app/scripts/
RUN chmod +x /app/scripts/build_resume.sh

# Copy requirements and install dependencies
COPY requirements.txt .

# hadolint ignore=SC1091
RUN uv venv .venv \
    && source .venv/bin/activate \
    && uv pip install -r requirements.txt

# Set the entrypoint
ENTRYPOINT ["/app/scripts/build_resume.sh"]
CMD ["My_Resume"]
