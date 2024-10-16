#!/bin/sh

# Errors are fatal
set -e

cd /mnt

if test "$1" = "bash" -o "$1" == "sh"
then
    echo "# "
    echo "# Welcome to the development container!"
    echo "# "
    echo "# Your files are in /mnt"
    echo "# "
    echo "# Argument specified! Executing command: $@"
    echo "# "

    exec $@
fi

/app/pdf-to-poster.py $@

