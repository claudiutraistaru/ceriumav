import zlib
import os
import numpy as np

def pack(filename):
    filename = str(filename)
    if os.path.isfile(filename):
        # print("File Found")
        vl = open(filen).read().splitlines()
        # a = str(a)
        vl = np.array(vl)
        # a = numpy.array(a)
    # print(a)
    # b = zlib.compress(a , 0)
    # raw_data = "import numpy\nC_MALS = numpy.array(" + a + ")"
    # newfile = open("newdb.py" , "wb")
    # newfile.write(raw_data.encode())
    # print(a)
    np.savez_compressed(filename +".cdb" , sign=vl)
    os.rename(filename + ".cdb.npz", filename+".cdb")
