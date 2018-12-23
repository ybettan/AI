#!/bin/bash


if [[ -e experiments_random_vs_directional_expectimax.csv ]]; then
    echo WARNING: experiments_random_vs_directional_expectimax.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_random_vs_directional_expectimax.csv
fi
touch experiments_random_vs_directional_expectimax.csv


# read part_1
while read line; do
    echo $line >> experiments_random_vs_directional_expectimax.csv
done < experiments_random_vs_directional_expectimax_part_1.csv


# read part_2
while read line; do
    echo $line >> experiments_random_vs_directional_expectimax.csv
done < experiments_random_vs_directional_expectimax_part_2.csv


# read part_3
while read line; do
    echo $line >> experiments_random_vs_directional_expectimax.csv
done < experiments_random_vs_directional_expectimax_part_3.csv


# read part_4
while read line; do
    echo $line >> experiments_random_vs_directional_expectimax.csv
done < experiments_random_vs_directional_expectimax_part_4.csv


#FIXME: uncomment
## remove all temporary files
#rm experiments_reflex_better.csv
#rm experiments_minimax.csv
#rm experiments_alpha_beta.csv
#rm experiments_random_expectimax.csv


