#!/bin/bash

if [[ -e data_files/experiments_extended.csv ]]; then
    echo WARNING: data_files/experiments_extended.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm data_files/experiments_extended.csv
fi
touch data_files/experiments_extended.csv


# read experiments_extended_reflex_better.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_reflex_better.csv


# read experiments_extended_alpha_beta.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_alpha_beta.csv


# read experiments_extended_random_expectimax.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_random_expectimax_part_1.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_random_expectimax_part_2.csv


# read experiments_extended_directional_expectimax.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_directional_expectimax_part_1.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_directional_expectimax_part_2.csv


# read experiments_extended_competition.csv
while read line; do
    echo $line >> data_files/experiments_extended.csv
done < data_files/experiments_extended_competition.csv


## remove all temporary files
#rm data_files/experiments_extended_reflex_better.csv
#rm data_files/experiments_extended_minimax.csv
#rm data_files/experiments_extended_alpha_beta.csv
#rm data_files/experiments_extended_random_expectimax.csv




