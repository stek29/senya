import os
import numpy as np
from numpy.lib.npyio import _savez as savez_internal
from senya import extract_faces

supersenya = []

for f in os.scandir('data/train/'):
    faces = extract_faces(f.path)
    print(f'{f.path}: got {len(faces)} faces', end=' - ')
    if len(faces) == 1:
        print('loaded!')
        supersenya.append(faces[0])
    else:
        print('need one face to train, skipping!')

savez_internal('supersenya2.npz', [], {'supersenya': np.array(supersenya)}, compress=True)
