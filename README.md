# BERT Intent Classifier for CLINC150 Dataset

Pytorch and Huggingface implementation of a intent classifier with BERT as the encoder and a MLP as the classification head.
While developed for [CLINC150](https://github.com/clinc/oos-eval) dataset, simply pass new dataset in form of .json work just fine.
- This repo fork from https://github.com/ginofft/BertClassifier to add a small Demo  


## Quick Start
- Download the model here: [Drive](https://drive.google.com/drive/u/0/folders/16ZrBGLpimLrvQ7l3UYi6WgKcFyjZdA78)
- Create a folder name **model** and put model following the path: `model/<put_model_here>` 
- Install requirements
```python
pip install -r requirements.txt
```
- Clone **Demo** branch
```git
git clone -b demo https://github.com/anhkhoa039/BertClassifier.git
```
- Run
```python
flask --app app run
```
