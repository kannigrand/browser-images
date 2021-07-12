ARG VERSION
#### STAGE 1: probuilder ###
FROM kannigrand/proxybound_prebuilder:1.1 AS prebuilder

#### STAGE 2: builder ###
FROM selenoid/firefox:$VERSION

ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
COPY proxybound.conf /etc/proxybound.conf
COPY entrypoint$VERSION.sh /entrypoint.sh
COPY --from=prebuilder /usr/local/bin/proxybound ./usr/local/bin/
COPY --from=prebuilder /usr/local/lib/libproxybound.so ./usr/local/lib/

USER root

RUN chmod +x /usr/local/lib/libproxybound.so && chmod +x /usr/local/bin/proxybound && chmod 777 /etc/proxybound.conf

USER selenium

EXPOSE 4444
ENTRYPOINT ["/entrypoint.sh"]