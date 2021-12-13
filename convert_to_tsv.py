from os import sep
import pandas as pd
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def argparser():
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument('--lang', default=None,
                    help='target language code')
    return ap

def main(argv):
    options = argparser().parse_args(argv[1:])
    print("Reading")
    df = pd.read_csv(f'data/{options.lang}.csv', chunksize=10000,low_memory=False, usecols=['id, text'])
    with open(f'data/{options.lang}.tsv', 'w') as f:
        for chunk in df:
            for row in chunk.itertuples(index=False):
                id = row.id
                text = row.text.replace('\n', '') if type(row.text) == str else row.text
                f.write(f'{id}\t{text}\n')
                print(f"Writing {id}")
                
if __name__ == '__main__':
    sys.exit(main(sys.argv))
