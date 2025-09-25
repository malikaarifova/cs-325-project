

from PIL import Image
import numpy as np

# Open image
img = Image.open("image.jpg")

# Convert to RGB if not already
img = img.convert("RGB")

# Convert to NumPy array
pixel_array = np.array(img)

print(pixel_array.shape)  # (height, width, 3)
print(pixel_array[0,0]) 