#!/bin/bash

if [[ -e experiments.csv ]]; then
    echo WARNING: experiments.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments.csv
fi
touch experiments.csv


# read experiments_reflex_better.csv
while read line; do
    echo $line >> experiments.csv
done < experiments_reflex_better.csv


# read experiments_minimax.csv
while read line; do
    echo $line >> experiments.csv
done < experiments_minimax.csv


# read experiments_alpha_beta.csv
while read line; do
    echo $line >> experiments.csv
done < experiments_alpha_beta.csv


# read experiments_random_expectimax.csv
while read line; do
    echo $line >> experiments.csv
done < experiments_random_expectimax.csv


#FIXME: uncomment
## remove all temporary files
#rm experiments_reflex_better.csv
#rm experiments_minimax.csv
#rm experiments_alpha_beta.csv
#rm experiments_random_expectimax.csv


