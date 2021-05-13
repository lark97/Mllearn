import os
import random
import matplotlib.pyplot as plt

import skimage
from skimage import io

basedir = os.getcwd()
test_dir = os.path.join(basedir, "images")
file_names = next(os.walk(test_dir))[2]
# image = skimage.io.imread(os.path.join(test_dir, random.choice(file_names)))
# plt.imshow(image)
# plt.show()

print(file_names)




