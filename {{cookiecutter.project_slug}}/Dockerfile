{%- for answer, infos in cookiecutter.docker|dictsort %}
{%- if answer == 'y' %}
{%- if infos.docker_compose == 'y' %}
ARG BASE_CONTAINER=python:3.7-buster
FROM $BASE_CONTAINER

ENV USERNAME=lincoln
ARG PUID={{ infos.uid }}
ARG PGID={{ infos.gid }}
ARG WORKDIR=/package
ARG VERSION={{ cookiecutter.version }}
ARG TARGETOS
ARG TARGETARCH
ARG TARGETVARIANT

RUN echo "Image target platform details :: "
RUN echo "TARGETOS:      $TARGETOS"
RUN echo "TARGETARCH:    $TARGETARCH"
RUN echo "TARGETVARIANT: $TARGETVARIANT"

RUN pip install --upgrade pip

RUN groupadd --gid $PGID $USERNAME \
    && useradd --uid $PUID --gid $PGID -d $WORKDIR $USERNAME \
    && chown -R $PUID:$PGID $WORKDIR

COPY requirements.txt .
COPY requirements/* requirements/

RUN pip install -r requirements.txt
{%- endif %}
{%- endif %}
{%- endfor %}