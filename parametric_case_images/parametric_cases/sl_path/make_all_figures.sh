#!/bin/bash

echo Run this only with bash and not sh
rm allfigures.tex
casenum=4
while read -r casename; do
cat template | sed -e "s|casename|$casename|g" \
				   -e "s|casenum|$casenum|g" >> allfigures.tex
((casenum=$casenum+1))
echo "casenum is now: $casenum" 

done < cases.txt
