import os, json
import numpy as np
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from numpy.core.defchararray import index

def argparser():
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument('--text', default=None,
                    help='input file')
    ap.add_argument('--preds', default=None,
                    help='input file')
    ap.add_argument('--probs', default=None,
                    help='input file', required=False)
    ap.add_argument('--labels', default=None,
                    help='input file')
    ap.add_argument('--save_to', default=None,
                    help='input file')
    return ap

def map_to_label(fn, labels):
    multilabels = []
    for row in fn:
        label_names = []
        for index, label in enumerate(row):
            if label == 1:
                label_names.append(labels[index])
        #multilabels.append(''.join(label_names) if len(label_names) <= 1 else 'HYB')
        #multilabels.append('_'.join(label_names))
        multilabels.append(label_names)
    return multilabels

def main(argv):
    options = argparser().parse_args(argv[1:])

    preds = np.load(options.preds, allow_pickle=True)
    labels = np.load(options.labels, allow_pickle=True)
    probs = np.load(options.probs, allow_pickle=True) if options.probs else None
    pred_l = map_to_label(preds, labels)
    labels = [label for label in labels]
    #print(preds)
    
    with open(options.text, 'r', encoding='utf-8') as f, open(options.save_to, 'a', encoding='utf-8') as jf:
        text = [line for line in f]
        
        for i, line in enumerate(text):
            line = line.split('\t', 1)
            print(labels)
            #print(probs[i])

            #label = pred_l[i]
            label_index = [labels.index(label) for label in pred_l[i]] 
            print(label_index)
            label_probs = [str(probs[i][x]) for x in label_index]  if probs else None
            #print(label_probs)

            if label_probs:
                j_line = {'id': line[0], 'probs': label_probs, 'labels': pred_l[i], 'text': line[1]}
                print(j_line)
            else:
                j_line = {'id': line[0], 'labels': pred_l[i], 'text': line[1]}
            #json.dump(json.dumps(j_line), jf, ensure_ascii=False)
            json_string = json.dumps(j_line, ensure_ascii=False)
            jf.write(json_string + "\n")

        if len(text) != preds.shape[0]:
            print(f"Length of {options.text} does not match length of {options.preds}")
            print(f"{len(text)}, {preds.shape[0]}")
        #for i, pred in enumerate(preds):
            #print(pred) 

if __name__ == '__main__':
    sys.exit(main(sys.argv))