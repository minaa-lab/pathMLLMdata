
import h5py
from PIL import Image
import numpy as np

# 打开 .h5 文件
h5_file = h5py.File(r'C:\LuoLab\pathMLLMdata\classification\PCam\camelyonpatch_level_2_split_train_x.h5', 'r')

# 获取图像数据
images_data = h5_file['x']  # 假设数据集名称为 "images"

# 遍历前 500 行数据并保存为图像文件
for i, img_data in enumerate(images_data[:5000]):
    # 假设图像数据是二维数组
    img = Image.fromarray(img_data, mode='RGB')  # 'L' 表示灰度图像

    # 保存图像为 JPEG 文件（或者使用其他格式如 PNG）
    img.save(rf'C:\LuoLab\pathMLLMdata\classification\PCam\images\output_image_{i}.jpg')

