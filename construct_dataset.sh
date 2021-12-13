#!/bin/bash

data=data/$1
count=$(ls $data | wc -l)

for i in $(seq $count);
    do
        files=$(ls $data/$i/ | wc -l)
        ((files=files-1))
        for j in $(seq 0 $files);
            #do python3 label_text.py --preds preds2/$1/$i/$1.$j.preds.npy --labels preds2/$1/$i/$1.$j.class_labels.npy --text ../hugging/datasets/$1/$i/$1.tsv.$j --probs preds2/$1/$i/$1.$j.probs.npy --save_to $data/$1.jsonl
            do python3 label_text.py --preds output/$1/$i/$1.$j.preds.npy --labels output/$1/$i/$1.$j.class_labels.npy --text data/$1/$i/$1.tsv.$j --save_to $data/$1.jsonl
            done
    done


#python3 label_text.py --preds preds/ar/1/ar.0.preds.npy --labels preds/ar/1/ar.0.class_labels.npy --text ../hugging/datasets/ar/1/ar.tsv.0