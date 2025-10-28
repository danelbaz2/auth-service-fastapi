# Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy metadata first (for caching)
COPY pyproject.toml uv.lock* ./

# Install dependencies into system environment
RUN uv sync

# Copy your code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Default command to run your app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
