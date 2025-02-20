# Use official Python 3.12 image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=true

# Install poetry
RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to PATH
ENV PATH="${POETRY_HOME}/bin:${PATH}"

# Set working directory
WORKDIR /backend

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy project files
COPY . .

# Set the command to run your application
CMD ["poetry", "run", "python", "main.py"]
