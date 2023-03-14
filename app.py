from scr.dataset import  SentenceLabelDataset
from transformers import BertTokenizer
from scr.models import BertMLPClassifier
from scr.utils import load_checkpoint, read_CLINC150_file, get_label_set, turn_single_label_to_multilabels
from scr.utils import predict_class
import torch

import os, glob
from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__, static_url_path="/static")

################################################################################
dataPath = 'data/CLINC150/data_oos_plus.json'
dataDict = read_CLINC150_file(dataPath)

device = torch.device('cpu')
trainList = dataDict['train'] + dataDict['oos_train']
valList = dataDict['val'] + dataDict['oos_val']
testList = dataDict['test'] + dataDict['oos_test']

turn_single_label_to_multilabels(trainList, valList, testList)
labelSet = get_label_set(trainList, valList, testList)

trainSet = SentenceLabelDataset(trainList, labelSet, tokenizer = BertTokenizer.from_pretrained('bert-base-uncased'))
tokenizer = trainSet.tokenizer

modelPath = 'model/best.pth.tar'
model = BertMLPClassifier()
# model.to(device)
load_checkpoint(modelPath, model,device=device)
################################################################################



@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        data = request.form['input_textbox']
        print (data)
        # result = data.split()
        if data:
            result = predict_class(data, model, tokenizer, labelSet)
        else:
            result = ''
        return render_template("index.html",result=result)
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)