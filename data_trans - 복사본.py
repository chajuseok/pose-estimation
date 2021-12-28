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
    parser.add_argument(
        '--out_folder', default='./data/kinetics')
    arg = parser.parse_args()


    if not os.path.exists(arg.out_folder):
        os.makedirs(arg.out_folder)
    

    p = "train"
    p1 = "train1"
    data_path = '{}/kinetics_{}'.format(arg.data_path, p)

    data_out_path = '{}/kinetics_{}'.format(arg.data_path, p1)



    # load file list
    sample_name = os.listdir(data_path)

    
    for i in sample_name:
        with open(data_path +"/"+ i) as f:
            label_info = json.load(f)
            index = label_info['label_index']
            if(index < 101):
                shutil.copy2(data_path + "/" + i,data_out_path + "/" + i)

    print("done")
    
    




    


