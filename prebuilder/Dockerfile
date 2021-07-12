FROM ubuntu

RUN apt update -y && apt full-upgrade -y && \
    apt install git make gcc -y && \
    cd home && \
    git clone https://github.com/kannigrand/Proxybound.git && \
    cd Proxybound && \
    ./configure && \
    make && \
    make install

COPY proxybound.conf /etc/proxybound.conf



