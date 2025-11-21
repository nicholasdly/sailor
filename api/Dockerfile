FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "--port", "8000"]
