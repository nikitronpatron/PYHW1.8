import os
import json
import csv
import pickle
from .file_info import FileInfo

def save_file_info_to_json(directory, output_file):
    file_infos = get_file_info(directory)
    with open(output_file, 'w') as json_file:
        json.dump([info.to_dict() for info in file_infos], json_file, indent=4)

def save_file_info_to_csv(directory, output_file):
    file_infos = get_file_info(directory)
    with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ["path", "name", "is_dir", "size"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for info in file_infos:
            writer.writerow(info.to_dict())

def save_file_info_to_pickle(directory, output_file):
    file_infos = get_file_info(directory)
    with open(output_file, 'wb') as pickle_file:
        pickle.dump([info.to_dict() for info in file_infos], pickle_file)

def get_file_info(directory):
    file_infos = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = FileInfo(file_path)
            file_infos.append(file_info)
    return file_infos