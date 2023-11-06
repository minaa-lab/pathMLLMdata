import os
import random
import json

# 指定数据集文件夹路径
dataset_path = 'C:\LuoLab\pathMLLMdata\classification\CRC-VAL-HE-7K\CRC-VAL-HE-7K'

# 定义缩写到全称的映射字典
abbr_to_full = {
    "ADI": "Adipose",
    "BACK": "Background",
    "DEB": "Debris",
    "LYM": "Lymphocytes",
    "MUC": "Mucus",
    "MUS": "Smooth Muscle",
    "NORM": "Normal Colon Mucosa",
    "STR": "Cancer-Associated Stroma",
    "TUM": "Colorectal Adenocarcinoma Epithelium"
}


# 初始化问答对列表
qa_pairs = []

# 设置图像ID的初始值
image_id = 1

# 定义多样的问题列表
question_templates = [
    "Which category does this image belong to?",
    "What is the primary category for this image?",
    "Identify the category of this image.",
    "Specify the class of this image.",
    "Categorize this image."
]

# 构造问答对
for i in range(7180):
    folder_name = random.choice(list(abbr_to_full.keys()))
    folder_path = os.path.join(dataset_path, folder_name)
    image_files = os.listdir(folder_path)
    image_file = random.choice(image_files)

    image_path = os.path.join(folder_path, image_file)
    question = random.choice(question_templates)
    multiple_choices = list(abbr_to_full.values())
    answer = abbr_to_full[folder_name]
    qa_id = image_id

    qa_pairs.append({
        "image_id": image_id,
        "question": question,
        "multiple_choices": multiple_choices,
        "qa_id": qa_id,
        "answer": answer,
        "type": "category"
    })

    image_id += 1

# 将问答对保存为JSON文件
output_file = 'C:\LuoLab\pathMLLMdata\classification\CRC-VAL-HE-7K\CRC_VAL_HE_7K_chatml.json'
with open(output_file, 'w') as f:
    json.dump({"qa_pairs": qa_pairs}, f, indent=2)

print(f"{len(qa_pairs)} QA pairs created and saved in {output_file}")
