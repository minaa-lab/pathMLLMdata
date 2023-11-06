import json
import os
import random

import h5py

# 指定 PNG 图像文件夹路径
images_folder = 'C:\LuoLab\pathMLLMdata\classification\PCam\images'
# 指定 HDF5 标签文件路径
labels_file = 'C:\LuoLab\pathMLLMdata\classification\PCam\camelyonpatch_level_2_split_train_y.h5'

# 定义查询列表
query_list_cancer = ["Does this image contain cancerous cells?",
                     "Can you identify cancer cells in this image?",
                     "Please tell me if cancer is present in this image.",
                     "Are there signs of cancer in this image?",
                     "Could you please determine if there are cancer cells in this image?",
                     "Is this image depicting malignant cells?"]

query_list_normal = ["Describe the features in this image.",
                     "Please provide details about this image."]


def get_label_value(label_data):
    # 提取有效的标签值，根据具体情况可能需要修改索引
    return label_data[0][0][0]


def make_chatml_data(images_folder, labels_file, caption_chatml_data):
    # 列出图像文件夹中的所有 JPG 图像文件
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]

    # 打开 HDF5 标签文件
    with h5py.File(labels_file, 'r') as labels_h5:
        labels = labels_h5['y'][:10001]

    for i, image_file in enumerate(image_files):
        img_path = os.path.join(images_folder, image_file)
        img_label = get_label_value(labels[i])  # 获取有效的标签值

        if img_label == 1:  # 包含癌症细胞
            query = random.choice(query_list_cancer)

        else:  # 正常图像
            query = random.choice(query_list_normal)

        query = "<img>" + img_path + "</img> " + query
        id = "image_" + str(i)

        if img_label == 1:
            answer = "Yes, this image contains cancerous cells."
        else:
            answer = "No, there are no cancerous cells in this image."

        caption_chatml_data.append(
            {"id": id, "conversations": [{"from": "user", "value": query}, {"from": "assistant", "value": answer}]})


if __name__ == '__main__':
    caption_chatml_data = []
    make_chatml_data(images_folder, labels_file, caption_chatml_data)

    with open('C:\LuoLab\pathMLLMdata\classification\PCam\chatml_data.json', 'w') as json_file:
        json.dump(caption_chatml_data, json_file)

    print("ChatML data saved to chatml_data.json.")
