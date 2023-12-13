from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googleapiclient import discovery

from utility.data_loader import DataLoader

import time


class AlgosMulti():

    @staticmethod
    def annotate_xlm_Roberta_Large(templates, loc):
        tokenizer = AutoTokenizer.from_pretrained("christinacdl/xlm_Roberta_Large_hate_speech_multilingual_binary")
        model = AutoModelForSequenceClassification.from_pretrained(
            "christinacdl/xlm_Roberta_Large_hate_speech_multilingual_binary")

        for index, element in templates.iterrows():
            res = model.config.id2label[
                (model(**tokenizer(element['text'], return_tensors="pt")).logits).argmax().item()]

            if res == 'NOT':
                res = 'non-hateful'
            else:
                res = 'hateful'

            templates.loc[index, 'Prediction'] = res
        DataLoader.save_df_to_csv(templates, loc)

    def annotate_robaconfi(templates, loc):
        tokenizer = AutoTokenizer.from_pretrained("Andrazp/multilingual-hate-speech-robacofi")
        model = AutoModelForSequenceClassification.from_pretrained("Andrazp/multilingual-hate-speech-robacofi")

        for index, element in templates.iterrows():
            res = model.config.id2label[
                (model(**tokenizer(element['text'], return_tensors="pt")).logits).argmax().item()]

            if res == 'not offensive':
                res = 'non-hateful'
            else:
                res = 'hateful'

            templates.loc[index, 'Prediction'] = res
        DataLoader.save_df_to_csv(templates, loc)