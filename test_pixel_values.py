import numpy as np

pixels = np.load("metal_pixels/metal_00068.npy")
print("Shape:", pixels.shape)   # (height, width, 3)
print("Top-left pixel RGB:", pixels[0, 0])  # e.g. [123 45 67]