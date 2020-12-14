{%- if cookiecutter.docker == 'y' %}
{%- if cookiecutter.docker_compose == 'y' %}
ARG BASE_CONTAINER=continuumio/miniconda:4.7.12
FROM $BASE_CONTAINER

ARG PUID
ARG PGID
ARG USERNAME=lincoln
ARG WORKDIR=/package
ARG VERSION={{ cookiecutter.version }}
ARG TARGETOS
ARG TARGETARCH
ARG TARGETVARIANT

RUN echo "Image target platform details :: "
RUN echo "TARGETOS:      $TARGETOS"
RUN echo "TARGETARCH:    $TARGETARCH"
RUN echo "TARGETVARIANT: $TARGETVARIANT"

WORKDIR $WORKDIR

COPY environment.yml .
COPY requirements/* requirements/

RUN conda env create -f environment.yml

ENV SHELL="conda run -n {{ cookiecutter.project_name.lower().replace(' ', '-') }} /bin/bash -c"
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

RUN groupadd --gid $PGID $USERNAME \
    && useradd --uid $PUID --gid $PGID -m $USERNAME \
    && chown -R $PUID:$PGID $WORKDIR

{%- endif %}
{%- endif %}
