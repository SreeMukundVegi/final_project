import requests
import json

# URL and headers provided
URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    """
    Calls Watson NLP EmotionPredict API to analyze emotions in the given text.
    Returns the 'text' attribute of the response.
    """
    # Create input JSON
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Make POST request
    response = requests.post(URL, headers=HEADERS, json=input_json)
    # Parse response
    if response.status_code == 200:
        result = response.json()

        # Extract emotions
        emotions = result['emotionPredictions'][0]['emotion']

        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Find dominant emotion
        scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(scores, key=scores.get)

        # Return formatted output
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

