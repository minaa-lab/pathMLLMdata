
import json
import random
query_list_lesion_wsi = ["这张病理图像wsi有哪些明显的特征？",
"这张病理图像中显示了哪些病变吗？",
"这张病理图像中有哪些显著的特征或异常情况？",
"你能分析一下这张病理图像中的病变吗？",
"请描述你在这张病理图像中观察到的特征。",
"你能详细描述这张病理图像吗？",
"请提供有关这张病理图像特征。",
"你能描述这张病理图像中的显著特征吗？",
"请描述这张病理图像中可能存在的病变。",
"描述这张病理图像。",
"请描述这张病理图像中的主要病变或异常情况。"]
query_list_normal_wsi = ["你能描述一下这张病理图像中的特征吗？"]
import pandas as pd
data=pd.read_excel("/root/autodl-tmp/dataset/pathNarrtive/annotation.xlsx",sheet_name="Sheet1")
caption_chatml_pathNarrtive=[]
for i in range(len(data)):
    wsi_name=data["imgName"][i]
    wsi_path="/root/autodl-tmp/dataset/pathNarrtive/wsi_img/"+wsi_name+".png"
    wsi_label=data["gt"][i]
    wsi_caption="标本:"+str(data["标本"][i])+"诊断结果:" +str(data["诊断结果"][i])+" "+"大体所见:"+str(data["大体所见"][i])+" "+"镜下所见:"+str(data["镜下所见"][i])
    query= random.choice(query_list_lesion_wsi)
    query="<img>"+wsi_path+"</img> "+query
    id="caption"+"_"+"pathNarrtive"+"_"+wsi_name
    answer = wsi_caption
    caption_chatml_pathNarrtive.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
with open('/root/autodl-tmp/dataset/pathNarrtive/caption_chatml_pathNarrtive_wsi_zh.json', 'w') as f:
    json.dump(caption_chatml_pathNarrtive, f)
print("caption_chatml_pathNarrtive_wsi_zh.json saved successfully!")
print(len(caption_chatml_pathNarrtive))

   