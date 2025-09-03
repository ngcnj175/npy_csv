import numpy as np
import sys

# 使い方: python convert.py input.npy output.csv

infile = sys.argv[1]
outfile = sys.argv[2]

arr = np.load(infile)
np.savetxt(outfile, arr, delimiter=",")
print(f"✅ Converted {infile} → {outfile}")
