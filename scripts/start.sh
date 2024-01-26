#!/bin/bash

cd ..
cd config

if [ -e lock.pa ]; then
    cd ../bin_arc/
    sudo python ussr-ssl.py
    exit 0
 else
    echo Install the dependencies first
    sleep 3
    exit 1
fi
