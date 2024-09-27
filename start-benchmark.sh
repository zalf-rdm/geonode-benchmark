#!/bin/bash


# checklist:
#  - load venv
#  - connect correct cluster
#  - connect correct context
#  - load benchmark-configuration.sh

source benchmark-configuration.sh
export LOCUST_TESTNAME=`date +%Y%m%d%H%M%S`;

./monitor.sh $GN_BENCHMARK_NAMESPACE > "results/monitoring_$LOCUST_TESTNAME.log" &
processId=$!

locust \
  --processes 4 \
  -f benchmark/ \
  --autostart \
  --users 500 \
  --spawn-rate 1 \
  --run-time 30m \
  --stop-timeout 10s \
  -H "$GN_BENCHMARK_EXTERNAL_DOMAIN" \
  --csv "results/$LOCUST_TESTNAME.csv" \
  --html "results/$LOCUST_TESTNAME.html" \
  --loglevel INFO \
  --logfile "results/$LOCUST_TESTNAME.log"
  
kill $processId