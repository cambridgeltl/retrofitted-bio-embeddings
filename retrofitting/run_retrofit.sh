#!/bin/bash

LEXDIR="lexicons/updated/1/"
WVDIR="input_vec/wiki-win-1.bin"
OUTDIR="output_vec/"

iters=("20")
thr=("5e-1")

for d in "$LEXDIR"/*.txt; do
	for i in "${iters[@]}" ; do
		for j in "${thr[@]}" ; do
			echo 'iters, thr, lex: ' $i $j, $d
			inFilestr=${d##*/}
			wvFile=${WVDIR##*/}
			#echo $inFilestr
			filePath=$wvFile.rf.it.$i.thr.$j.l.$inFilestr
			echo $filePath 
			python retrofit_3.py -i $WVDIR -l $d -o $OUTDIR/$filePath.bin -n $i -t $j
			echo
		done
	done
done