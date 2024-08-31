from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googleapiclient import discovery

from utility.data_loader import DataLoader

import time


class AlgosENG():

    @staticmethod
    def annotate_google_jigsaw(templates, loc:str, API_KEY:str):


        client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=API_KEY,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
        )

        for index, element in templates.iterrows():
            analyze_request = {
                'comment': {'text': element['text']},
                'requestedAttributes': {'IDENTITY_ATTACK': {}},
                'languages': ['en'],
                'doNotStore': True
            }

            try:
                res = client.comments().analyze(body=analyze_request).execute()
                if res['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value'] < 0.5:
                    res = 'non-hateful'
                else:
                    res = 'hateful'

                templates.loc[index, 'Prediction'] = res
            except Exception as e:
                print(e)
                templates.loc[index, 'Prediction'] = 'na'
            time.sleep(1.15)
        DataLoader.save_df_to_csv(templates, loc)

    @staticmethod
    def annotate_IMSyPP(templates, loc):
        tokenizer = AutoTokenizer.from_pretrained("IMSyPP/hate_speech_en")
        model = AutoModelForSequenceClassification.from_pretrained("IMSyPP/hate_speech_en")
        for index, element in templates.iterrows():
            res = model.config.id2label[
                (model(**tokenizer(element['text'], return_tensors="pt")).logits).argmax().item()]

            if res == 'LABEL_0':
                res = 'non-hateful'
            else:
                res = 'hateful'

            templates.loc[index, 'Prediction'] = res
        DataLoader.save_df_to_csv(templates, loc)

    @staticmethod
    def annotate_hate_explain(templates, loc):
        tokenizer = AutoTokenizer.from_pretrained("Hate-speech-CNERG/bert-base-uncased-hatexplain")
        model = AutoModelForSequenceClassification.from_pretrained("Hate-speech-CNERG/bert-base-uncased-hatexplain")
        for index, element in templates.iterrows():
            res = model.config.id2label[
                (model(**tokenizer(element['text'], return_tensors="pt")).logits).argmax().item()]

            if res == 'normal':
                res = 'non-hateful'
            else:
                res = 'hateful'

            templates.loc[index, 'Prediction'] = res
        DataLoader.save_df_to_csv(templates, loc)

    def annotate_roberta(templates, loc):
        tokenizer = AutoTokenizer.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")
        model = AutoModelForSequenceClassification.from_pretrained("facebook/roberta-hate-speech-dynabench-r4-target")

        for index, element in templates.iterrows():
            res = model.config.id2label[
                (model(**tokenizer(element['text'], return_tensors="pt")).logits).argmax().item()]

            if res == 'nothate':
                res = 'non-hateful'
            else:
                res = 'hateful'

            templates.loc[index, 'Prediction'] = res
        DataLoader.save_df_to_csv(templates, loc)
