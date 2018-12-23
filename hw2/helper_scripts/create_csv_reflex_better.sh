#!/bin/bash

N=7
NUM_GHOST=2
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


if [[ -e experiments_reflex_better.csv ]]; then
    echo WARNING: experiments_reflex_better.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm experiments_reflex_better.csv
fi
touch experiments_reflex_better.csv


# make sure ReflexAgent use scoreEvaluationFunciton
echo
echo is ReflexAgent use \'scoreEvaluationFunction\' to evaluate ? [y\\n]
read response
while [[ $response != 'y' ]];do
    echo is ReflexAgent use \'scoreEvaluationFunction\' to evaluate ? [y\\n]
    read response
done




#==============================================================================
#                               ReflexAgent
#==============================================================================

echo
for layout in ${LAYOUTS[*]}; do
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N | \
         grep Average | \
         cut -d":" -f2`
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    echo ReflexAgent,1,$layout,$avg_score,$avg_move_time >> experiments_reflex_better.csv
    echo ReflexAgent, $layout, depth=1... DONE.
done






# make sure ReflexAgent use betterEvaluationFunciton
echo
echo is ReflexAgent use \'betterEvaluationFunction\' to evaluate ? [y\\n]
read response
while [[ $response != 'y' ]];do
    echo is ReflexAgent use \'betterEvaluationFunction\' to evaluate ? [y\\n]
    read response
done

#==============================================================================
#                               BetterAgent
#==============================================================================

echo
for layout in ${LAYOUTS[*]}; do
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N | \
        grep Average | cut -d":" -f2`
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    echo BetterAgent,1,$layout,$avg_score,$avg_move_time >> experiments_reflex_better.csv
    echo BetterAgent, $layout, depth=1... DONE.
done

