#!/bin/bash

namespace=$1

pods_str=$(kubectl get pods -o json | jq -r ".items[].metadata.name")
pods_arr=($pods_str)
echo "name, cpu, mem, timestamp"
while true; do 
  EPOCH=$(date +%s)
  for pod in ${pods_arr[@]}; do
      pods_str=$(kubectl get pods -o json | jq -r ".items[].metadata.name")
      pods_arr=($pods_str)
      kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/$namespace/pods/$pod |  jq  -r  --arg EPOCH "$EPOCH" '.containers[] | [ .name, .usage.cpu, .usage.memory, $EPOCH] | @csv'
  done
  sleep 1
done
