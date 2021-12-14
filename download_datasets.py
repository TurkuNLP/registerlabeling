from datasets import load_dataset
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from pathlib import Path

def argparser():
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument('--lang', default=None,
                    help='dataset to download')
    return ap

def main(argv):
    options = argparser().parse_args(argv[1:])

    Path("./data").mkdir(parents=True, exist_ok=True)

    dataset = load_dataset('oscar', f'unshuffled_deduplicated_{options.lang}', cache_dir='./data', split='train')
    dataset.to_csv(f'./data/{options.lang}.csv')
    
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))