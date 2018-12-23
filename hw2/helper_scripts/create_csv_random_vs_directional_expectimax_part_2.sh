#!/bin/bash

N=5
NUM_GHOSTS=2
DEPTH=4
LAYOUT="trickyClassic"

echo ==========================================================================
echo make sure you have:
echo \"print\('Average move time:', pacman.time_total_actions/float\(pacman.num_actions\)\)\"
echo in pacman.py line 647 
echo ==========================================================================
echo


if [[ -e experiments_random_vs_directional_expectimax_part_2.csv ]]; then
    echo WARNING: experiments_random_vs_directional_expectimax_part_2.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_random_vs_directional_expectimax_part_2.csv
fi
touch experiments_random_vs_directional_expectimax_part_2.csv




echo
res=`python pacman.py -p RandomExpectimaxAgent -q -a depth=$DEPTH -l $LAYOUT \
    -g DirectionalGhost -k $NUM_GHOSTS -n $N | grep Average | cut -d":" -f2`
avg_score=`echo $res | cut -d" " -f1`
avg_move_time=`echo $res | cut -d" " -f2`
echo RandomExpectimaxAgent,DirectionalGhost,$avg_score,$avg_move_time >> experiments_random_vs_directional_expectimax_part_2.csv
echo RandomExpectimaxAgent, DirectionalGhost... DONE.



