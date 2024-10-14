#!/bin/bash


# checklist:
#  - load venv
#  - connect correct cluster
#  - connect correct context
#  - load benchmark-configuration.sh

source benchmark-configuration.sh
export LOCUST_TESTNAME=`date +%Y%m%d%H%M%S`;

./monitor.sh $GN_BENCHMARK_NAMESPACE > "results/$LOCUST_TESTNAME-monitoring.log" &
processId=$!


  # --processes 4 \

locust \
  -f benchmark/ \
  --headless \
  --users 100 \
  --spawn-rate 0.1666 \
  --run-time 10m \
  --stop-timeout 10s \
  -H "$GN_BENCHMARK_EXTERNAL_DOMAIN" \
  --csv "results/$LOCUST_TESTNAME.csv" \
  --html "results/$LOCUST_TESTNAME.html" \
  --loglevel INFO \
  --logfile "results/$LOCUST_TESTNAME.log"
  
kill $processId