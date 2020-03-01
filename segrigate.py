#!/usr/bin/python3

import shutil
import csv
import os

def move_file(src, dst):
    shutil.copy(src, dst)

def read_csv():
    f = open("./Train.csv", 'r')
    reader = csv.reader(f)
    headers = next(reader, None)
    column = {}
    for h in range(1,17):
        column[str(h)] = []
    for row in reader:
        column[row[1]].append(row[0])
    return column

def segrigate(final_dict):
    os.mkdir("./segri_dir")
    for dir_name in final_dict.keys():
        os.mkdir("./segri_dir/" + dir_name)
    print("Done cereating dirs")
    for cat_num in final_dict.keys():
        for file_name in final_dict[cat_num]:
            move_file("./train/"+file_name, "./segri_dir/" + cat_num)

if __name__ == '__main__':
    final_dict = {}
    final_dict = read_csv()
    print("I am done with population")
    segrigate(final_dict)
    print("Done with populatting file in dir")
    print("1st chnages for GIT")
    print("2nd changes for GIT")
    
