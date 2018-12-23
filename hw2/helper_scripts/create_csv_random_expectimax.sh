#!/bin/bash

N=7
NUM_GHOST=2
DEPTH=(2 3 4)
LAYOUTS=("capsuleClassic" \
         "contestClassic" \
         "mediumClassic" \
         "minimaxClassic" \
         "openClassic" \
         "originalClassic" \
         "smallClassic" \
         "testClassic" \
         "trappedClassic" \
         "trickyClassic" )

echo ==========================================================================
echo make sure you have:
echo \"print\('Average move time:', pacman.time_total_actions/float\(pacman.num_actions\)\)\"
echo in pacman.py line 647 
echo ==========================================================================
echo


if [[ -e experiments_random_expectimax.csv ]]; then
    echo WARNING: experiments_random_expectimax.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_random_expectimax.csv
fi
touch experiments_random_expectimax.csv


#==============================================================================
#                          RandomExpectimaxAgent
#==============================================================================

echo
for d in ${DEPTH[*]}; do
    for layout in ${LAYOUTS[*]}; do
        res=`python pacman.py -p RandomExpectimaxAgent -q -a depth=$d -l $layout \
            -k $NUM_GHOST -n $N | grep Average | cut -d":" -f2`
        avg_score=`echo $res | cut -d" " -f1`
        avg_move_time=`echo $res | cut -d" " -f2`
        echo RandomExpectimaxAgent,$d,$layout,$avg_score,$avg_move_time >> experiments_random_expectimax.csv
        echo RandomExpectimaxAgent, $layout, depth=$d... DONE.
    done
    echo
done



