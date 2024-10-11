#!/bin/bash
#
# Push our Docker image our Docker Hub.
#

# Errors are fatal
set -e

# Change to the parent directory of this script
pushd $(dirname $0)/.. > /dev/null

docker tag pdf-to-poster dmuth1/pdf-to-poster
docker push dmuth1/pdf-to-poster


