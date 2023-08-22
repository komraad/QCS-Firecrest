#!/bin/bash
echo -n "Removing logs and temp files... "
sudo rm -fr logs/client/*.log
sudo rm -fr logs/cluster/*.log
sudo rm -fr logs/firecrest/*.log
sudo rm -fr logs/keycloak/*.log
sudo rm -fr minio/.minio.sys
sudo rm -fr taskpersistence-data/dump.rdb taskpersistence-data/redis.log
echo "done."
