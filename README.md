# pathMLLMdata

## Classification


## Caption
[caption]Pathological caption is mainly used to describe the microscopic view of WSI or PATCH, lesion characteristics, and general image features. The main data sources are shown in the table below.



Dataset

|  No. |       Name      |                         Link                               |  Count  |
|:----:|:---------------:|:----------------------------------------------------------:|:-------:|
|   1  |      PathYL     |    https://figshare.com/projects/nmi-wsi-diagnosis/61973   |  14337  |
|   2  |PatchGastricADC22| https://github.com/masatsuneki/histopathology-image-caption|         |
|   3  |   PathNarrative |                                                            |patch2454|
|   3  |   PathNarrative |                                                            |wsi   83 |
|   4  |      OpenPath   |             https://tinyurl.com/openpathdata               |         |


## vqa
[pathvqa]PathVQA is a dataset used for Visual Question Answering (VQA) tasks in the field of pathology. It contains images of pathological slides and corresponding questions and answers. The goal is to develop models that can accurately answer questions about the content of these images, aiding in tasks such as disease identification and understanding of pathological images.
we first use the BioCLIP model to filter out Hematoxylin and Eosin (H&E) stained pathological images from the PathVQA dataset. Then, we combine the filtered images with the QA dataset to generate a ChatML dataset.



Dataset

|  No. |       Name      |                         Link                               |  Count  |
|:----:|:---------------:|:----------------------------------------------------------:|:-------:|
|   1  |      Pathvqa    |             https://github.com/UCSD-AI4H/PathVQA           |  1046   |


