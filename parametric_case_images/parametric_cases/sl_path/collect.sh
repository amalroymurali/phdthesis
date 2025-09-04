ls .. | grep AOA | grep .png | grep -v _ |xargs -I {} cp ../{} .
 
ls .. | grep AOA | grep .png | grep -v _ > cases.txt
sed -i "s|.png||g" cases.txt
