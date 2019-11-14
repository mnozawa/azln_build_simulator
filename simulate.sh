#! /bin/bash
TEMP_FILE="tmp.txt"

TRY_POPULATION=$1
TRY_TIMES=$2
PROBABILITY_TO_BUILD=${@:3:($#-2)}

for i in $(seq ${TRY_POPULATION}); do python simu.py ${TRY_TIMES} ${PROBABILITY_TO_BUILD} ; done > ${TEMP_FILE}
cat ${TEMP_FILE} | grep True | wc -l 