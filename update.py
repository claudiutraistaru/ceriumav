import os
import numpy as np
import requests
import sys
from tqdm import tqdm
import math

def main():
    print(" == CERIUM AV VIRUS DATABASE UPDATER ==\n")
    if not os.path.isdir("tmp-update"):
        os.mkdir("tmp-update")
    DOWNLOAD_UPDATE()
    COMBINE_INTO_ONE()

def DOWNLOAD_UPDATE():
    url = "http://localhost:8000/abcd.apk"
    filename = "./tmp-update/udpate-today"
    r= requests.get(url ,stream=True )
    total_size = int(r.headers.get('content-length' , 0));
    block_size = 1024
    wrote = 0
    with open(filename , "wb") as f:
        for data in tqdm(r.iter_content(block_size) , total = math.ceil(total_size/block_size) ,unit = "kb", unit_scale = True):
            wrote = wrote + len(data)
            f.write(data)
    if total_size!=0 and wrote!= total_size:
        print("Something Went Wrong")


def COMBINE_INTO_ONE():
    dbfile = []

    vx = np.array(dbfile)
    for file in os.listdir("./tmp-update"):
        if file.endswith(".cdb"):
            # print(os.path.join("./", file))
            dbfile.append(file)
            file = np.load("./tmp-update/"+file)
            vx = np.concatenate((vx , file['sign']) , axis = 0)
        # print(dbfile)
        # print(vx)
        np.savez_compressed("./signs/MAINDB" , sign=vx)
        os.rename("./signs/MAINDB.npz", "./signs/MAINDB.cdb")

if __name__ == '__main__':
    main()
