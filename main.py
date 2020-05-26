import numpy as np
import os
from PIL import Image
im=Image.open("apple1.jpg")
im.show()
image_array=np.array(im)
for k in range(2):
        i = int(np.random.random() * image_array.shape[1]);
        j = int(np.random.random() * image_array.shape[0]);
        if image_array.ndim == 2:
            image_array[j,i] = 255
        elif image_array.ndim == 3:
            image_array[j,i,0]= 255
            image_array[j,i,1]= 255
            image_array[j,i,2]= 255
im = Image.fromarray(image_array.astype('uint8')).convert('RGB')
im.show()
