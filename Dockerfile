# Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ENV PYTHONUNBUFFERED=1
# Put the project environment outside /app so the host mount can't clobber it
ENV UV_PROJECT_ENVIRONMENT=/venv
# (optional) make the venv active on PATH
ENV PATH="/venv/bin:${PATH}"

WORKDIR /app

# Copy metadata first for caching
COPY pyproject.toml uv.lock* ./

# Install dependencies once at build time
RUN uv sync --frozen

# Copy app code
COPY . .

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
