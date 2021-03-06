# AUTOGENERATED! DO NOT EDIT! File to edit: 01_Filename_Processing.ipynb (unless otherwise specified).

__all__ = ['get_label', 'check_type', 'get_fnames', 'filter_fnames', 'show_data_count', 'get_noise_level',
           'classify_noise_levels', 'noise_levels', 'load_fnames']

# Cell
import pathlib
import os
import tensorflow as tf
import numpy as np
import pickle
import string

# Cell
def get_label(file_path):
    parts = tf.strings.split(file_path, os.path.sep)
    label_tensor = tf.strings.substr(parts[-1], pos=9, len=1)
    label = label_tensor.numpy().decode('utf-8')
    return label

def check_type(fname, dataset_type):
    label = get_label(fname)
    if dataset_type == 'digits' and label.isdigit():
        return True
    elif dataset_type == 'letters' and not(label.isdigit()):
        return True
    return False

def get_fnames(data_dir):
    return tf.io.gfile.glob(str(data_dir)+"*/*.wav")

def filter_fnames(fnames):
    return [fname for fname in fnames if check_type(fname, dataset_type)]

def show_data_count(filenames, label_strings):
    for i in range(len(label_strings)):
        num_examples = len([fname for fname in filenames if get_label(fname)==label_strings[i]])
        print(f"""# examples for "{label_strings[i]}": {num_examples}""")

    num_samples = len(filenames)
    print('# total examples:', num_samples)
    print()

# Cell
noise_levels = ['IDL', '35D', '35U', '55D', '55U']

def get_noise_level(file_path):
    parts = tf.strings.split(file_path, os.path.sep)
    level_tensor = tf.strings.substr(parts[-1], pos=4, len=3)
    level = level_tensor.numpy().decode('utf-8')
    return level

def classify_noise_levels(fnames):
    noise_levels = ['IDL', '35D', '35U', '55D', '55U']
    noise_levels_dict = {}
    # initialize empty lists
    for level in noise_levels:
        noise_levels_dict[level] = []
    # put each filename into a category
    for fname in fnames:
        noise_level = get_noise_level(fname)
        noise_levels_dict[noise_level].append(fname)
    return noise_levels_dict



# Cell
def load_fnames(fname_path):
    with open(fname_path, 'rb') as filehandle:
        return pickle.load(filehandle)