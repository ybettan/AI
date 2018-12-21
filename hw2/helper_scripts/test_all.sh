#!/bin/bash

N=$2

echo ==========================================================================
echo "                          ReflexAgent"
echo ==========================================================================
./helper_scripts/test_reflex_agent.sh -n $N





echo ==========================================================================
echo "                          MinimaxAgent, D=0"
echo ==========================================================================
./helper_scripts/test_minimax_agent.sh -n $N -d 0

echo ==========================================================================
echo "                          MinimaxAgent, D=1"
echo ==========================================================================
./helper_scripts/test_minimax_agent.sh -n $N -d 1

echo ==========================================================================
echo "                          MinimaxAgent, D=2"
echo ==========================================================================
./helper_scripts/test_minimax_agent.sh -n $N -d 2

echo ==========================================================================
echo "                          MinimaxAgent, D=3"
echo ==========================================================================
./helper_scripts/test_minimax_agent.sh -n $N -d 3





echo ==========================================================================
echo "                      AlphaBetaAgent, D=0"
echo ==========================================================================
./helper_scripts/test_alpha_beta_agent.sh -n $N -d 0

echo ==========================================================================
echo "                      AlphaBetaAgent, D=1"
echo ==========================================================================
./helper_scripts/test_alpha_beta_agent.sh -n $N -d 1

echo ==========================================================================
echo "                      AlphaBetaAgent, D=2"
echo ==========================================================================
./helper_scripts/test_alpha_beta_agent.sh -n $N -d 2

echo ==========================================================================
echo "                      AlphaBetaAgent, D=3"
echo ==========================================================================
./helper_scripts/test_alpha_beta_agent.sh -n $N -d 3






echo ==========================================================================
echo "                      RandomExpectimaxAgent, D=0"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 0 -a RandomExpectimaxAgent

echo ==========================================================================
echo "                      RandomExpectimaxAgent, D=1"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 1 -a RandomExpectimaxAgent

echo ==========================================================================
echo "                      RandomExpectimaxAgent, D=2"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 2 -a RandomExpectimaxAgent

echo ==========================================================================
echo "                      RandomExpectimaxAgent, D=3"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 3 -a RandomExpectimaxAgent





echo ==========================================================================
echo "                      DirectionalExpectimaxAgent, D=0"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 0 -a DirectionalExpectimaxAgent

echo ==========================================================================
echo "                      DirectionalExpectimaxAgent, D=1"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 1 -a DirectionalExpectimaxAgent

echo ==========================================================================
echo "                      DirectionalExpectimaxAgent, D=2"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 2 -a DirectionalExpectimaxAgent

echo ==========================================================================
echo "                      DirectionalExpectimaxAgent, D=3"
echo ==========================================================================
./helper_scripts/test_expectimax_agent.sh -n $N -d 3 -a DirectionalExpectimaxAgent



