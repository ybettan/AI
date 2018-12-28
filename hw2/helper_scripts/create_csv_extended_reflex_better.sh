#!/bin/bash

N=$2
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


if [[ -e data_files/experiments_extended_reflex_better.csv ]]; then
    echo WARNING: data_files/experiments_extended_reflex_better.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm data_files/experiments_extended_reflex_better.csv
fi
touch data_files/experiments_extended_reflex_better.csv


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

# random ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N | \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo ReflexAgent,1,RandomGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_reflex_better.csv
    echo ReflexAgent, RandomGhost, $layout, depth=1... DONE.
done

# directional ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N -g DirectionalGhost| \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo ReflexAgent,1,DirectionalGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_reflex_better.csv
    echo ReflexAgent, DirectionalGhost, $layout, depth=1... DONE.
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


# random ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N | \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo BetterAgent,1,RandomGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_reflex_better.csv
    echo BetterAgent, RandomGhost, $layout, depth=1... DONE.
done

# directional ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p ReflexAgent -q -l $layout -k $NUM_GHOST -n $N -g DirectionalGhost| \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo BetterAgent,1,DirectionalGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_reflex_better.csv
    echo BetterAgent, DirectionalGhost, $layout, depth=1... DONE.
done
