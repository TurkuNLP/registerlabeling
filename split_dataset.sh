#!/bin/bash

# $1 = language code for the target language, e.g en

mkdir -p data/$1
split -d -C 500M data/$1.tsv data/$1/$1.tsv.
count=$(ls data/$1 | wc -l)
splits=$(($count / 200))

if [ $splits -lt 1 ]; then
    splits=1;
fi

echo $splits
for i in `seq $splits`;
    do
        mkdir -p data/$1/$i;
        files=$(ls data/$1/*.tsv.* | head -n 200)
        fc=0
        for file in $files;
            do echo $i; echo $file;
            mv $file data/$1/$i/$1.tsv.$fc;
            ((fc=fc+1))
            done
        done
