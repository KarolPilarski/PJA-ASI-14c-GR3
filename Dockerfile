FROM python:3.9-slim

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip

ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker
WORKDIR /home/kedro_docker

COPY . /home/kedro_docker
USER kedro_docker

FROM python:3.9-slim

ARG KEDRO_UID=999
ARG KEDRO_GID=0
COPY --chown=${KEDRO_UID}:${KEDRO_GID} . .
RUN apt-get update -y && apt-get install -y gcc
RUN pip install --no-cache-dir -r environment.yml&& rm -f environment.yml
EXPOSE 8888

CMD ["kedro", "run"]
