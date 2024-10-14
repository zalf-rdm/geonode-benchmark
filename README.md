# geonode-benchmark
a repository containing all sourcecode and data to deploy and run geonode benchmark proposed geonode-benchmark as a contribution for the foss4g 2024 acadmic track

## Deploy GeoNode on Kubernetes

requirements:
- helm3
- kubectl

```
# Setup environment variable for deployment and running benchmark
cp cluster-configuration-template.sh my-cluster-configuration.sh
vim my-cluster-configuration.sh
source my-cluster-configuration.sh

cat values-templates/base_values.yaml | envsubst > geonode-k8s/evaluation_base_values.yaml

helm dependency build geonode-k8s/
helm upgrade --cleanup-on-fail  --install --namespace geonode-benchmark --create-namespace --values geonode-k8s/evaluation_base_values.yaml geonode geonode-k8s/
```

add user specific templating into /geonode-k8s/template folder. E.g. tls certificates.

## Initialize GeoNode

```
# prepare python environment
> python -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt

# get familiar with initialize tool
>  python initialize_geonode.py --help
usage: initialize_geonode.py [-h] (--generate-user-file | --create-users-in-geonode | --generate-datasets | --upload-dataset-into-geonode | --delete-all-datasets) [-l] [-v]

options:
  -h, --help            show this help message and exit
  --generate-user-file  generate file with random user credentials in (datsets/users.txt) ...
  --create-users-in-geonode
                        create users in geonode using env variables, like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...
  --generate-datasets   generate datasets ...
  --upload-dataset-into-geonode
                        create datasets in geonode using env variables, like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...
  --delete-all-datasets
                        delete all datasets from geonode instance (all ALL!!!), like in geonodectl (GEONODE_API_BASIC_AUTH: dXNlcjpwYXNzd29yZA== # you can generate this string like: echo -n user:password | base64)...
  -l , --log            Redirect logs to a given file in addition to the console.
  -v, --verbose         Enable verbose logging

# generate user list and create users for benchmarking
python initialize_geonode.py --generate-user-file
python initialize_geonode.py --create-users-in-geonode

# generate datasets and upload them to geonode for benchmark
python initialize_geonode.py --generate-datasets
python initialize_geonode.py --upload-dataset-into-geonode
```

## Evaluation Benchmark

requirements:
- locust

Before running the evaluation benchmarks you can run a simple run of locust using:
```
locust --users 10 --spawn-rate 10 --processes 4 -H $GN_BENCHMARK_EXTERNAL_DOMAIN -f benchmark/
```

For evaluation use: (or check docs: https://docs.locust.io/en/stable/configuration.html)
```
./start-benchmark.sh 
```