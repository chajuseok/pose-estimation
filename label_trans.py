import argparse
import os
import numpy as np
import json
from torch.utils.data import Dataset
import pickle
from tqdm import tqdm
import shutil
import copy


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Kinetics-skeleton Data Converter.')
    parser.add_argument(
        '--data_path', default='./data/kinetics_raw')
    arg = parser.parse_args()

    

    p = "train"
    p1 = "train1"

    label_path = '{}/kinetics_{}_label.json'.format(arg.data_path, p)
    data_out_path = '{}/kinetics_{}'.format(arg.data_path, p1)
    label_out_path = '{}/kinetics_{}_label.json'.format(arg.data_path, p1)


    # load file list

    sample_name = os.listdir(data_out_path)

    sample_id = [name.split('.')[0] for name in sample_name]

    with open(label_path) as f:
        label_info = json.load(f)

    
    label_t = dict()

    for id in sample_id:
        label_t[id] = label_info[id]
    
    with open(label_out_path, 'w', encoding="utf-8") as make_file:
        json.dump(label_t, make_file, indent = "\t")





