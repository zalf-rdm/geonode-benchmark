# geonode-benchmark
a repository containing all sourcecode and data to deploy and run geonode benchmark proposed geonode-benchmark as a contribution for the foss4g 2024 acadmic track

## Deploy Kubernetes GeoNode on Kubernetes (Optional)

requirements:
- helm3
- kubectl

#### A) use templating to write configuration and deploy your GeoNode Kubernetes installation
```
cp cluster-configuration-template.sh my-cluster-configuration.sh
vim my-cluster-configuration.sh
source my-cluster-configuration.sh

cat values-templates/geonode_half_recommended_resources.yaml | envsubst > geonode-k8s/geonode_half_recommended-values.yaml
helm dependency build geonode-k8s/
helm upgrade --cleanup-on-fail  --install --namespace geonode-benchmark --create-namespace --values geonode-k8s/geonode_half_recommended-values.yaml geonode geonode-k8s/
```
add user specific templating into /geonode-k8s/template folder. E.g. tls certificates.

To Delete the deployment use:
```
helm delete geonode geonode-k8s
```

#### B) ...


## simple Benchmark

requirements:
- locust

To simply run locust use something like (or check docs: https://docs.locust.io/en/stable/configuration.html):
```
locust --users 10 --spawn-rate 10 --processes 4 -H $GN_BENCHMARK_EXTERNAL_DOMAIN -f benchmark/
```

```
 LOCUST_TESTNAME==test1; locust
  --processes 4
  --headless
  --users 100
  --spawn-rate 0.033333333 
  --run-time 52m 
  --stop-timeout 10s
  -H "$GN_BENCHMARK_EXTERNAL_DOMAIN"
  --csv "results/$LOCUST_TESTNAME.csv"
  --html "results/$LOCUST_TESTNAME.html"
  --loglevel INFO
  --logfile "results/$LOCUST_TESTNAME.log"
  --locustfile benchmark/