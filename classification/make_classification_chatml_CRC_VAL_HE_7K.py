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

# 初始化对话列表
conversations = []

# 设置图像ID的初始值
image_id = 0

# 构造对话
for i in range(7180):
    folder_name = random.choice(list(abbr_to_full.keys()))
    folder_path = os.path.join(dataset_path, folder_name)
    image_files = os.listdir(folder_path)
    image_file = random.choice(image_files)

    image_path = os.path.join(folder_path, image_file)

    # 用户问题
    user_question = f"Which category does this pathological images belong to? Choose one of the following categories: 'Adipose', 'Background', 'Debris', 'Lymphocytes', 'Mucus', 'Smooth Muscle', 'Normal Colon Mucosa', 'Cancer-Associated Stroma', 'Colorectal Adenocarcinoma Epithelium' <img>{image_path}</img>"

    # 生成随机的助手回答
    selected_category = random.choice(list(abbr_to_full.values()))
    assistant_answer = f"{selected_category}"

    # 为每个对话分配独立的ID
    conversation_id = f"image_{image_id}"

    # 添加对话阶段
    conversations.append({"id": conversation_id, "conversations": [
        {"from": "user", "value": user_question},
        {"from": "assistant", "value": assistant_answer}
    ]})

    # 更新图像ID
    image_id += 1

# 将 JSON 数据保存为文件
output_file = 'C:\LuoLab\pathMLLMdata\classification\CRC-VAL-HE-7K\CRC_VAL_HE_7K_chatml.json'
with open(output_file, 'w') as f:
    json.dump(conversations, f, indent=2)

print(f"{len(conversations)} conversation stages created and saved in {output_file}")
