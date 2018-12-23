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


if [[ -e experiments_alpha_beta.csv ]]; then
    echo WARNING: experiments_alpha_beta.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_alpha_beta.csv
fi
touch experiments_alpha_beta.csv



#==============================================================================
#                               AlphaBetaAgent
#==============================================================================

echo
for d in ${DEPTH[*]}; do
    for layout in ${LAYOUTS[*]}; do
        res=`python pacman.py -p AlphaBetaAgent -q -a depth=$d -l $layout \
            -k $NUM_GHOST -n $N | grep Average | cut -d":" -f2`
        avg_score=`echo $res | cut -d" " -f1`
        avg_move_time=`echo $res | cut -d" " -f2`
        echo AlphaBetaAgent,$d,$layout,$avg_score,$avg_move_time >> experiments_alpha_beta.csv
        echo AlphaBetaAgent, $layout, depth=$d... DONE.
    done
    echo
done

