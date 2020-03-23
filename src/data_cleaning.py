import os
import sys
module_path = os.path.abspath(os.path.join(os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)

import pandas as pd

def create_df(csv):
    relative_filename = os.path.abspath(os.path.join(os.pardir, 'data', csv))
    df1 = pd.read_csv(relative_filename)

    return df1