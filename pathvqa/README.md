# pathvqa

[pathvqa]PathVQA is a dataset used for Visual Question Answering (VQA) tasks in the field of pathology. It contains images of pathological slides and corresponding questions and answers. The goal is to develop models that can accurately answer questions about the content of these images, aiding in tasks such as disease identification and understanding of pathological images.
we first use the BioCLIP model to filter out Hematoxylin and Eosin (H&E) stained pathological images from the PathVQA dataset. Then, we combine the filtered images with the QA dataset to generate a ChatML dataset.



Dataset

|  No. |       Name      |                         Link                               |  Count  |
|:----:|:---------------:|:----------------------------------------------------------:|:-------:|
|   1  |      Pathvqa    |             https://github.com/UCSD-AI4H/PathVQA           |  1046   |


Method
cleaner_pathvqa(): Use bioclip to find images of 'hematoxylin and eosin histopathology'.
make_chatml_pathvqa(): generates chatml queries and answers for each image and saves the results in a JSON file.
