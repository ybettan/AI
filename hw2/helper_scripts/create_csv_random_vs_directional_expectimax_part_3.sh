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


if [[ -e experiments_random_vs_directional_expectimax_part_3.csv ]]; then
    echo WARNING: experiments_random_vs_directional_expectimax_part_3.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_random_vs_directional_expectimax_part_3.csv
fi
touch experiments_random_vs_directional_expectimax_part_3.csv




echo
res=`python pacman.py -p DirectionalExpectimaxAgent -q -a depth=$DEPTH -l $LAYOUT \
    -g RandomGhost -k $NUM_GHOSTS -n $N | grep Average | cut -d":" -f2`
avg_score=`echo $res | cut -d" " -f1`
avg_move_time=`echo $res | cut -d" " -f2`
echo DirectionalExpectimaxAgent,RandomGhost,$avg_score,$avg_move_time >> experiments_random_vs_directional_expectimax_part_3.csv
echo DirectionalExpectimaxAgent, RandomGhost... DONE.




