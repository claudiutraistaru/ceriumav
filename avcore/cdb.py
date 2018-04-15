# virus signature database


# nudb_dict = {
#     'c7e4f11a217215144679ad56199d4ca6' : 'TestVirus.Dir.PY',
#     'ecda09d2814e862a8437c818621fcdb1' : "testvirus.Test2.TXT",
#     'bbfa1f311a5828452b953d1335cbf027' : 'testvirus.Test.TXT'

# }

import numpy as np
import os
maindb = np.load("./signs/MAINDB.cdb")

cdb_dict = maindb['sign']
