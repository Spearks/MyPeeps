FROM python:3.11-slim-bullseye AS build
ARG TARGETARCH

WORKDIR /app

COPY pyproject.toml pyproject.toml
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN PYTHONPATH=${PYTHONPATH}:${PWD} pip3 install poetry
RUN poetry config virtualenvs.create false
RUN if [ $TARGETARCH = "arm64" ]; then \
        apt-get update && apt-get install -y python3-dev gcc \
    ; fi

RUN poetry install --no-dev

COPY . .

RUN chmod +x /app/runner.sh

ENTRYPOINT [ "bash" ]
CMD ["/app/runner.sh"]   