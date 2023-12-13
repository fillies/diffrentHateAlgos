from googleapiclient import discovery

from utility.data_loader import DataLoader

import time


class AlgosDE():

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
                'languages': ['de']
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

