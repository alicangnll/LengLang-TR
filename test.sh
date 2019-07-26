#!/bin/bash

for file in dene.lng
do
    if [ $(python3 lenglang.py $file |  grep "Bitti.") ]
    then
	if eval ${file%.*}
	then
	    :
	else
	    echo "${file%.*} başarıyla derlendi."
	fi
    else
	echo "$file derleme hatası."
    fi
done
    
    
	    

