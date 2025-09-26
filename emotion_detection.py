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
        return result  # full response
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}
