#!/bin/bash
TIMESTAMP="$1"

kubectl logs geonode-geonode-0 -c geonode > results/$TIMESTAMP-geonode.log
kubectl logs geonode-geonode-0 -c celery > results/$TIMESTAMP-celery.log
kubectl logs geonode-geoserver-0 -c geoserver > results/$TIMESTAMP-geoserver.log
kubectl logs geonode-memcached-0 > results/$TIMESTAMP-memcached.log
nginx_pod=`kubectl get pods | grep nginx | awk -F " " '{ print $1 }'`
kubectl logs "$nginx_pod" > results/$TIMESTAMP-nginx.log
kubectl logs geonode-pycsw-0 -c pycsw > results/$TIMESTAMP-pycsw.log
kubectl logs geonode-rabbitmq-0 -c rabbitmq > results/$TIMESTAMP-rabbitmq.log
kubectl logs geonode-postgres-0 > results/$TIMESTAMP-postgres.log
