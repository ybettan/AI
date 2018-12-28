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


if [[ -e data_files/experiments_extended_alpha_beta.csv ]]; then
    echo WARNING: data_files/experiments_extended_alpha_beta.csv already exist, remove ? [yes, exit]
    read response
    if [[ $response != 'yes' ]]; then
        exit
    fi
    rm data_files/experiments_extended_alpha_beta.csv
fi
touch data_files/experiments_extended_alpha_beta.csv





#==============================================================================
#                               AlphaBetaAgent
#==============================================================================

# random ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p AlphaBetaAgent -q -a depth=$d -l $layout -k $NUM_GHOST -n $N | \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo AlphaBetaAgent,$d,RandomGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_alpha_beta.csv
    echo AlphaBetaAgent, RandomGhost, $layout, depth=$d... DONE.
done

# directional ghosts
echo
for layout in ${LAYOUTS[*]}; do
    start_time=$SECONDS
    res=`python pacman.py -p AlphaBetaAgent -q -a depth=$d -l $layout -k $NUM_GHOST -n $N -g DirectionalGhost| \
         grep Average | \
         cut -d":" -f2`
    end_time=$SECONDS
    avg_score=`echo $res | cut -d" " -f1`
    avg_move_time=`echo $res | cut -d" " -f2`
    avg_total_time=$(((end_time - start_time) / $N))
    echo AlphaBetaAgent,$d,DirectionalGhost,$layout,$avg_score,$avg_move_time,$avg_total_time >> data_files/experiments_extended_alpha_beta.csv
    echo AlphaBetaAgent, DirectionalGhost, $layout, depth=$d... DONE.
done



