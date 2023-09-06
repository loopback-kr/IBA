# Python built-in libs for handling filesystems
import sys, os, json, pickle, csv, re, random, logging, importlib, argparse
from os.path import join, basename, exists, splitext, dirname, isdir, isfile
from pathlib import Path
from shutil import copy, copytree, rmtree
from copy import deepcopy
from glob import glob, iglob


TRAIN_DIR = "~/data/ILSVRC2012_img_train"
TRAIN_DIR = "imagenet/train"
VALID_DIR = "~/data/ILSVRC2012_img_valid"
VALID_DIR = "imagenet/validation"



if __name__ == '__main__':
    classes = sorted(glob(join(TRAIN_DIR, '*')))
    assert len(classes) == 1000
    assert all([isdir(cls) for cls in classes])

    classes = [basename(cls) for cls in classes]
    [os.makedirs(join(VALID_DIR, cls), exist_ok=True) for cls in classes]

    with open('make_val_directory.txt') as f:
        fname, target_dir = f.readline().split(' ')
        os.rename(join(VALID_DIR, fname), join(VALID_DIR, target_dir, fname))
