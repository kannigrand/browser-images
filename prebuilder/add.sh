#!/bin/bash

if [ -n "$PR_FULL" ]
then
  echo "$PR_FULL" >> /etc/proxybound.conf
  echo "proxybound config installed"
  echo "$PR_FULL"
  export PROXYBOUND_QUIET_MODE="1"
  export LD_PRELOAD=/usr/local/lib/libproxybound.so
  export PROXYBOUND_CONF_FILE=/etc/proxybound.conf
else
  echo "PR_FULL is null"
fi