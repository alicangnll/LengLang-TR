#!/bin/bash

for file in tests/dene.c
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
    
    
	    

