#!/bin/bash

for f in temp/*; do
    echo ----------$f-------------
    cat $f
done
