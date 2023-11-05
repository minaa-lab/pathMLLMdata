
query_list_lesion=["What are the distinguishing features of this pathology image?",
"Can you tell me what lesions are shown in this pathology image?",
"What are the distinguishing features or abnormalities in this pathological image?",
"Can you analyze the lesions in this pathological image?",
"Please describe the features you observed in this pathology image. ",
"Can you describe this pathology image in detail?",
"Please provide more information about the feature of this pathological image.",
"Can you describe the salient features in this pathological image?",
"Please describe the possible lesions in this pathology image.",
"What features in this pathology image can aid in diagnosis?",
"Describe this pathology image.",
"Please describe the primary lesions or abnormalities in this pathology image."
]
query_list_normal=["Can you describe the features in this pathological image?",
"Describe this pathology image."]
pathYL_IMG_PATH = '/root/autodl-tmp/dataset/pathYL/images/'
import json
import random
def make_chatml_pathYL(pathYL_IMG_PATH,pathYL_ANNOTATION_PATH,caption_chatml_pathYL):
    with open(pathYL_ANNOTATION_PATH, 'r') as f:
        annotation = json.load(f)
        for key, value in annotation.items():
            img_id = key
            img_path = pathYL_IMG_PATH + img_id + '.png'
            img_caption_list = value['caption']
            img_label = value['label']
            if img_label != 0 and img_label != 3:
                for j in range(1,len(img_caption_list)):
                    query= random.choice(query_list_lesion)
                    query="<img>"+img_path+"</img> "+query
                    id = "caption" + "_" + "pathYL" + "_" + img_id+"_"+str(j)
                    answer = img_caption_list[j]
                    caption_chatml_pathYL.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
                # caption_chatml_pathYL.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
            elif img_label ==0:
                query= random.choice(query_list_normal)
                query="<img>"+img_path+"</img> "+query
                id="caption"+"_"+"pathYL"+"_"+img_id
                answer = img_caption_list[0]
                caption_chatml_pathYL.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
    return caption_chatml_pathYL

if __name__ == '__main__':
    pathYL_IMG_PATH = '/root/autodl-tmp/dataset/pathYL/images/'
    pathYL_ANNOTATION_PATH =["/root/autodl-tmp/dataset/pathYL/train_annotation.json","/root/autodl-tmp/dataset/pathYL/test_annotation.json"]
    caption_chatml_pathYL=[]
    caption_chatml_pathYL=make_chatml_pathYL(pathYL_IMG_PATH,pathYL_ANNOTATION_PATH[0],caption_chatml_pathYL)
    caption_chatml_pathYL=make_chatml_pathYL(pathYL_IMG_PATH,pathYL_ANNOTATION_PATH[1],caption_chatml_pathYL)
    with open('/root/autodl-tmp/dataset/pathYL/caption_chatml_pathYL.json', 'w') as f:
        json.dump(caption_chatml_pathYL, f)
    print("caption_chatml_pathYL.json saved successfully!")
    print(len(caption_chatml_pathYL))