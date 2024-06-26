# geonode-benchmark
a repository containing all sourcecode and data to deploy and run geonode benchmark proposed geonode-benchmark as a contribution for the foss4g 2024 acadmic track

## Deploy Kubernetes GeoNode on Kubernetes (Optional)

requirements:
- helm3
- kubectl
- locust
- har2locust

#### A) use templating to write configuration
```
cp cluster-configuration-template.sh my-cluster-configuration.sh
vim my-cluster-configuration.sh
source my-cluster-configuration.sh


cat values-templates/geonode_half_recommended_resources.yaml | envsubst > geonode-k8s/geonode_half_recommended_resources.yaml
helm dependency build geonode-k8s/
helm upgrade --cleanup-on-fail  --install --namespace geonode-benchmark --create-namespace --values geonode-k8s/geonode_half_recommended_resources.yaml geonode geonode-k8s/
```


#### B) manual edit different helm configurations



####
install https://docs.locust.io/
install https://github.com/SvenskaSpel/har2locust
```
pip install locust har2locust
```

Record your way with chrome dev tool, export .har
Convert har to locustfile
```
har2locust mypath.har > locustfile.py
```

```
locust 

locust --headless --users 10 --spawn-rate 1 -H http://your-server.com

# geonode stable
locust --headless --users 10 --spawn-rate 1 -H https://stable.demo.geonode.org/#/
```
user: number of users
spaw-rate: the speed at which these users are created in the beginning until the specified number of concurrent users are created
H: Host