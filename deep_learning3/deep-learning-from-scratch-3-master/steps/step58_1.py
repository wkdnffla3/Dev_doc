if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from PIL import Image
import dezero
from dezero.models import VGG16



url = 'https://github.com/oreilly-japan/deep-learning-from-scratch-3/raw/images/zebra.jpg'
img_path = dezero.utils.get_file(url)
img = Image.open(img_path)
img.show()

x = VGG16.preprocess(img)
print(type(x),x.shape)
model = VGG16(pretrained=True)

x=np.random.randn(1,3,224,224).astype(np.float32)
model.plot(x)
