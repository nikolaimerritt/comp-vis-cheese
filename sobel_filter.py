from matplotlib.pyplot import sci
import numpy as np
from scipy.signal import convolve2d

def read2dArray(filename):
    with open(filename, "r") as file:
        array = [
            [int(el) for el in line.split(" ") if len(el) > 0]
            for line in file.readlines()
        ]

    array = np.array(array)

    return array


image = read2dArray("image.txt")
h_x = read2dArray("sobel_h_x.txt")
h_y = read2dArray("sobel_h_y.txt")
laplacian = read2dArray("laplacian.txt")

convolved_x = convolve2d(image, h_x, mode="valid")
print(f"image * h_x = \n{convolved_x} \n\n")

convolved_y = convolve2d(image, h_y, mode="valid")
print(f"image * h_y = \n{convolved_y} \n\n")

convolved_laplace = convolve2d(image, laplacian, mode="valid")
print(f"image * laplacian = \n{convolved_laplace} \n\n")