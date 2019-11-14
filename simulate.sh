#! /bin/bash
TEMP_FILE="tmp.txt"


for i in $(seq 100); do python simu.py 100 20 20 20 ; done > ${TEMP_FILE}
cat ${TEMP_FILE} | grep True | wc -l 