# ----------- Stage 1: Builder -----------
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# ----------- Stage 2: Final Image -----------
FROM python:3.13-slim

ENV PATH="/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup --system pygroup && \
    adduser --system --ingroup pygroup pyuser

WORKDIR /app

# Copy virtual environment and app code
COPY --from=builder /venv /venv
COPY . .

# Change ownership to the non-root user
RUN chown -R pyuser:pygroup /app

# Switch to non-root user
USER pyuser

EXPOSE 8000

CMD ["uvicorn", "gptsvc:main.app", "--host", "0.0.0.0", "--port", "8000"]
