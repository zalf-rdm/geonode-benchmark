import argparse
import logging
import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def configure_logging(debug, filename=None):
    """define loglevel and log to file or to std"""
    if filename is None:
        if debug:
            logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)
        else:
            logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    else:
        if debug:
            logging.basicConfig(
                filename=filename, format="%(asctime)s %(message)s", level=logging.DEBUG
            )
        else:
            logging.basicConfig(
                filename=filename, format="%(asctime)s %(message)s", level=logging.INFO
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        dest="host",
        type=str,
        required=True,
        help="goldilocks api endoint for desired namespace ... e.g. https://goldilocks.draven.cluster.zalf.de/api/geonode-benchmark",
    )

    parser.add_argument(
        "--skip-host-validation",
        dest="skip_host_validation",
        action="store_true",
        help="skip ssl certificate validation ...",
    )

    # parser.add_argument(
    #     "--output",
    #     dest="output_type",
    #     type=str,
    #     choices=["json", "yaml", "table"],
    #     help="define output format ... (json,yaml,table)",
    # )

    # logging
    parser.add_argument(
        "-l",
        "--log",
        help="Redirect logs to a given file in addition to the console.",
        metavar="",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()
    debug = False
    if args.verbose:
        debug = True

    if args.log:
        logfile = args.log
        configure_logging(debug, logfile)
    else:
        configure_logging(debug)
        logging.debug("debug mode enabled")

    logging.debug(f"reading json from {args.host} ...")

    url = args.host
    ssl_verify = not args.skip_host_validation
    try:
        r = requests.get(url, verify=ssl_verify)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    result_json = r.json()
    namespace = url.split("/")[-1]
    workloads = result_json["Namespaces"][namespace]["workloads"]
    f_json = {}
    # print(workloads)
    for workload, content in workloads.items():
        # breakpoint()
        for name, container in content["containers"].items():
            f_json[name] = container
            for d in [
                "BasePath",
                "BurstableCost",
                "BurstableCostInt",
                "ContainerCost",
                "ContainerCostInt",
                "GuaranteedCost",
                "GuaranteedCostInt",
                "containerName",
            ]:
                del f_json[name][d]

    print(json.dumps(f_json, indent=2))
    # logging.info(r.json())


if __name__ == "__main__":
    main()
