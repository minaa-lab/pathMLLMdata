query_list_lesion=["Could you use a few keywords to summarize the pathological features of this pathology image patch?",
"Please list the main keywords to encapsulate the pathological lesion of this pathology image patch.",
"Can you provide a set of keywords to summarize the  lesion in this pathology image patch?",
"Please offer a set of keywords to outline characteristics of this pathology image patch.",
"Concisely summarize the pathological lesion of this pathology image patch using a few keywords.",
"Please describe this pathology image patch with a few keywords.",
"What keywords can you provide to succinctly characterize the pathological traits observed in this pathology image patch?"
"Please generate a set of keywords to concisely outline the pathological features within this pathology image patch.",
"Please create a descriptive caption for this pathology image.",
"Generate caption to summarize the lesion of this pathology image."
"Please provide a caption for this pathology image to better grasp its features."]
query_list_normal=["Please describe the features in this pathology image patch with a few keywords.",
"Please offer a set of keywords to outline characteristics of this pathology image patch.",
"Concisely summarize the features of this pathology image patch using a few keywords.",
"Please give a caption for this pathology image patch."]
subtypes2label = {0:0,1:1,2:1,3:2,4:2,5:2,6:2,7:2}
import random
path_Narrtive_IMG_PATH = '/root/autodl-tmp/dataset/pathNarrtive/3class_img_patch_10000/'
import pandas as pd
import json
def make_chatml_pathNarrtive(path_Narrtive_IMG_PATH,path_Narrtive_ANNOTATION_PATH,caption_chatml_pathNarrtive):
    annotation = json.load(open(path_Narrtive_ANNOTATION_PATH, 'r'))
    for i in range(len(annotation)):
        caption = annotation[i]['caption']
        patch_list=annotation[i]['patches']
        label=subtypes2label[annotation[i]['subtype']]
        max_patch=50
        if len(patch_list)<max_patch:
            max_patch=len(patch_list)
        j_list=random.sample(range(len(patch_list)),max_patch)
        for j in j_list:
            patch_id=patch_list[j]
            img_path = path_Narrtive_IMG_PATH +str(label)+"/"+ patch_id + '.png'
            if label != 0:
                query= random.choice(query_list_lesion)
                query="<img>"+img_path+"</img> "+query
                id="caption"+"_"+"pathNarrtive"+"_"+patch_id.split(".")[0]
                answer = caption
                caption_chatml_pathNarrtive.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
            elif label ==0:
                query= random.choice(query_list_normal)
                query="<img>"+img_path+"</img> "+query
                id="caption"+"_"+"pathNarrtive"+"_"+patch_id
                answer = caption
                caption_chatml_pathNarrtive.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})

    return caption_chatml_pathNarrtive

if __name__ == '__main__':
    pathpathNarrtive_IMG_PATH = '/root/autodl-tmp/dataset/pathYL/images/'
    pathpathNarrtive_ANNOTATION_PATH ="/root/autodl-tmp/dataset/pathNarrtive/train_translated_data.json"
    patch_caption_chatml_pathpathNarrtive=[]
    patch_caption_chatml_pathpathNarrtive=make_chatml_pathNarrtive(pathpathNarrtive_IMG_PATH,pathpathNarrtive_ANNOTATION_PATH,patch_caption_chatml_pathpathNarrtive)
    with open('/root/autodl-tmp/dataset/pathNarrtive/patch_caption_chatml_pathpathNarrtive.json', 'w') as f:
        json.dump(patch_caption_chatml_pathpathNarrtive, f)
    print("patch_caption_chatml_pathpathNarrtive.json saved successfully!")
    print(len(patch_caption_chatml_pathpathNarrtive))
