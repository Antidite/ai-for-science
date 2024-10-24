from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
image_path = "train/ants_image/5650366_e22b7e1065.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
#writer.add_image需要看image formats HWC or CHW or others print(img_array.shape)

writer.add_image("train", img_array, 1, dataformats='HWC')
#y = x
for i in range(100):
    writer.add_scalar("y=2x",i*i,i)

writer.close()
