FROM alpine

LABEL maintainer="Jim Wright <jmwri93@gmail.com>"
LABEL description="RuneHistory CLI"

RUN apk add --no-cache \
    python3 \
    python3-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install runehistory-cli && \
    rm -r /root/.cache

COPY . /app
WORKDIR /app

ENTRYPOINT ["runehistory"]
CMD ["poll"]
