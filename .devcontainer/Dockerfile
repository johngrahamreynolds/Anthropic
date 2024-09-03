# NOTE: this container is rather large to build, primarily because of the python and tex installations 
# (even when tex is truncated to a basic installation as oppossed to the full 7+GB install)
# TODO: build a base image and house it somewhere on a docker/gitlab container registry to optimize non-cached build times

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

# Install texlive for LaTeX, limited to only an essential package scheme
RUN curl -LO https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
    && tar -xzf install-tl-unx.tar.gz \
    && cd install-tl-* \
    && perl ./install-tl --no-interaction --scheme=medium

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

# These build args can be configured from the command line using `uname -m` and `date +%Y` respectively  
# The current computer's instruction set architecture for configuring Tex bins to PATH
ARG ISA=aarch64
# Likewise the current year is needed
ARG YEAR=2024

ENV PATH=$PATH:/root/.local/bin/:/usr/local/texlive/${YEAR}/bin/${ISA}-linux
ENV PYTHONPATH=$PYTHONPATH:/workspaces/Anthropic
ENV ANTHROPIC_API_KEY=redacated!-must-be-set-by-user


