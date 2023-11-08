# pathMLLMdata

## Classification


## Caption
[caption]Pathological caption is mainly used to describe the microscopic view of WSI or PATCH, lesion characteristics, and general image features. The main data sources are shown in the table below.



Dataset

|  No. |       Name      |                         Link                               |         Count       |
|:----:|:---------------:|:----------------------------------------------------------:|:-------------------:|
|   1  |      PathYL     |    https://figshare.com/projects/nmi-wsi-diagnosis/61973   |         14337       |
|   2  |PatchGastricADC22| https://github.com/masatsuneki/histopathology-image-caption|                     |
|   3  |   PathNarrative |                                                            | patch2454 // wsi 83 |
|   4  |      OpenPath   |             https://tinyurl.com/openpathdata               |                     |


## vqa
[pathvqa]PathVQA is a dataset used for Visual Question Answering (VQA) tasks in the field of pathology. It contains images of pathological slides and corresponding questions and answers. The goal is to develop models that can accurately answer questions about the content of these images, aiding in tasks such as disease identification and understanding of pathological images.
we first use the BioCLIP model to filter out Hematoxylin and Eosin (H&E) stained pathological images from the PathVQA dataset. Then, we combine the filtered images with the QA dataset to generate a ChatML dataset.



Dataset

|  No. |       Name      |                         Link                               |  Count  |
|:----:|:---------------:|:----------------------------------------------------------:|:-------:|
|   1  |      Pathvqa    |             https://github.com/UCSD-AI4H/PathVQA           |  1046   |

## classification
[classification]
PCam consists of 10,000 color images (96 x 96px) extracted from histopathologic scans of lymph node sections. Each image is annoted with a binary label indicating presence of metastatic tissue.

NCT-CRC-HE-100K is a set of 100,000 non-overlapping image patches from hematoxylin & eosin (H&E) stained histological images of human colorectal cancer (CRC) and normal tissue.

Dataset

| No.  |      Name       |                             Link                             | Count |
| :--: | :-------------: | :----------------------------------------------------------: | :---: |
|  1   |      PCam       | [basveeling/pcam: The PatchCamelyon (PCam) deep learning classification benchmark. (github.com)](https://github.com/basveeling/pcam) | 10000 |
|  2   | NCT-CRC-HE-100K | [100,000 histological images of human colorectal cancer and healthy tissue (zenodo.org)](https://zenodo.org/records/1214456) | 10000 |


