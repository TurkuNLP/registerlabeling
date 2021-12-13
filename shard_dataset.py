from tqdm.auto import tqdm
import os
import sys

SHARD_SIZE = 1 << 30  # 1GB


def iter_batches(path: str, batch_size=SHARD_SIZE):
    with open(path, "rb") as f:
        while True:
            batch = f.read(batch_size)
            if not batch:
                break
            batch += f.readline()  # finish current line
            yield batch


if __name__ == "__main__":

    path = sys.argv[1]
    extension = path[path.rindex("."):]
    approx_total = os.path.getsize(path) // SHARD_SIZE + 1
    for i, batch in enumerate(tqdm(iter_batches(path), unit="shard", total=approx_total)):
        with open(path[:-len(extension)] + f"_{i:05}{extension}", 'wb') as f:
            f.write(batch)