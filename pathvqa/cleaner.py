import open_clip
import glob
from collections import OrderedDict
import json
import torch
from PIL import Image
import open_clip
path_vqa_IMG_PATH='/root/autodl-tmp/dataset/pathvqa/Images/'
def  cleaner_pathvqa():
    dataset_path = '/root/autodl-tmp/dataset/pathvqa'
    template = 'this is a photo of '
    labels = [
        'hematoxylin and eosin histopathology',
        'structure figure',
        'chart',
        'muti figure',
    ]

    test_imgs = glob.glob(dataset_path + '/*')

    model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224')
    tokenizer = open_clip.get_tokenizer('hf-hub:microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224')

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    model.eval()

    context_length = 256

    # Process images in batches
    batch_size = 10
    he_img = []
    for i in range(0, len(test_imgs), batch_size):
        batch_imgs = test_imgs[i:i+batch_size]
        images = torch.stack([preprocess_val(Image.open(img)) for img in batch_imgs]).to(device)
        texts = tokenizer([template + l for l in labels], context_length=context_length).to(device)
        with torch.no_grad():
            image_features, text_features, logit_scale = model(images, texts)

            logits = (logit_scale * image_features @ text_features.t()).detach().softmax(dim=-1)
            sorted_indices = torch.argsort(logits, dim=-1, descending=True)

            logits = logits.cpu().numpy()
            sorted_indices = sorted_indices.cpu().numpy()

        top_k = -1
        for i, img in enumerate(batch_imgs):
            pred = labels[sorted_indices[i][0]]

            top_k = len(labels) if top_k == -1 else top_k
            for j in range(top_k):
                jth_index = sorted_indices[i][j]
                if labels[jth_index]=='hematoxylin and eosin histopathology' and logits[i][jth_index]>0.98:
                    he_img.append(img)

        # Delete tensors to free up memory
        del images, texts, image_features, text_features, logit_scale, logits, sorted_indices
        torch.cuda.empty_cache()
    return he_img



def make_chatml_pathvqa():
    pathvqa_chatml= []
    he_img = cleaner_pathvqa()
    he_img_filename = [i.split('/')[-1]. split('.')[0] for i in he_img]
    qa_json=json.load(open('/root/autodl-tmp/dataset/QA_pairs_vb.json','r'))
    for i in range(len(qa_json)):
        if qa_json[i]['Image_ID'] in he_img_filename:
            id = "path_vqa_"+ qa_json[i]['Image_ID']+"_"+str(i)
            img_path = path_vqa_IMG_PATH + qa_json[i]['Image_ID']+ '.jpg'
            query= qa_json[i]['Questions']
            query="<img>"+img_path+"</img> "+query
            answer = qa_json[i]['Answers']
            pathvqa_chatml.append({"id":id,"conversations":[{"from":"user","value":query},{"from":"assistant","value":answer}]})
    with open('/root/autodl-tmp/dataset/pathvqa_chatml.json', 'w') as outfile:
        json.dump(pathvqa_chatml, outfile)
    print("pathvqa_chatml.json created")
    print(len(pathvqa_chatml))
    return pathvqa_chatml
make_chatml_pathvqa()
        