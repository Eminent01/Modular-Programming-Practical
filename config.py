import argparse
from importlib.resources import path

args = argparse.Namespace(
    lr =1e-4,
    bs =32,
    train_size =0.8,
    path ="./data/Images",
    metadata ="./data/metadata_ok.csv",
    wd = 1.0
    )