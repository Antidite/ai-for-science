from torchvision import transforms
from PIL import Image

#python的用法 -> tensor数据类型
#  通过 transforms.ToTensor

#2.Tensor数据类型有什么用

#绝对路径F:\ai4s\pycharm\code\learn_pytorch\train\ants_image\6743948_2b8c096dda.jpg
#相对路径train/ants_image/6743948_2b8c096dda.jpg
img_path = "train/ants_image/6743948_2b8c096dda.jpg"
img = Image.open(img_path)

#1.transforms该如何使用（python）
tensor_trans = transforms.ToTensor() #rename and conduct
tensor_image = tensor_trans(img)

print(tensor_image)
