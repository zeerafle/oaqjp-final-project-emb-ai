import requests


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 400:
        return {"anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                'dominant_emotion': None}

    emotions = response.json()['emotionPredictions'][0]['emotion']
    
    # emotions['dominant_emotion'] = for k, v in emotions.items()
    highest_emo_idx = list(emotions.values()).index(max(list(emotions.values())))
    emotions['dominant_emotion'] = list(emotions.keys())[highest_emo_idx]

    return emotions
