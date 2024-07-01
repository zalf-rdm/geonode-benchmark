# geonode-benchmark
a repository containing all sourcecode and data to deploy and run geonode benchmark proposed geonode-benchmark as a contribution for the foss4g 2024 acadmic track

## Deploy Kubernetes GeoNode on Kubernetes (Optional)

requirements:
- helm3
- kubectl

#### A) use templating to write configuration
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


## Benchmark

requirements:
- locust

To Run:
```
#https://geonode-benchmark.draven.cluster.zalf.de
locust --users 10 --spawn-rate 10 -H https://geonode-benchmark.draven.cluster.zalf.de -f benchmark/geonode-benchmark.py
```