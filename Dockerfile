FROM python:3.12-alpine

# Install curl (needed for uv sometimes)
RUN apk add --no-cache curl

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project into container
COPY . .

# Create virtual environment and install dependencies
RUN uv venv && \
    . .venv/bin/activate && \
    uv sync --all-groups

# Run tests
RUN . .venv/bin/activate && pytest

# Run your calculator
CMD [".venv/bin/python", "-m", "src.calculator.calculator"]