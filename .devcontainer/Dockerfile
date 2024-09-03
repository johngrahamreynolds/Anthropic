FROM ubuntu:22.04

ARG PYTHON_VERSION=3.10.12

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /tmp/dockerbuild \
    && cd /tmp/dockerbuild \ 
    && apt-get update \
    # Install supporting packages
    && apt-get -y install --no-install-recommends \
        apt-utils \
        ca-certificates \
        curl \
        dialog \
        gnupg \
        lsb-release \
    && apt-get update && apt-get -y install \
        build-essential \
        gettext-base \
        git \
        libbz2-dev \
        libffi-dev \
        libgdbm-dev \
        libncurses5-dev \
        libnss3-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        unixodbc-dev \
        unzip \
        zip \
        zlib1g-dev

# Install Python, poetry
RUN curl -O https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz \
    && tar -xf Python-$PYTHON_VERSION.tar.xz \
    && cd Python-$PYTHON_VERSION && ./configure --enable-optimizations \
    && make install \
    # Install poetry
    && curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/dockerbuild

# Set Workspace directory
ARG WORKSPACE=/workspaces/Anthropic
ENV WORKSPACE=${WORKSPACE}

COPY poetry.lock pyproject.toml ${WORKSPACE}/
# RUN cd $WORKSPACE && poetry install --no-root

WORKDIR ${WORKSPACE}

ENV PATH=$PATH:/root/.local/bin/
ENV PYTHONPATH=$PYTHONPATH:/workspaces/Anthropic
ENV ANTHROPIC_API_KEY=redacated!-must-be-set-by-user


