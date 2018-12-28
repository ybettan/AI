#!/bin/bash

N=$2
d=4
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


if [[ -e data_files/experiments_extended_random_expectimax_part_1.csv ]]; then
    echo WARNING: data_files/experiments_extended_random_expectimax_part_1.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm data_files/experiments_extended_random_expectimax_part_1.csv
fi
touch data_files/experiments_extended_random_expectimax_part_1.csv





#==============================================================================
#                               RandomExpectimaxAgent
#==============================================================================

# random ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p RandomExpectimaxAgent -q -a depth=$d -l $layout -k $NUM_GHOST -n $N | \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo RandomExpectimaxAgent,$d,RandomGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_random_expectimax_part_1.csv
    echo RandomExpectimaxAgent, RandomGhost, $layout, depth=$d... DONE.
done




