ARG BASE_IMAGE=python:3.11.8
FROM $BASE_IMAGE as runtime-environment

# install essential libraries
RUN apt-get update && apt-get install -y build-essential

# install project requirements
COPY env/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# install AutoGluon
RUN pip install autogluon --no-cache

# add kedro user
ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
    useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker

WORKDIR /home/kedro_docker
USER kedro_docker

FROM runtime-environment

# copy project
ARG KEDRO_UID=999
ARG KEDRO_GID=0
COPY --chown=${KEDRO_UID}:${KEDRO_GID} . .

EXPOSE 8888

# run project
CMD ["kedro", "run"]
