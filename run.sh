#!/bin/bash

benchmarks=(600.perlbench_s-570B.champsimtrace.xz 605.mcf_s-994B.champsimtrace.xz 620.omnetpp_s-141B.champsimtrace.xz 641.leela_s-1083B.champsimtrace.xz 657.xz_s-2302B.champsimtrace.xz)

cd ChampSim

# #baseline
# ./build_champsim.sh bimodal no no no no lru 1

# for i in "${benchmarks[@]}"
# do
# 	./run_champsim.sh bimodal-no-no-no-no-lru-1core 10 10 "$i"
# done


#with L1D ipcp
./build_champsim.sh bimodal no bingo_dpc3 next_line next_line lru 1

for i in "${benchmarks[@]}"
do
	./run_champsim.sh bimodal-no-bingo_dpc3-next_line-next_line-lru-1core 10 10 "$i"
done

